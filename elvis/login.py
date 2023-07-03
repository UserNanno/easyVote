import tkinter as tk
import mysql.connector
from votar import Votar


class Login:
    def __init__(self):
        # Crear la ventana
        self.login = tk.Tk()

        # Configurar propiedades de la ventana
        self.login.title("Inicio de sesión")
        self.login.geometry("300x200")  # Tamaño de la ventana en píxeles

        # Etiqueta y campo de entrada para el DNI
        self.label_dni = tk.Label(self.login, text="DNI:")
        self.label_dni.pack()

        self.entry_dni = tk.Entry(self.login)
        self.entry_dni.pack()

        # Botón de inicio de sesión
        self.boton_iniciar = tk.Button(self.login, text="Iniciar sesión", command=self.iniciar_sesion)
        self.boton_iniciar.pack()

    # Función para validar el inicio de sesión
    def iniciar_sesion(self):
        dni = self.entry_dni.get()

        # Establecer la conexión a la base de datos
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="easyvote"
        )

        # Crear un cursor para ejecutar consultas SQL
        cursor = conexion.cursor()

        # Consultar si el DNI existe en la base de datos//debe ser reemplazado con algoritmo de busqueda
        consulta = "SELECT * FROM votantes WHERE dni = %s"
        cursor.execute(consulta, (dni,))
        resultado = cursor.fetchone()

        if resultado:
            print("Inicio de sesión exitoso")
            self.login.destroy()
            votar=Votar()
            
        else:
            print("DNI no válido")

        # Cerrar el cursor y la conexión
        cursor.close()
        conexion.close()


