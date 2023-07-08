import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from Heapsort import heapsort
import time

class GraficoDepartamento:
    def __init__(self):
        self.candidatos = []
        self.votosDepartamento = []  # DATOS DE PRUEBA, SE DEBE REEMPLAZAR
        
        self.departamento_disponible = ['Amazonas', 'Ancash', 'Apurímac', 'Arequipa', 'Ayacucho', 
                                  'Cajamarca', 'Callao', 'Cusco', 'Huancavelica', 'Huánuco', 
                                  'Ica', 'Junín', 'La Libertad', 'Lambayeque', 'Lima', 'Loreto', 
                                  'Madre de Dios', 'Moquegua', 'Pasco', 'Piura', 'Puno', 'San Martín', 
                                  'Tacna', 'Tumbes', 'Ucayali']

    def crear_grafico(self):
        # Crear ventana
        ventana = tk.Tk()
        ventana.title("Gráfico de Barras")
        ventana.geometry("800x600")

        # Crear figura de Matplotlib
        fig = Figure(figsize=(8, 6), dpi=100)

        # Crear eje de barras
        ax = fig.add_subplot(111)

        # Obtener el valor seleccionado del combobox
        def actualizar_grafico(event):
            seleccion = combo.get()
            start_time = time.time()
            self.candidatos, self.votosDepartamento = heapsort(combo.get())
            end_time = time.time()  # Guardar el tiempo de finalización
            tiempo_transcurrido = end_time - start_time  # Calcular la diferencia de tiempo
            print("Tiempo transcurrido obtener:", tiempo_transcurrido)
            ax.clear()
            ax.bar(self.candidatos, self.votosDepartamento)
            
            for i, v in enumerate(self.votosDepartamento):
                ax.text(i, v, str(v), ha='center', va='bottom')
            
            lienzo.draw()

        # Crear combobox para seleccionar los datos
        combo = ttk.Combobox(ventana, values=self.departamento_disponible)
        combo.pack(pady=10)
        combo.current(0)  # Establecer el valor inicial del combobox
        combo.bind("<<ComboboxSelected>>", actualizar_grafico)

        # Configurar los datos iniciales en el eje de barras
        start_time = time.perf_counter()  # Guardar el tiempo de inicio
        self.candidatos, self.votosDepartamento = heapsort(combo.get())
        end_time = time.perf_counter()  # Guardar el tiempo de finalización
        tiempo_transcurrido = end_time - start_time  # Calcular la diferencia de tiempo
        print("Tiempo transcurrido visualizar (Heapsort):", tiempo_transcurrido)
        ax.bar(self.candidatos, self.votosDepartamento)

        # Crear lienzo para el gráfico de Matplotlib
        lienzo = FigureCanvasTkAgg(fig, master=ventana)
        lienzo.draw()
        lienzo.get_tk_widget().pack()

        # Mostrar el gráfico al iniciar
        actualizar_grafico(None)

        ventana.mainloop()


if __name__ == '__main__':
    grafico = GraficoDepartamento()
    grafico.crear_grafico()
