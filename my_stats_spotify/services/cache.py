"""Caché persistente de estadísticas de Spotify.

La app lee un snapshot JSON generado por GitHub Actions (cada ~3 minutos)
en lugar de llamar a la API de Spotify en cada carga de página. Así se
evitan rate limits y la UI sigue funcionando aunque Spotify falle.

Origen de datos (en orden):

1. URL remota ``SPOTIFY_CACHE_URL`` (rama ``spotify-data`` en GitHub).
2. Archivo local ``data/spotify_cache.json``.
"""

from __future__ import annotations

import json
import logging
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import requests

logger = logging.getLogger(__name__)

REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_CACHE_PATH = REPO_ROOT / "data" / "spotify_cache.json"
DEFAULT_CACHE_URL = (
    "https://raw.githubusercontent.com/santyjL/mi-stats-spotify/"
    "spotify-data/spotify_cache.json"
)

SnapshotTuple = tuple[
    dict | None,
    dict | None,
    dict | None,
    dict | None,
    list[dict[str, str | int]] | None,
    dict | None,
    dict | None,
]


def cache_path() -> Path:
    """Ruta del snapshot local (configurable con ``SPOTIFY_CACHE_PATH``)."""
    override = os.getenv("SPOTIFY_CACHE_PATH")
    if override:
        return Path(override)
    return DEFAULT_CACHE_PATH


def cache_url() -> str:
    """URL del snapshot remoto (configurable con ``SPOTIFY_CACHE_URL``)."""
    return os.getenv("SPOTIFY_CACHE_URL", DEFAULT_CACHE_URL).strip()


def snapshot_from_payload(payload: dict[str, Any]) -> SnapshotTuple:
    """Convierte el JSON guardado a la tupla que espera la UI."""
    return (
        payload.get("perfil"),
        payload.get("artistas"),
        payload.get("canciones"),
        payload.get("historial"),
        payload.get("albumes"),
        payload.get("reproduccion_actual"),
        payload.get("artistas_mes"),
    )


def build_payload(
    perfil: dict | None,
    artistas: dict | None,
    canciones: dict | None,
    historial: dict | None,
    albumes: list[dict[str, str | int]] | None,
    reproduccion_actual: dict | None,
    artistas_mes: dict | None,
    *,
    limite: int = 30,
    rango: str = "medium_term",
) -> dict[str, Any]:
    """Construye el documento JSON del snapshot."""
    return {
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "limite": limite,
        "rango": rango,
        "perfil": perfil,
        "artistas": artistas,
        "canciones": canciones,
        "historial": historial,
        "albumes": albumes,
        "reproduccion_actual": reproduccion_actual,
        "artistas_mes": artistas_mes,
    }


def save_snapshot(payload: dict[str, Any], path: Path | None = None) -> Path:
    """Escribe el snapshot en disco (usado por el script de GitHub Actions)."""
    destino = path or cache_path()
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    logger.info("Snapshot guardado en %s", destino)
    return destino


def _load_from_file(path: Path) -> SnapshotTuple | None:
    if not path.is_file():
        return None
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(payload, dict):
            logger.error("Caché local inválida: se esperaba un objeto JSON")
            return None
        if not payload.get("perfil"):
            logger.warning("Caché local sin perfil")
            return None
        logger.info(
            "Datos cargados desde caché local (%s, fetched_at=%s)",
            path,
            payload.get("fetched_at"),
        )
        return snapshot_from_payload(payload)
    except (OSError, json.JSONDecodeError, TypeError) as exc:
        logger.error("No se pudo leer la caché local: %s", exc)
        return None


def _load_from_url(url: str) -> SnapshotTuple | None:
    if not url:
        return None
    try:
        # Cache-bust: raw.githubusercontent.com puede cachear agresivamente.
        bust = datetime.now(timezone.utc).strftime("%Y%m%d%H%M")
        separator = "&" if "?" in url else "?"
        response = requests.get(
            f"{url}{separator}_={bust}",
            timeout=20,
            headers={"Cache-Control": "no-cache", "Pragma": "no-cache"},
        )
        response.raise_for_status()
        payload = response.json()
        if not isinstance(payload, dict) or not payload.get("perfil"):
            logger.warning("Snapshot remoto sin perfil útil")
            return None
        logger.info(
            "Datos cargados desde caché remota (fetched_at=%s)",
            payload.get("fetched_at"),
        )
        return snapshot_from_payload(payload)
    except requests.RequestException as exc:
        logger.warning("No se pudo obtener la caché remota: %s", exc)
    except (ValueError, TypeError) as exc:
        logger.warning("Snapshot remoto inválido: %s", exc)
    return None


def load_snapshot() -> SnapshotTuple | None:
    """Carga el snapshot: primero remoto, luego archivo local.

    Returns:
        Tupla de datos o ``None`` si no hay caché usable.
    """
    remoto = _load_from_url(cache_url())
    if remoto is not None:
        return remoto

    local = _load_from_file(cache_path())
    if local is not None:
        return local

    logger.error("No hay snapshot de Spotify disponible (remoto ni local)")
    return None
