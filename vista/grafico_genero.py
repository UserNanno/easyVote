import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


class GraficoGenero:
    def __init__(self):
        self.candidatos = ['A','B','C','D','E','F','G','H','I','J']
        self.votos = [150, 200, 300, 250, 180, 220, 280, 190, 210, 100]  # DATOS DE PRUEBA, SE DEBE REEMPLAZAR

    def crear_grafico(self):
        # Crear ventana
        ventana = tk.Tk()
        ventana.title("Gráfico de Barras Genero")

        # Crear figura de Matplotlib
        fig = Figure(figsize=(10, 4), dpi=100)

        # Crear eje de barras para el primer gráfico
        ax1 = fig.add_subplot(121)
        ax1.bar(self.candidatos, self.votos)
        ax1.set_title("Masculino")

        # Crear eje de barras para el segundo gráfico
        ax2 = fig.add_subplot(122)
        ax2.bar(self.candidatos, self.votos, color='red')
        ax2.set_title("Femenino")

        # Crear lienzo para el gráfico de Matplotlib
        lienzo = FigureCanvasTkAgg(fig, master=ventana)
        lienzo.draw()
        lienzo.get_tk_widget().pack()

        ventana.mainloop()




