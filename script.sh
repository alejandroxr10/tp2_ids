#!/bin/bash
#al ejecutar este script se inicia el servidor flask
RUTA_PROYECTO="$(pwd)/TP2-IDS"

mkdir -p "$RUTA_PROYECTO"

cd "$RUTA_PROYECTO"

mkdir -p static/css
mkdir -p static/images
mkdir -p templates

source .venv/bin/activate
python3 -m venv .venv
pip install flask flask-mail
touch app.py
pip freeze > requirements.txt

echo "Proyecto Flask creado en $RUTA_PROYECTO"
