import tkinter as tk
import subprocess
from login import Login



class App:
    def __init__(self):
        # Crear la ventana
        self.ventana = tk.Tk()

        # Agregar contenido a la ventana
        self.etiqueta = tk.Label(self.ventana, text="SISTEMA DE VOTACIÓN ELECTRÓNICO")
        self.etiqueta.pack(pady=30)

        # Configurar propiedades de la ventana
        self.ventana.title("EasyVote")
        self.ventana.geometry("500x400")  # Tamaño de la ventana en píxeles

        # Crear un contenedor para los botones
        self.contenedor = tk.Frame(self.ventana)
        self.contenedor.pack(pady=50)

        # Crear los botones dentro del contenedor
        self.boton1 = tk.Button(self.contenedor, text="Votar", width=20, height=10, command=self.boton1_click)
        self.boton2 = tk.Button(self.contenedor, text="Estadistica", width=20, height=10, command=self.boton2_click)

        # Ubicar los botones dentro del contenedor
        self.boton1.pack(side="left", padx=10)
        self.boton2.pack(side="left", padx=10)

    # Funciones para los botones
    def boton1_click(self):
        login_app = Login()
        

    def boton2_click(self):
        print("Botón 2 fue clickeado")

    # Ejecutar el bucle principal de la aplicación
    def iniciar(self):
        self.ventana.mainloop()