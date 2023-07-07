import tkinter as tk
from tkinter import messagebox
import mysql.connector
from vista.votar import Votar


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
        print(type(dni))
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
        
        # Obtener todos los valores de la columna
        columna = [fila[0] for fila in cursor]
        
        
        
        #realiza la busqueda binaria(IMPORTANTE)<-------------------------------------------------------   BUSQUEDA BINARIA
        #ordenar lista
        columna = sorted(columna)
        
        inicio = 0
        fin = len(columna) - 1
        resultado=False
        
        print(dni)
        while inicio <= fin:
            medio = (inicio + fin) // 2
            valor_medio = columna[medio]

            if valor_medio == dni:
                # El DNI fue encontrado
                resultado= True
                break
            elif valor_medio < dni:
                inicio = medio + 1
            else:
                fin = medio - 1
        
        #----------------------------------------------------------------------------------------

        if resultado:
            messagebox.showinfo("Bienvenido","Inicio de sesión exitoso")
            
            self.ventana.destroy()
            votar=Votar(dni)
            
        else:
            messagebox.showinfo("Alerta", "El DNI no es válido")

        # Cerrar el cursor y la conexión
        cursor.close()
        conexion.close()

    # Ejecutar el bucle principal de la aplicación
    def iniciar(self):
        self.ventana.mainloop()
