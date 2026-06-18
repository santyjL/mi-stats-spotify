source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
rm -rf public
reflex init
REFLEX_API_URL=
reflex export --frontend-only
unzip frontend.zip -d public
rm -f frontend.zip
deactivate