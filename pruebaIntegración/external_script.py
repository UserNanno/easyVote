import tkinter as tk
from voter_analyzer import VoterAnalyzerGUI

def button_click_handler():
    host = 'localhost'
    user = 'root'
    password = ''
    database_name = 'easyvote'

    analyzer = VoterAnalyzerGUI(host, user, password, database_name)
    analyzer.analyze_voters()

def close_button_click_handler():
    root.destroy()

# Crear y configurar la ventana principal
root = tk.Tk()

# Crear el botón "Ejecutar análisis"
button_run = tk.Button(root, text="Ejecutar análisis", command=button_click_handler)
button_run.pack()

# Crear el botón "Cerrar"
button_close = tk.Button(root, text="Cerrar", command=close_button_click_handler)
button_close.pack()

# Iniciar el bucle de eventos
root.mainloop()
