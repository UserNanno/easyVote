import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class GraficoRegion:
    def __init__(self):
        self.candidatos = []
        self.votosRegion = []  # DATOS DE PRUEBA, SE DEBE REEMPLAZAR
        
        self.region_disponible = ['Amazonas', 'Ancash', 'Apurímac', 'Arequipa', 'Ayacucho', 
                                  'Cajamarca', 'Callao', 'Cusco', 'Huancavelica', 'Huánuco', 
                                  'Ica', 'Junín', 'La Libertad', 'Lambayeque', 'Lima', 'Loreto', 
                                  'Madre de Dios', 'Moquegua', 'Pasco', 'Piura', 'Puno', 'San Martín', 
                                  'Tacna', 'Tumbes', 'Ucayali']


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
            self.candidatos = [] // deben ser traidos de la función
            self.votosRegion = [] 
            
            seleccion = combo.get()
            ax.clear()
            ax.bar(self.candidatos, self.votosRegion)
            lienzo.draw()

        # Crear combobox para seleccionar los datos
        combo = ttk.Combobox(ventana, values=self.region_disponible)
        combo.pack(pady=10)
        combo.current(0)  # Establecer el valor inicial del combobox
        combo.bind("<<ComboboxSelected>>", actualizar_grafico)

        # Configurar los datos iniciales en el eje de barras
        ax.bar(self.candidatos, self.votosRegion)

        # Crear lienzo para el gráfico de Matplotlib
        lienzo = FigureCanvasTkAgg(fig, master=ventana)
        lienzo.draw()
        lienzo.get_tk_widget().pack()

        ventana.mainloop()


if __name__ == '__main__':
    grafico = GraficoRegion()
    grafico.crear_grafico()
