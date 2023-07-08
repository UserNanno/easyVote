import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import mysql.connector
from Quicksort import quicksort
from Burbuja import burbuja


class GraficoGenero:
    def __init__(self):
        
        self.candidatosM = []
        self.votosM = []
        self.candidatosF = []
        self.votosF = []
        
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="easyvote"
        )

        # Crear un cursor para ejecutar consultas SQL
        cursor = conexion.cursor()

        # Realizar la consulta SQL
        consultaM = """
        SELECT voto, COUNT(*) AS cantidad_votos
        FROM votantes
        WHERE genero='M'
        GROUP BY voto
        """


        cursor.execute(consultaM)
        resultadosM = cursor.fetchall()
 
 
        # Realizar la consulta SQL
        consultaF = """
        SELECT voto, COUNT(*) AS cantidad_votos
        FROM votantes
        WHERE genero='F'
        GROUP BY voto
        """


        cursor.execute(consultaF)
        resultadosF = cursor.fetchall()       
        
        
        
        cursor.close()
        conexion.close()
        
        for candidato, votos in resultadosM:
            self.candidatosM.append(candidato)
            self.votosM.append(votos)
        
        for candidato, votos in resultadosF:
            self.candidatosF.append(candidato)
            self.votosF.append(votos)
        
        self.candidatosM, self.votosM = burbuja(self.candidatosM, self.votosM)
        self.candidatosF, self.votosF = burbuja(self.candidatosF, self.votosF)
        

        
        #--------------- 
            
    def crear_grafico(self):
        # Crear ventana
        ventana = tk.Tk()
        ventana.title("Gráfico de Barras Genero")

        # Crear figura de Matplotlib
        fig = Figure(figsize=(10, 4), dpi=100)

        # Crear eje de barras para el primer gráfico
        ax1 = fig.add_subplot(121)
        ax1.bar(self.candidatosM, self.votosM)
        for i, v in enumerate(self.votosM):
            ax1.text(i, v, str(v), ha='center', va='bottom')
        ax1.set_title("Masculino")

        # Crear eje de barras para el segundo gráfico
        ax2 = fig.add_subplot(122)
        ax2.bar(self.candidatosF, self.votosF, color='red')
        
        for i, v in enumerate(self.votosF):
            ax2.text(i, v, str(v), ha='center', va='bottom')
        ax2.set_title("Femenino")

        # Crear lienzo para el gráfico de Matplotlib
        lienzo = FigureCanvasTkAgg(fig, master=ventana)
        lienzo.draw()
        lienzo.get_tk_widget().pack()

        ventana.mainloop()




