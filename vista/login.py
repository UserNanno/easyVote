import tkinter as tk
from tkinter import messagebox
import mysql.connector
from vista.votar import Votar
from busqueda_binaria import busqueda_binaria

class Login:
    def __init__(self):
        # Crear la ventana
        self.ventana = tk.Tk()

        # Configurar propiedades de la ventana
        self.ventana.title("Inicio de sesión")
        self.ventana.geometry("300x200")  # Tamaño de la ventana en píxeles

        # Etiqueta y campo de entrada para el DNI
        self.label_dni = tk.Label(self.ventana, text="DNI:")
        self.label_dni.pack(pady=10)

        self.entry_dni = tk.Entry(self.ventana)
        self.entry_dni.pack(pady=10)

        # Botón de inicio de sesión
        self.boton_iniciar = tk.Button(self.ventana, text="Iniciar sesión", command=self.iniciar_sesion)
        self.boton_iniciar.pack(pady=10)

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

        # Consultar la columna deseada
        consulta = "SELECT dni FROM votantes"
        cursor.execute(consulta)
        columna = [fila[0] for fila in cursor]

        resultado = busqueda_binaria(columna, dni)  # Llamada a la función de búsqueda binaria

        if resultado:
            messagebox.showinfo("Bienvenido", "Inicio de sesión exitoso")
            self.ventana.destroy()
            votar = Votar(dni)

        else:
            messagebox.showinfo("Alerta", "El DNI no es válido")

        # Cerrar el cursor y la conexión
        cursor.close()
        conexion.close()

    # Ejecutar el bucle principal de la aplicación
    def iniciar(self):
        self.ventana.mainloop()

# Ejemplo de uso de la clase Login
if __name__ == "__main__":
    login = Login()
    login.iniciar()
