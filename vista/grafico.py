import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class Grafico:
    def __init__(self, candidatos, votos):
        self.candidatos = candidatos
        self.votos = votos

    def crear_grafico(self):
        # Crear ventana
        ventana = tk.Tk()
        ventana.title("Gráfico de Barras")

        # Crear figura de Matplotlib
        fig = Figure(figsize=(6, 4), dpi=100)

        # Crear eje de barras
        ax = fig.add_subplot(111)

        # Configurar los datos en el eje de barras
        ax.bar(self.candidatos, self.votos)

        # Crear lienzo para el gráfico de Matplotlib
        lienzo = FigureCanvasTkAgg(fig, master=ventana)
        lienzo.draw()
        lienzo.get_tk_widget().pack()

        ventana.mainloop()

