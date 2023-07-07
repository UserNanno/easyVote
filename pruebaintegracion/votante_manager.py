# UTILIZACION DE LA ESTRUCTURA TABLAHASH
# UTILIZACION DEL ALGORITMO DE BUSQUEDA HASHMAP EN validar_voto(dni) => Verifica si el votante ha realizado su voto o no en la tabla hash
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tablahash import TablaHash
from database_manager import DatabaseManager


class VotanteManager:
    def __init__(self):
        self.tabla_hash = None
        self.db_manager = DatabaseManager()
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
                                command=self.iniciar_sesion(78801600))
        self.button.pack()

        self.canvas = tk.Canvas(self.root, width=400, height=300)
        self.canvas.pack()

        self.total_votes_label = tk.Label(self.root, text="")
        self.total_votes_label.pack()

    def close_button_click_handler(self):
        self.root.destroy()

    def llenar_tabla_hash(self):
        # Obtener el tamaño de la tabla votantes desde la base de datos
        query = "SELECT COUNT(*) FROM votantes"
        result = self.db_manager.execute_query(query)
        tamano_tabla = result[0][0]  # Obtener el valor del conteo

        # Crear una nueva instancia de TablaHash con el tamaño obtenido
        self.tabla_hash = TablaHash(tamano_tabla)
        self.tabla_hash.insertar_votantes_registrados()

    def iniciar_sesion(self, dni):
        # Busca el DNI en la base de datos
        query = "SELECT dni FROM votantes WHERE dni = %s"
        result = self.db_manager.execute_query(query, (dni,))
        if result:
            return True
        else:
            return False

    def validar_voto(self, dni):
        # Valida si el DNI tiene un voto registrado en la tabla hash
        voto = self.tabla_hash.buscar(dni)
        return voto is None

    def votar(self, dni, voto):
        # Agrega un DNI y su voto a la tabla hash
        self.tabla_hash.insertar(dni, voto)
        query = "UPDATE votantes SET voto = %s WHERE dni = %s"
        self.db_manager.execute_query(query, (voto, dni))
        self.db_manager.commit()
        print("Voto registrado correctamente.")
