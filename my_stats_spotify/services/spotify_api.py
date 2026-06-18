"""Cliente para consultar estadísticas personales de Spotify.

Este módulo gestiona la autenticación con refresh token, expone una clase
``SpotifyAPI`` con métodos para cada endpoint relevante y ofrece funciones
de alto nivel para recuperar e imprimir los datos en consola.

Variables de entorno requeridas (``.env``):

- ``SPOTIFY_CLIENT_ID``
- ``SPOTIFY_CLIENT_SECRET``
- ``SPOTIFY_REFRESH_TOKEN``

Scopes recomendados al generar el refresh token:

- ``user-read-private`` — país, plan y preferencias de contenido explícito
- ``user-read-email`` — correo electrónico
- ``user-top-read`` — top artistas y canciones
- ``user-read-recently-played`` — historial reciente
"""

import logging
import os

import requests
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger(__name__)

CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
REFRESH_TOKEN = os.getenv("SPOTIFY_REFRESH_TOKEN")

_PLANES: dict[str, str] = {
    "premium": "Premium",
    "free": "Gratuito",
    "open": "Open",
}


def refresh_access_token() -> str | None:
    """Obtiene un access token válido usando el refresh token almacenado.

    Realiza una petición POST al endpoint de cuentas de Spotify y devuelve
    el token de acceso de corta duración necesario para las llamadas a la API.

    Returns:
        Access token como cadena, o ``None`` si la petición falla o la
        respuesta no contiene el campo esperado.
    """
    try:
        response = requests.post(
            "https://accounts.spotify.com/api/token",
            data={
                "grant_type": "refresh_token",
                "refresh_token": REFRESH_TOKEN,
                "client_id": CLIENT_ID,
                "client_secret": CLIENT_SECRET,
            },
            timeout=30,
        )
        response.raise_for_status()
        return response.json()["access_token"]
    except requests.RequestException as exc:
        logger.error("Error obteniendo token de acceso: %s", exc)
    except (KeyError, ValueError) as exc:
        logger.error("Respuesta de token inválida: %s", exc)
    return None


