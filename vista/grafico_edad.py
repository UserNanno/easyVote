import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from database import Database
from mergesort import merge_sort
from votante import Votante
import time 

class GraficoEdad:
    def __init__(self):
        self.database = Database("localhost", "root", "", "easyvote")
        self.root = tk.Tk()
        self.root.title("Estadísitca por Edad")

        self.label_min = tk.Label(self.root, text="Rango de edad mínimo:")
        self.label_min.pack()
        self.entry_min = tk.Entry(self.root)
        self.entry_min.pack()

        self.label_max = tk.Label(self.root, text="Rango de edad máximo:")
        self.label_max.pack()
        self.entry_max = tk.Entry(self.root)
        self.entry_max.pack()

        # Crear el botón "Cerrar"
        button_close = tk.Button(
            self.root, text="Cerrar", command=self.close_button_click_handler)
        button_close.pack()

        self.button = tk.Button(self.root, text="Filtrar",
                                command=self.analyze_voters)
        self.button.pack()

        button_new_filter = tk.Button(
            self.root, text="Nuevo Filtro", command=self.restart_program)
        button_new_filter.pack()

        self.canvas = tk.Canvas(self.root, width=400, height=300)
        self.canvas.pack()

        self.total_votes_label = tk.Label(self.root, text="")
        self.total_votes_label.pack()

    def run(self):
        self.root.mainloop()
        

    def close_button_click_handler(self):
        self.root.destroy()

    def analyze_voters(self):
        rango_edad_min = self.entry_min.get()
        rango_edad_max = self.entry_max.get()

        if not rango_edad_min.strip() or not rango_edad_max.strip():
            messagebox.showinfo("Información", "Ingrese valores para el rango de edad.")
            return

        if not rango_edad_min.isdigit() or not rango_edad_max.isdigit():
            messagebox.showinfo("Información", "Ingrese valores numéricos para el rango de edad.")
            return

        rango_edad_min = int(rango_edad_min)
        rango_edad_max = int(rango_edad_max)

        self.database.connect()

        query = f"SELECT dni, nombre, apellido, departamento, genero, edad, voto FROM votantes WHERE edad >= {rango_edad_min} AND edad <= {rango_edad_max}"
        votantes = self.database.fetch_votantes(query)

        if votantes:
            votos_por_candidato = {}
            for votante in votantes:
                candidato = votante.voto
                if candidato in votos_por_candidato:
                    votos_por_candidato[candidato] += 1
                else:
                    votos_por_candidato[candidato] = 1

            start_time = time.perf_counter()  # Guardar el tiempo de inicio
            resultados_ordenados = merge_sort(list(votos_por_candidato.items()))
            end_time = time.perf_counter()  # Guardar el tiempo de finalización
            tiempo_transcurrido = end_time - start_time  # Calcular la diferencia de tiempo
            print("Tiempo transcurrido (mergesort):", tiempo_transcurrido)
            
            candidatos = [candidato[0] for candidato in resultados_ordenados]
            votos = [candidato[1] for candidato in resultados_ordenados]
            total_votos = sum(votos)

            self.plot_graph(candidatos, votos)
            self.total_votes_label.config(
                text=f"Total de votos contabilizados: {total_votos}")

        else:
            messagebox.showinfo(
                "Información", "No se encontraron votos para el rango de edad especificado.")
            self.reset_graph()  # Borrar la gráfica actual

        self.database.close()

    def plot_graph(self, candidatos, votos):

        fig, ax = plt.subplots(figsize=(8, 6))
        ax.barh(candidatos, votos)
        ax.set_xlabel("Cantidad de Votos")
        ax.set_ylabel("Candidatos")
        ax.set_title("Resultados de Votación")

        for i, v in enumerate(votos):
            ax.text(v + 3, i, str(v), color='blue', fontweight='bold')

        plt.tight_layout()

        canvas = FigureCanvasTkAgg(fig, master=self.canvas)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

    def restart_program(self):
        self.root.destroy()  # Cerrar la ventana actual
        new_analyzer = GraficoEdad()  # Crear una nueva instancia de GraficoEdad
        new_analyzer.run()  # Ejecutar el programa nuevamente


if __name__ == "__main__":
    host = 'localhost'
    user = 'root'
    password = ''
    database_name = 'easyvote'

    analyzer = GraficoEdad(host, user, password, database_name)
    analyzer.run()
