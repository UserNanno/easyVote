import tkinter as tk
from tkinter import messagebox
from tkinter import font
import mysql.connector
from vista.votar import Votar
from busqueda_binaria import busqueda_binaria
import time

class Login:
    def __init__(self):
        # Crear la ventana
        self.ventana = tk.Tk()

        # Configurar propiedades de la ventana
        self.ventana.title("Inicio de sesión")
        self.ventana.geometry("300x200")  # Tamaño de la ventana en píxeles

        # Etiqueta y campo de entrada para el DNI
        self.label_easyvote= tk.Label(self.ventana, text="EasyVote")
        # Configurar opciones de formato
        fuente = font.Font(weight="bold", size=16)
        self.label_easyvote.configure(font=fuente)
        self.label_easyvote.pack(pady=15)
        
        # Etiqueta y campo de entrada para el DNI
        self.label_dni = tk.Label(self.ventana, text="Ingrese su DNI:")
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
        
        start_time = time.perf_counter()  # Guardar el tiempo de inicio
        resultado = busqueda_binaria(columna, dni)  # Llamada a la función de búsqueda binaria
        end_time = time.perf_counter()  # Guardar el tiempo de finalización
        tiempo_transcurrido = end_time - start_time  # Calcular la diferencia de tiempo
        print("Tiempo transcurrido:", tiempo_transcurrido)
        
        
        if resultado:
            messagebox.showinfo("Bienvenido", "Inicio de sesión exitoso")
            self.ventana.destroy()
            votar = Votar(dni)
            votar.iniciar_ventana()

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