class SpotifyAPI:
    """Cliente ligero para la Spotify Web API.

    Encapsula el token de acceso y centraliza las cabeceras de autorización
    y las peticiones HTTP a los distintos endpoints del usuario autenticado.

    Args:
        access_token: Token Bearer obtenido con :func:`refresh_access_token`.
    """

    def __init__(self, access_token: str):
        self.token = access_token

    @property
    def headers(self) -> dict[str, str]:
        """Cabeceras HTTP con el token Bearer para autenticación."""
        return {"Authorization": f"Bearer {self.token}"}

    def perfil(self) -> dict | None:
        """Obtiene el perfil completo del usuario autenticado.

        Endpoint: ``GET /v1/me``

        Campos habituales en la respuesta: ``display_name``, ``id``,
        ``country``, ``followers``,``images``, ``external_urls``,
        ``explicit_content``, ``uri``.

        Returns:
            Diccionario con los datos del perfil, o ``None`` si hay error.
        """
        try:
            response = requests.get(
                "https://api.spotify.com/v1/me",
                headers=self.headers,
                timeout=30,
            )
            response.raise_for_status()
            return response.json()
        except requests.RequestException as exc:
            logger.error("Error obteniendo perfil: %s", exc)
        except ValueError as exc:
            logger.error("Respuesta de perfil inválida: %s", exc)
        return None

    def top_artistas(
        self,
        limite: int = 20,
        rango: str = "long_term",
    ) -> dict | None:
        """Obtiene los artistas más escuchados del usuario.

        Endpoint: ``GET /v1/me/top/artists``

        Args:
            limite: Número de artistas a devolver (máximo 50).
            rango: Ventana temporal. Valores: ``short_term`` (~4 semanas),
                ``medium_term`` (~6 meses), ``long_term`` (varios años).

        Returns:
            Respuesta paginada de la API con clave ``items``, o ``None``.
        """
        try:
            response = requests.get(
                "https://api.spotify.com/v1/me/top/artists",
                headers=self.headers,
                params={"limit": limite, "time_range": rango},
                timeout=30,
            )
            response.raise_for_status()
            return response.json()
        except requests.RequestException as exc:
            logger.error("Error obteniendo top artistas: %s", exc)
        except ValueError as exc:
            logger.error("Respuesta de top artistas inválida: %s", exc)
        return None

    def top_canciones(
        self,
        limite: int = 20,
        rango: str = "long_term",
    ) -> dict | None:
        """Obtiene las canciones más escuchadas del usuario.

        Endpoint: ``GET /v1/me/top/tracks``

        Args:
            limite: Número de canciones a devolver (máximo 50).
            rango: Ventana temporal (``short_term``, ``medium_term``,
                ``long_term``).

        Returns:
            Respuesta paginada de la API con clave ``items``, o ``None``.
        """
        try:
            response = requests.get(
                "https://api.spotify.com/v1/me/top/tracks",
                headers=self.headers,
                params={"limit": limite, "time_range": rango},
                timeout=30,
            )
            response.raise_for_status()
            return response.json()
        except requests.RequestException as exc:
            logger.error("Error obteniendo top canciones: %s", exc)
        except ValueError as exc:
            logger.error("Respuesta de top canciones inválida: %s", exc)
        return None

    def historial(self, limite: int = 20) -> dict | None:
        """Obtiene el historial de reproducción reciente.

        Endpoint: ``GET /v1/me/player/recently-played``

        Args:
            limite: Número de pistas recientes (máximo 50).

        Returns:
            Respuesta con clave ``items`` (cada entrada incluye ``track``),
            o ``None`` si hay error.
        """
        try:
            response = requests.get(
                "https://api.spotify.com/v1/me/player/recently-played",
                headers=self.headers,
                params={"limit": limite},
                timeout=30,
            )
            response.raise_for_status()
            return response.json()
        except requests.RequestException as exc:
            logger.error("Error obteniendo historial: %s", exc)
        except ValueError as exc:
            logger.error("Respuesta de historial inválida: %s", exc)
        return None

    def top_albumes(
        self,
        limite: int = 10,
        rango: str = "long_term",
    ) -> list[dict[str, str | int]] | None:
        """Calcula los álbumes más escuchados a partir del top de canciones.

        Spotify no expone un endpoint de álbumes top; este método obtiene
        las 50 canciones más escuchadas y agrupa por álbum, asignando más
        peso a las canciones con mejor posición en el ranking.

        Args:
            limite: Cantidad de álbumes a devolver.
            rango: Ventana temporal para el cálculo.

        Returns:
            Lista de diccionarios con ``nombre``, ``artista`` y
            ``puntuacion``, ordenada de mayor a menor puntuación.
        """
        canciones = self.top_canciones(limite=50, rango=rango)
        if not canciones or not canciones.get("items"):
            logger.error("No se pudieron obtener canciones para calcular álbumes")
            return None

        conteo: dict[str, dict[str, str | int]] = {}
        total = len(canciones["items"])
        for posicion, track in enumerate(canciones["items"]):
            album = track.get("album", {})
            album_id = album.get("id")
            if not album_id:
                continue

            peso = total - posicion
            if album_id not in conteo:
                artista = track["artists"][0]["name"] if track.get("artists") else "Desconocido"
                conteo[album_id] = {
                    "nombre": album.get("name", "Desconocido"),
                    "artista": artista,
                    "puntuacion": 0,
                }
            conteo[album_id]["puntuacion"] = int(conteo[album_id]["puntuacion"]) + peso

        ordenados = sorted(
            conteo.values(),
            key=lambda album: album["puntuacion"],
            reverse=True,
        )
        return ordenados[:limite]


def _valor_perfil(perfil: dict, clave: str, por_defecto: str = "No disponible") -> str:
    """Extrae un campo del perfil como texto, con valor por defecto si falta."""
    valor = perfil.get(clave)
    if valor is None or valor == "":
        return por_defecto
    return str(valor)


