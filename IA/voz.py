import pyttsx3
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from threading import Thread
import queue

def sintetizar_voz(texto, q):
    """Realiza a síntese de voz e comunica o término via fila."""
    engine = pyttsx3.init()
    engine.setProperty('rate', 200)  # Velocidade da fala
    engine.setProperty('volume', 1.0)  # Volume (valor entre 0.0 e 1.0)
    
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # Escolhe uma voz disponível
    
    engine.say(texto)
    engine.runAndWait()
    
    # Após a síntese, envia um sinal para a thread principal encerrar a janela
    q.put("done")

def check_queue(root, q):
    """Verifica a fila periodicamente e fecha a janela se a síntese terminou."""
    try:
        if q.get_nowait() == "done":
            root.destroy()
    except queue.Empty:
        root.after(100, check_queue, root, q)

def create_window(texto):
    """Cria a janela Tkinter e inicia a síntese de voz em um thread separado."""
    root = tk.Tk()
    root.title("Terminal de Texto")
    root.overrideredirect(True)
    root.configure(bg='#d3d3d3')
    root.attributes('-alpha', 0.5)
    root.attributes('-topmost', True)

    frame = tk.Frame(root, bg='black')
    frame.pack(fill="both", expand=True)
    
    label = tk.Label(frame, text=texto, bg='black', fg='white', wraplength=280)
    label.pack()
    
    root.update_idletasks()
    
    width = 300
    height = root.winfo_height()
    root.geometry(f"{width}x{height}+0+0")
    
    scrolled_text = ScrolledText(root, wrap=tk.WORD, font=("Helvetica", 8), bg='black', fg='white')
    scrolled_text.pack(expand=True, fill='both')
    scrolled_text.insert(tk.END, texto)
    scrolled_text.configure(state='disabled')
    
    # Cria uma fila para comunicação entre a thread e a GUI
    q = queue.Queue()

    # Inicia a síntese de voz em um thread separado
    thread = Thread(target=sintetizar_voz, args=(texto, q), daemon=True)
    thread.start()
    
    # Agendar verificação da fila para fechar a janela na thread principal
    root.after(100, check_queue, root, q)

    root.mainloop()