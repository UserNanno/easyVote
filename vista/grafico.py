import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from Quicksort import quicksort
import mysql.connector
import time

class Grafico:
    def __init__(self):
        
        self.candidatos = []
        self.votos = []# DATOS DE PRUEBA, SE DEBE REEMPLAZAR
        
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="easyvote"
        )

        # Crear un cursor para ejecutar consultas SQL
        cursor = conexion.cursor()

        # Realizar la consulta SQL
        consulta = """
        SELECT voto, COUNT(*) AS cantidad_votos
        FROM votantes
        GROUP BY voto
        """

        cursor.execute(consulta)
        resultados = cursor.fetchall()
        
        cursor.close()
        conexion.close()
        
        for candidato, votos in resultados:
            self.candidatos.append(candidato)
            self.votos.append(votos)
            
        start_time = time.perf_counter()  # Guardar el tiempo de inicio
        self.candidatos, self.votos = quicksort(self.candidatos, self.votos)
        end_time = time.perf_counter()  # Guardar el tiempo de finalización
        tiempo_transcurrido = end_time - start_time  # Calcular la diferencia de tiempo
        print("Tiempo transcurrido (quicksort):", tiempo_transcurrido)
        
    def crear_grafico(self):
        # Crear ventana
        ventana = tk.Tk()
        ventana.title("Gráfico de Barras")
        ventana.geometry("800x600")

        # Crear figura de Matplotlib
        fig = Figure(figsize=(8, 6), dpi=100)

        # Crear eje de barras
        ax = fig.add_subplot(111)

        # Configurar los datos en el eje de barras
        ax.bar(self.candidatos, self.votos)

        for i, v in enumerate(self.votos):
            ax.text(i, v, str(v), ha='center', va='bottom')
            
        # Crear lienzo para el gráfico de Matplotlib
        lienzo = FigureCanvasTkAgg(fig, master=ventana)
        lienzo.draw()
        lienzo.get_tk_widget().pack()

        ventana.mainloop()

