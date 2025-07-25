
🔧 Demucs Render Setup – LucianoAI

Este proyecto separa automáticamente stems de un archivo .wav usando Demucs (modelo de 6 stems).
Salidas: WAV y MP3.
Modelo: htdemucs_6s

Estructura esperada:
- /audio/test.wav → tu canción original
- /separados/ → se crean los stems (vocals, drums, bass, other, guitar, piano)

👉 Build Command en Render:
pip install -r requirements.txt

👉 Start Command:
python main.py

⚠️ Requiere instancia Standard o superior en Render.
