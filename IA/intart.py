import os
import platform
import google.generativeai as genai
from voz import create_window
import subprocess
import webbrowser
from process import verifica_exe, verifica_palavra_meio, abrir_exe, fim, abrir, infdata, infhora, time


def ia(ordem):
  # Chave da API fornecida
  api_key = "AIzaSyAc51fvkTYpOcLsrLigxXOwuEEeEiGmnwQ"

  # Detecta o sistema operacional atual
  current_os = platform.system()

  # Seleciona o comando adequado conforme o SO
  if current_os == "Windows":
    # No Windows, usamos o comando "set"
    command = f"set GEMINI_API_KEY={api_key}"
  elif current_os in ["Linux", "Darwin"]:
    # Em sistemas Unix-like (Linux/MacOS), usamos o comando "export"
    command = f"export GEMINI_API_KEY={api_key}"
  else:
    command = None

  if command:
    os.system(command)
  else:
    print(f"Sistema operacional '{current_os}' não suportado.")

  genai.configure(api_key=os.environ["GEMINI_API_KEY"])

  # Create the model
  generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 256,
    "response_mime_type": "text/plain",
  }

  model = genai.GenerativeModel(
    model_name="gemini-2.0-flash-exp",
    generation_config=generation_config,
  )

  chat_session = model.start_chat(
    history=[
    ]
  )

  response = chat_session.send_message("responda apenas em portugês brasil, sem emojis e sem caracteres especiais, de forma objetiva e FINJA SER A FRIDAY DO TONY STARK..."+ ordem)
  return response.text
