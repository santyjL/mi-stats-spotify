# my_stats_spotify

App Reflex con estadísticas personales de Spotify. Los datos **no** se
consultan a Spotify en cada visita: GitHub Actions refresca un snapshot JSON
cada ~3 minutos y la app solo lee esa caché.

## Cómo funciona

1. El workflow [`.github/workflows/refresh-spotify.yml`](.github/workflows/refresh-spotify.yml)
   llama a Spotify con tus secretos y publica `spotify_cache.json` en la rama
   `spotify-data` (sin redesplegar Railway).
2. El backend Reflex lee ese JSON desde
   `https://raw.githubusercontent.com/santyjL/mi-stats-spotify/spotify-data/spotify_cache.json`
   (o desde `data/spotify_cache.json` en local).
3. Cada carga de página usa la caché → sin rate limit por navegación.

## Secretos de GitHub Actions

En el repo: **Settings → Secrets and variables → Actions**, crea:

| Secret | Descripción |
|--------|-------------|
| `SPOTIFY_CLIENT_ID` | Client ID de la app en Spotify Developer |
| `SPOTIFY_CLIENT_SECRET` | Client Secret |
| `SPOTIFY_REFRESH_TOKEN` | Refresh token con los scopes de la app |

Luego: **Actions → Refresh Spotify data → Run workflow** (primera vez).

## Desarrollo

```bash
source .venv/bin/activate
# Generar caché local (opcional; requiere .env con las mismas variables)
python scripts/refresh_spotify_data.py
reflex run
```

## Build

```bash
bash build.sh
```

## Variables opcionales (Railway / local)

| Variable | Uso |
|----------|-----|
| `SPOTIFY_CACHE_URL` | URL alternativa del JSON (por defecto la rama `spotify-data`) |
| `SPOTIFY_CACHE_PATH` | Ruta local del snapshot |

En producción **ya no hace falta** tener las credenciales de Spotify en Railway:
solo Actions las necesita.
