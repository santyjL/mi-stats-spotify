#!/usr/bin/env python3
"""Consulta Spotify una vez y guarda el snapshot JSON para la app.

Pensado para ejecutarse en GitHub Actions (cron ~3 min). La app Reflex
solo lee este JSON; así no se satura la API en cada visita/navegación.
"""

from __future__ import annotations

import logging
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from my_stats_spotify.services.cache import (  # noqa: E402
    build_payload,
    cache_path,
    save_snapshot,
)
from my_stats_spotify.services.spotify_api import recuperar_datos  # noqa: E402

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger("refresh_spotify_data")

LIMITE = 30
RANGO = "medium_term"


def main() -> int:
    logger.info("Recuperando datos de Spotify (limite=%s, rango=%s)", LIMITE, RANGO)
    (
        perfil,
        artistas,
        canciones,
        historial,
        albumes,
        reproduccion_actual,
        artistas_mes,
    ) = recuperar_datos(limite=LIMITE, rango=RANGO)

    if perfil is None:
        logger.error("Fallo al autenticar o obtener el perfil; no se actualiza la caché")
        return 1

    payload = build_payload(
        perfil,
        artistas,
        canciones,
        historial,
        albumes,
        reproduccion_actual,
        artistas_mes,
        limite=LIMITE,
        rango=RANGO,
    )
    destino = save_snapshot(payload, path=cache_path())
    logger.info("OK — snapshot en %s (fetched_at=%s)", destino, payload["fetched_at"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
