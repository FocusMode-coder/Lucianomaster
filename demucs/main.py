
import os
import subprocess

INPUT_FILE = "audio/test.wav"
OUTPUT_DIR = "separados"
MODEL_NAME = "htdemucs_6s"

command = f"python3 -m demucs --mp3 -n {MODEL_NAME} {INPUT_FILE} -o {OUTPUT_DIR}"

print(f"🎧 Separando {INPUT_FILE} usando modelo {MODEL_NAME}...")
subprocess.run(command, shell=True)
print(f"✅ Exportación completa. Revisa la carpeta: {OUTPUT_DIR}")
