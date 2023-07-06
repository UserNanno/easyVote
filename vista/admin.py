import tkinter as tk
from grafico import Grafico
from grafico_genero import GraficoGenero
from grafico_region import GraficoRegion
from login import Login



class Admin:
    def __init__(self):
        # Crear la ventana
        self.ventana = tk.Tk()

        # Agregar contenido a la ventana
        self.etiqueta = tk.Label(self.ventana, text="SISTEMA DE VOTACIÓN ELECTRÓNICO")
        self.etiqueta.pack(pady=30)

        # Configurar propiedades de la ventana
        self.ventana.title("EasyVote")
        self.ventana.geometry("600x400")  # Tamaño de la ventana en píxeles

        # Crear un contenedor para los botones
        self.contenedor = tk.Frame(self.ventana)
        self.contenedor.pack(pady=50)

        # Crear los botones dentro del contenedor
        self.boton1 = tk.Button(self.contenedor, text="Estadística\nGeneral", width=20, height=10, command=self.boton1_click)
        self.boton2 = tk.Button(self.contenedor, text="Estadística por\nRegión", width=20, height=10, command=self.boton2_click)
        self.boton3 = tk.Button(self.contenedor, text="Estadística por\nGénero", width=20, height=10, command=self.boton3_click)
        
        # Ubicar los botones dentro del contenedor
        self.boton1.pack(side="left", padx=10)
        self.boton2.pack(side="left", padx=10)
        self.boton3.pack(side="left", padx=10)

    # Funciones para los botones
    def boton1_click(self):
        
        grafico=Grafico()
        grafico.crear_grafico()

    def boton2_click(self):
        grafico2=GraficoRegion()
        grafico2.crear_grafico()
        
    def boton3_click(self):
        grafico3=GraficoGenero()
        grafico3.crear_grafico()

    # Ejecutar el bucle principal de la aplicación
    def iniciar(self):
        self.ventana.mainloop()