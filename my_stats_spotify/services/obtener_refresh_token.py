import base64
import requests
from urllib.parse import urlencode

CLIENT_ID = "MI_ID"
CLIENT_SECRET = "MI_SECRET_TOKEN"

REDIRECT_URI = "http://127.0.0.1:3000"

SCOPES = [
    "user-read-private",
    "user-read-email",
    "user-top-read",
    "user-read-recently-played",
    "user-read-currently-playing",
]

# URL de autorización
params = {
    "client_id": CLIENT_ID,
    "response_type": "code",
    "redirect_uri": REDIRECT_URI,
    "scope": " ".join(SCOPES),
}

auth_url = (
    "https://accounts.spotify.com/authorize?"
    + urlencode(params)
)

print("\nAbre esta URL en tu navegador:\n")
print(auth_url)

print(
    "\nDespués de autorizar, pega aquí la URL completa "
    "a la que Spotify te redirija:\n"
)

redirected_url = input("> ").strip()

# Extraer el code
code = redirected_url.split("code=")[1].split("&")[0]

# Intercambiar code por tokens
auth_header = base64.b64encode(
    f"{CLIENT_ID}:{CLIENT_SECRET}".encode()
).decode()

response = requests.post(
    "https://accounts.spotify.com/api/token",
    headers={
        "Authorization": f"Basic {auth_header}",
        "Content-Type": "application/x-www-form-urlencoded",
    },
    data={
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": REDIRECT_URI,
    },
)

data = response.json()

print("\n===== TOKENS =====\n")

print("ACCESS TOKEN:\n")
print(data.get("access_token"))

print("\nREFRESH TOKEN:\n")
print(data.get("refresh_token"))

print("\nSCOPES OTORGADOS:\n")
print(data.get("scope"))