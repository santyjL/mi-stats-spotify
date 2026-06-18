import reflex as rx


class StateYoutube(rx.State):
    videos: list[str] = []
    channel_id: str = ""


class StateSpotify(rx.State):
    tracks: list[str] = []
    artist_id: str = ""


class StateGithub(rx.State):
    repos: list[str] = []
    username: str = ""


class StateWeather(rx.State):
    temperature: str = ""
    description: str = ""
    city: str = ""


class StateWhatsapp(rx.State):
    number: str = ""
    message: str = ""

    @rx.var
    def link(self) -> str:
        return f"https://wa.me/{self.number}?text={self.message}"
