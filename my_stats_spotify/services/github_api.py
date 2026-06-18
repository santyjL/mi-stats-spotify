import os

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("GITHUB_TOKEN")
BASE_URL = "https://api.github.com"
