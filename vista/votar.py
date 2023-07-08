import tkinter as tk
from tkinter import messagebox
from database import Database
from votante import Votante
from candidato import Candidato


class Votar:
    def __init__(self, dni):
        self.dni = dni
        self.candidatos = []  # Lista para almacenar los candidatos disponibles

        # Crear la ventana
        self.ventana = tk.Tk()

        # Configurar propiedades de la ventana
        self.ventana.title("EasyVote")
        self.ventana.geometry("400x600")  # Tamaño de la ventana en píxeles

        # Crear una instancia de la clase Database para manejar la conexión a la base de datos
        self.database = Database(
            host="localhost", user="root", password="", db="easyvote")
        self.database.connect()

        # Obtener los votantes desde la base de datos
        query = "SELECT id_candidato, nombre, apellido, partido_politico FROM candidatos"
        query_candidatos = self.database.fetch_candidatos(query)

       # Almacenar los candidatos en la lista
        self.candidatos = [(candidato.nombre, candidato.apellido,
                            candidato.partido_politico) for candidato in query_candidatos]

        # Cerrar la conexión a la base de datos
        self.database.close()

        # Agregar contenido a la ventana
        etiqueta = tk.Label(self.ventana, text="ELIGE UN CANDIDATO")
        etiqueta.pack(pady=10)

        # Crear un contenedor para los botones
        contenedor = tk.Frame(self.ventana)
        contenedor.pack(pady=10)

        # Crear los botones y etiquetas usando los candidatos cargados
        fila_actual = 0
        columna_actual = 0
        for i, candidato in enumerate(self.candidatos):
            etiqueta = tk.Label(contenedor, text=candidato)
            etiqueta.grid(row=fila_actual, column=columna_actual, pady=10)

            boton = tk.Button(contenedor, text="Votar", width=10, height=5,
                              command=lambda candidato=candidato: self.boton_click(candidato))
            boton.grid(row=fila_actual + 1, column=columna_actual, pady=10)

            columna_actual += 1
            if columna_actual >= 3:
                columna_actual = 0
                fila_actual += 2

    def boton_click(self, candidato):
        # Crear una nueva instancia de la clase Database para manejar la conexión a la base de datos
        database = Database(host="localhost", user="root",
                            password="", db="easyvote")
        database.connect()

        # Actualizar el voto del votante en la base de datos
        query = "UPDATE votantes SET voto = %s WHERE dni = %s"
        print(f"Ejecutando consulta: {query}")
        print(f"Voto: {candidato[0]}, DNI: {self.dni}")
        database.cursor.execute(query, (candidato[0], self.dni))
        database.conn.commit()

        # Cerrar la conexión a la base de datos
        database.close()

        messagebox.showinfo("Voto Registrado", f"Has votado por {candidato}.")

    def iniciar_ventana(self):
        # Ejecutar el bucle principal de la aplicación
        self.ventana.mainloop()
