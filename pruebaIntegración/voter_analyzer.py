import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from database import Database
from sort import merge_sort
from votante import Votante


class VoterAnalyzerGUI:
    def __init__(self, host, user, password, database_name):
        self.database = Database(host, user, password, database_name)
        self.root = tk.Tk()
        self.root.title("Voter Analyzer")

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

        self.canvas = tk.Canvas(self.root, width=400, height=300)
        self.canvas.pack()

        self.total_votes_label = tk.Label(self.root, text="")
        self.total_votes_label.pack()

    def run(self):
        self.root.mainloop()

    def close_button_click_handler(self):
        self.root.destroy()    

    def analyze_voters(self):
        rango_edad_min = int(self.entry_min.get())
        rango_edad_max = int(self.entry_max.get())
        if not rango_edad_min or not rango_edad_max:
            messagebox.showinfo(
                "Información", "Por favor, ingrese valores para el rango de edad.")
            return

        rango_edad_min = int(rango_edad_min)
        rango_edad_max = int(rango_edad_max)

        self.database.connect()

        query = f"SELECT dni, nombre, apellido, region, genero, edad, voto FROM votantes WHERE edad >= {rango_edad_min} AND edad <= {rango_edad_max}"
        votantes = self.database.fetch_votantes(query)

        if votantes:
            votos_por_candidato = {}
            for votante in votantes:
                candidato = votante.voto
                if candidato in votos_por_candidato:
                    votos_por_candidato[candidato] += 1
                else:
                    votos_por_candidato[candidato] = 1

            resultados_ordenados = merge_sort(
                list(votos_por_candidato.items()))
            candidatos = [candidato[0] for candidato in resultados_ordenados]
            votos = [candidato[1] for candidato in resultados_ordenados]
            total_votos = sum(votos)

            self.plot_graph(candidatos, votos)
            self.total_votes_label.config(
                text=f"Total de votos contabilizados: {total_votos}")

        else:
            messagebox.showinfo(
                "Información", "No se encontraron votos para el rango de edad especificado.")

        self.database.close()

    def plot_graph(self, candidatos, votos):
        self.canvas.delete("all")

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


if __name__ == "__main__":
    host = 'localhost'
    user = 'root'
    password = ''
    database_name = 'easyvote'

    analyzer = VoterAnalyzerGUI(host, user, password, database_name)
    analyzer.run()
