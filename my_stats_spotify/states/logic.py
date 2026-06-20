import asyncio
from typing import TypedDict

import reflex as rx

from ..services.spotify_api import (
    _PLANES,
    _valor_perfil,
    recuperar_datos,
)


class ArtistaItem(TypedDict):
    name: str
    image_url: str


class HistorialItem(TypedDict):
    name: str
    album_name:str
    artist: str
    image_url: str


class AlbumItem(TypedDict):
    nombre: str
    artista: str
    image_url: str
    spotify_url: str


class CancionTopItem(TypedDict):
    num: int
    nombre: str
    artista: str
    album: str
    image_url: str


class ReproduccionActualItem(TypedDict):
    nombre: str
    artista: str
    album: str
    image_url: str
    spotify_url: str
    is_playing: bool


class StateSpotify(rx.State):
    """Estado de la app con datos de la Spotify Web API."""

    loading: bool = False
    error: str = ""
    limite: int = 30
    rango: str = "long_term"

    perfil: dict = {}
    artistas: dict = {}
    canciones: dict = {}
    historial: dict = {}
    albumes: list[dict] = []
    reproduccion_actual: dict = {}
    artistas_mes: dict = {}

    @rx.var
    def imagen_perfil(self) -> str:
        imagenes = self.perfil.get("images") or []
        if imagenes:
            return imagenes[0].get("url", "")
        return ""

    @rx.var
    def display_name(self) -> str:
        return _valor_perfil(self.perfil, "display_name")

    @rx.var
    def plan(self) -> str:
        producto = self.perfil.get("product")
        if producto:
            return _PLANES.get(producto, str(producto))
        return "No disponible"

    @rx.var
    def user_id(self) -> str:
        return _valor_perfil(self.perfil, "id")

    @rx.var
    def pais(self) -> str:
        return _valor_perfil(self.perfil, "country")

    @rx.var
    def hay_reproduccion(self) -> bool:
        return bool(self.reproduccion_actual.get("item"))

    @rx.var
    def reproduccion_actual_item(self) -> ReproduccionActualItem:
        track = self.reproduccion_actual.get("item") or {}
        artista = (
            track["artists"][0]["name"]
            if track.get("artists")
            else "Desconocido"
        )
        album = track.get("album") or {}
        imagenes = album.get("images") or []
        imagen_url = imagenes[0].get("url", "") if imagenes else ""
        spotify_url = track.get("external_urls", {}).get("spotify", "")
        return {
            "nombre": track.get("name", "Desconocido"),
            "artista": artista,
            "album": album.get("name", "Desconocido"),
            "image_url": imagen_url,
            "spotify_url": spotify_url,
            "is_playing": bool(self.reproduccion_actual.get("is_playing")),
        }

    @rx.var
    def artistas_mes_items(self) -> list[ArtistaItem]:
        items = self.artistas_mes.get("items") or []
        resultado: list[ArtistaItem] = []
        for artista in items:
            imagenes = artista.get("images") or []
            url = imagenes[0].get("url", "") if imagenes else ""
            resultado.append(
                {
                    "name": artista.get("name", "Desconocido"),
                    "image_url": url,
                }
            )
        return resultado

    @rx.var
    def top_artistas_nombres(self) -> list[str]:
        items = self.artistas.get("items") or []
        return [artista.get("name", "Desconocido") for artista in items]

    @rx.var
    def artistas_items(self) -> list[ArtistaItem]:
        items = self.artistas.get("items") or []
        resultado: list[ArtistaItem] = []
        for artista in items:
            imagenes = artista.get("images") or []
            url = imagenes[0].get("url", "") if imagenes else ""
            resultado.append(
                {
                    "name": artista.get("name", "Desconocido"),
                    "image_url": url,
                }
            )
        return resultado

    @rx.var
    def historial_items(self) -> list[HistorialItem]:
        items = self.historial.get("items") or []
        resultado: list[HistorialItem] = []
        for entrada in items:
            track = entrada.get("track", {})
            artista = (
                track["artists"][0]["name"]
                if track.get("artists")
                else "Desconocido"
            )
            album = track.get("album") or {}
            nombre_album= album.get("name")or []
            imagenes = album.get("images") or []
            url = imagenes[0].get("url", "") if imagenes else ""
            resultado.append(
                {
                    "name": track.get("name", "Desconocido"),
                    "album_name": nombre_album,
                    "artist": artista,
                    "image_url": url,
                }
            )
        return resultado

    @rx.var
    def top_canciones_texto(self) -> list[str]:
        items = self.canciones.get("items") or []
        resultado: list[str] = []
        for track in items:
            artista = (
                track["artists"][0]["name"]
                if track.get("artists")
                else "Desconocido"
            )
            resultado.append(f"{track.get('name', 'Desconocido')} - {artista}")
        return resultado

    @rx.var
    def historial_texto(self) -> list[str]:
        items = self.historial.get("items") or []
        resultado: list[str] = []
        for entrada in items:
            track = entrada.get("track", {})
            artista = (
                track["artists"][0]["name"]
                if track.get("artists")
                else "Desconocido"
            )
            resultado.append(f"{track.get('name', 'Desconocido')} - {artista}")
        return resultado

    @rx.var
    def albumes_texto(self) -> list[str]:
        return [
            f"{album.get('nombre', 'Desconocido')} - {album.get('artista', 'Desconocido')}"
            for album in self.albumes
        ]

    @rx.var
    def albumes_items(self) -> list[AlbumItem]:
        resultado: list[AlbumItem] = []
        for album in self.albumes:
            resultado.append(
                {
                    "nombre": album.get("nombre", "Desconocido"),
                    "artista": album.get("artista", "Desconocido"),
                    "image_url": album.get("image_url", ""),
                    "spotify_url": album.get("spotify_url", ""),
                }
            )
        return resultado

    @rx.var
    def top_canciones_items(self) -> list[CancionTopItem]:
        items = self.canciones.get("items") or []

        resultado: list[CancionTopItem] = []

        for indice, track in enumerate(items, start=1):

            artista = (
                track["artists"][0]["name"]
                if track.get("artists")
                else "Desconocido"
            )

            album = track.get("album") or {}

            imagenes = album.get("images") or []

            url = (
                imagenes[0].get("url", "")
                if imagenes
                else ""
            )

            resultado.append(
                {
                    "num": indice,
                    "nombre": track.get(
                        "name",
                        "Desconocido",
                    ),
                    "artista": artista,
                    "album": album.get(
                        "name",
                        "Desconocido",
                    ),
                    "image_url": url,
                }
            )

        return resultado

    @rx.var
    def tiene_datos(self) -> bool:
        return bool(self.perfil)

    def _aplicar_datos(
        self,
        perfil: dict | None,
        artistas: dict | None,
        canciones: dict | None,
        historial: dict | None,
        albumes: list | None,
        reproduccion_actual: dict | None,
        artistas_mes: dict | None,
    ) -> None:
        if perfil is None:
            self.error = "No se pudo autenticar con Spotify"
            self.perfil = {}
            self.artistas = {}
            self.canciones = {}
            self.historial = {}
            self.albumes = []
            self.reproduccion_actual = {}
            self.artistas_mes = {}
            return

        self.perfil = perfil
        self.artistas = artistas or {}
        self.canciones = canciones or {}
        self.historial = historial or {}
        self.albumes = albumes or []
        self.reproduccion_actual = reproduccion_actual or {}
        self.artistas_mes = artistas_mes or {}
        self.error = ""

    @rx.event(background=True)
    async def cargar_datos(self):
        async with self:
            self.loading = True
            self.error = ""
            limite = self.limite
            rango = self.rango

        (
            perfil,
            artistas,
            canciones,
            historial,
            albumes,
            reproduccion_actual,
            artistas_mes,
        ) = await asyncio.to_thread(
            recuperar_datos,
            limite,
            rango,
        )

        async with self:
            self._aplicar_datos(
                perfil,
                artistas,
                canciones,
                historial,
                albumes,
                reproduccion_actual,
                artistas_mes,
            )
            self.loading = False

    @rx.event
    def cambiar_rango(self, rango: str):
        self.rango = rango
        return StateSpotify.cargar_datos
