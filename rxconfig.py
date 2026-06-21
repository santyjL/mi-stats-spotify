import reflex as rx

config = rx.Config(
    app_name="my_stats_spotify",
    api_url="https://mi-stats-spotify-production.up.railway.app",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)