def _mostrar_perfil(perfil: dict | None) -> None:
    """Imprime todos los campos disponibles del perfil de Spotify.

    Algunos campos (``email``, ``country``, ``product``, ``explicit_content``)
    solo aparecen si el refresh token incluye los scopes ``user-read-email``
    y ``user-read-private``.
    """
    print("\n===== PERFIL =====\n")

    if not perfil:
        print("No se pudo obtener el perfil")
        return

    print(f"Nombre: {_valor_perfil(perfil, 'display_name')}")
    print(f"ID: {_valor_perfil(perfil, 'id')}")
    print(f"Account ID: {_valor_perfil(perfil, 'account_id')}")
    print(f"Email: {_valor_perfil(perfil, 'email')}")
    print(f"País: {_valor_perfil(perfil, 'country')}")

    producto = perfil.get("product")
    if producto:
        print(f"Plan: {_PLANES.get(producto, producto)}")
    else:
        print("Plan: No disponible (requiere scope user-read-private)")

    seguidores = perfil.get("followers", {}).get("total")
    if seguidores is not None:
        print(f"Seguidores: {seguidores}")
    else:
        print("Seguidores: No disponible")

    url = perfil.get("external_urls", {}).get("spotify")
    print(f"Perfil en Spotify: {url or 'No disponible'}")

    imagenes = perfil.get("images") or []
    if imagenes:
        print(f"Imagen de perfil: {imagenes[0].get('url', 'No disponible')}")
    else:
        print("Imagen de perfil: No disponible")

    explicito = perfil.get("explicit_content")
    if explicito is not None:
        filtro = "activado" if explicito.get("filter_enabled") else "desactivado"
        bloqueado = "sí" if explicito.get("filter_locked") else "no"
        print(f"Filtro de contenido explícito: {filtro} (bloqueado: {bloqueado})")
    else:
        print("Contenido explícito: No disponible (requiere scope user-read-private)")

    print(f"URI: {_valor_perfil(perfil, 'uri')}")
    print(f"Tipo: {_valor_perfil(perfil, 'type')}")


def recuperar_datos(
    limite: int = 10,
    rango: str = "long_term",
) -> tuple[
    dict | None,
    dict | None,
    dict | None,
    dict | None,
    list[dict[str, str | int]] | None,
]:
    """Autentica y recupera en bloque todas las estadísticas del usuario.

    Args:
        limite: Cantidad de artistas y canciones top a solicitar.
        rango: Ventana temporal para rankings (``short_term``, ``medium_term``,
            ``long_term``).

    Returns:
        Tupla ``(perfil, artistas, canciones, historial, albumes)``.
        Cada elemento puede ser ``None`` si falla la autenticación o la
        petición correspondiente.
    """
    token = refresh_access_token()
    if not token:
        logger.error("No se pudo obtener el token de acceso")
        return None, None, None, None, None

    spotify = SpotifyAPI(token)
    perfil = spotify.perfil()
    artistas = spotify.top_artistas(limite=limite, rango=rango)
    canciones = spotify.top_canciones(limite=limite, rango=rango)
    historial = spotify.historial(limite=20)
    albumes = spotify.top_albumes(limite=10, rango=rango)

    return perfil, artistas, canciones, historial, albumes


def mostrar_datos(
    perfil: dict | None,
    artistas: dict | None,
    canciones: dict | None,
    historial: dict | None = None,
    albumes: list[dict[str, str | int]] | None = None,
) -> None:
    """Imprime en consola el perfil y todas las estadísticas recuperadas.

    Args:
        perfil: Datos del usuario (``GET /v1/me``).
        artistas: Top artistas (``GET /v1/me/top/artists``).
        canciones: Top canciones (``GET /v1/me/top/tracks``).
        historial: Reproducciones recientes.
        albumes: Álbumes calculados por :meth:`SpotifyAPI.top_albumes`.
    """
    _mostrar_perfil(perfil)

    print("\n===== TOP ARTISTAS =====\n")

    if artistas and artistas.get("items"):
        for artista in artistas["items"]:
            print(artista["name"])
    else:
        print("No se pudieron obtener los artistas")

    print("\n===== TOP CANCIONES =====\n")

    if canciones and canciones.get("items"):
        for track in canciones["items"]:
            artista = track["artists"][0]["name"] if track.get("artists") else "Desconocido"
            print(f"{track['name']} - {artista}")
    else:
        print("No se pudieron obtener las canciones")

    print("\n===== HISTORIAL (ÚLTIMAS 20) =====\n")

    if historial and historial.get("items"):
        for entrada in historial["items"]:
            track = entrada.get("track", {})
            artista = track["artists"][0]["name"] if track.get("artists") else "Desconocido"
            print(f"{track.get('name', 'Desconocido')} - {artista}")
    else:
        print("No se pudo obtener el historial")

    print("\n===== TOP ÁLBUMES (TOP 10) =====\n")

    if albumes:
        for album in albumes:
            print(f"{album['nombre']} - {album['artista']} ({album['puntuacion']})")
    else:
        print("No se pudieron calcular los álbumes")


if __name__ == "__main__":
    datos = recuperar_datos()
    mostrar_datos(*datos)
