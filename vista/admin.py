import tkinter as tk
from tkinter import font
from grafico import Grafico
from grafico_genero import GraficoGenero
from grafico_edad import GraficoEdad
from grafico_departamento import GraficoDepartamento
from login import Login



class Admin:
    def __init__(self):
        # Crear la ventana
        self.ventana = tk.Tk()

        # Agregar contenido a la ventana
        self.etiqueta = tk.Label(self.ventana, text="ESTADISTICAS DE LAS ELECCIONES")
        fuente = font.Font(weight="bold", size=16)
        self.etiqueta.configure(font=fuente)
        self.etiqueta.pack(pady=30)

        # Configurar propiedades de la ventana
        self.ventana.title("EasyVote")
        self.ventana.geometry("1000x400")  # Tamaño de la ventana en píxeles

        # Crear un contenedor para los botones
        self.contenedor = tk.Frame(self.ventana)
        self.contenedor.pack(pady=50)

        # Crear los botones dentro del contenedor
        self.boton1 = tk.Button(self.contenedor, text="Estadística\nGeneral\nQUICKSORT", width=20, height=10, command=self.boton1_click)
        self.boton2 = tk.Button(self.contenedor, text="Estadística por\nDepartamento\nHEAPSORT", width=20, height=10, command=self.boton2_click)
        self.boton3 = tk.Button(self.contenedor, text="Estadística por\nGénero\nBURBUJA", width=20, height=10, command=self.boton3_click)
        self.boton4 = tk.Button(self.contenedor, text="Estadística por\nEdad\nMERGESORT", width=20, height=10, command=self.boton4_click)
        self.boton_salir = tk.Button(self.contenedor, text="Salir", width=20, height=10, command=self.boton_salir_click)
        
        # Ubicar los botones dentro del contenedor
        self.boton1.pack(side="left", padx=10)
        self.boton2.pack(side="left", padx=10)
        self.boton3.pack(side="left", padx=10)
        self.boton4.pack(side="left", padx=10)
        self.boton_salir.pack(side="left", padx=10)

    # Funciones para los botones
    def boton1_click(self):
        grafico1=Grafico()
        grafico1.crear_grafico()

    def boton2_click(self):
        grafico2=GraficoDepartamento()
        grafico2.crear_grafico()
        
    def boton3_click(self):
        grafico3=GraficoGenero()
        grafico3.crear_grafico()

    def boton4_click(self):
        grafico4=GraficoEdad()
        grafico4.analyze_voters()

    def boton_salir_click(self):
        self.ventana.destroy()

    # Ejecutar el bucle principal de la aplicación
    def iniciar(self):
        self.ventana.mainloop()