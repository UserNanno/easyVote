import tkinter as tk
from grafico import Grafico
class Estadistica:
    def __init__(self):
        # Crear la ventana
        self.ventana = tk.Tk()

        # Agregar contenido a la ventana
        self.etiqueta = tk.Label(self.ventana, text="ESTADISTICAS")
        self.etiqueta.pack(pady=30)

        # Configurar propiedades de la ventana
        self.ventana.title("EasyVote")
        self.ventana.geometry("500x400")  # Tamaño de la ventana en píxeles

        # Crear un contenedor para los botones
        self.contenedor = tk.Frame(self.ventana)
        self.contenedor.pack(pady=50)

        # Crear los botones dentro del contenedor
        self.boton1 = tk.Button(self.contenedor, text="GENERAL", width=20, height=10, command=self.boton1_click)
        self.boton2 = tk.Button(self.contenedor, text="POR REGION", width=20, height=10, command=self.boton2_click)

        # Ubicar los botones dentro del contenedor
        self.boton1.pack(side="left", padx=10)
        self.boton2.pack(side="left", padx=10)

    # Funciones para los botones
    def boton1_click(self):
        candidatos = ['A','B','C','D','E','F','G','H','I','J']
        votos = [150, 200, 300, 250, 180, 220, 280, 190, 210, 240]# DATOS DE PRUEBA, SE DEBE REEMPLAZAR
        grafico=Grafico(candidatos,votos)
        grafico.crear_grafico()

    def boton2_click(self):
        print("Botón 2 fue clickeado")

    # Ejecutar el bucle principal de la aplicación
    def iniciar(self):
        self.ventana.mainloop()