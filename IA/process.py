import os
import subprocess
import webbrowser
from voz import sintetizar_voz

def verifica_palavra_meio(texto, palavra_alvo):
    palavras = texto.split()
    tamanho = len(palavras)
    
    if tamanho == 0:
        return False
    
    meio = tamanho // 2  # Índice do meio
    
    if tamanho % 2 == 0:
        return palavras[meio - 1] == palavra_alvo or palavras[meio] == palavra_alvo
    else:
        return palavras[meio] == palavra_alvo

def verifica_exe(nome_exe):
    caminhos = [
        os.getenv("PROGRAMFILES"),
        os.getenv("PROGRAMFILES(X86)"),
        os.getenv("LOCALAPPDATA"),
        os.getenv("APPDATA"),
        os.getenv("USERPROFILE")
    ]
    
    for caminho in caminhos:
        if caminho:
            for root, _, files in os.walk(caminho):
                if nome_exe in files:
                    return os.path.join(root, nome_exe)
    return None

def abrir_exe(caminho_exe):
    try:
        subprocess.Popen(caminho_exe, shell=True)
        print(f"Executando {caminho_exe}")
    except Exception as e:
        print(f"Erro ao abrir {caminho_exe}: {e}")

fim=["desligar","break","off"]
abrir=["abrir", "abra","inicie", "iniciar","execute", "executar"]
