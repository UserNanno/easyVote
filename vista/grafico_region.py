import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class GraficoRegion:
    def __init__(self):
        self.candidatos = ['A','B','C','D','E','F','G','H','I','J']
        self.votosRegion1 = [150, 200, 300, 250, 180, 220, 280, 190, 210, 240]  # DATOS DE PRUEBA, SE DEBE REEMPLAZAR
        self.votosRegion2 = [200, 300, 250, 180, 220, 280, 190, 210, 240, 100]
        
    def crear_grafico(self):
        # Crear ventana
        ventana = tk.Tk()
        ventana.title("Gráfico de Barras")

        # Crear figura de Matplotlib
        fig = Figure(figsize=(6, 4), dpi=100)

        # Crear eje de barras
        ax = fig.add_subplot(111)

        # Obtener el valor seleccionado del combobox
        def actualizar_grafico(event):
            seleccion = combo.get()
            if seleccion == "Región 1":
                ax.clear()
                ax.bar(self.candidatos, self.votosRegion1)
            elif seleccion == "Región 2":
                ax.clear()
                ax.bar(self.candidatos, self.votosRegion2)
            lienzo.draw()

        # Crear combobox para seleccionar los datos
        combo = ttk.Combobox(ventana, values=["Región 1", "Región 2"])
        combo.pack(pady=10)
        combo.current(0)  # Establecer el valor inicial del combobox
        combo.bind("<<ComboboxSelected>>", actualizar_grafico)

        # Configurar los datos iniciales en el eje de barras
        ax.bar(self.candidatos, self.votosRegion1)

        # Crear lienzo para el gráfico de Matplotlib
        lienzo = FigureCanvasTkAgg(fig, master=ventana)
        lienzo.draw()
        lienzo.get_tk_widget().pack()

        ventana.mainloop()

if __name__ == '__main__':
    grafico = GraficoRegion()
    grafico.crear_grafico()
