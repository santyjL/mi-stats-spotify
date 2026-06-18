import reflex as rx

from .pages.home import home
from .pages.about import about
from .pages.services import services
from .pages.contact import contact
from .routers import ROUTES


app = rx.App()
app.add_page(home, route=ROUTES["home"])
app.add_page(about, route=ROUTES["about"])
app.add_page(services, route=ROUTES["services"])
app.add_page(contact, route=ROUTES["contact"])
