import tkinter as tk
from tkinter import messagebox
import mysql.connector

class Votar:
    def __init__(self,dni):
        
        # Crear la ventana
        
        self.ventana = tk.Tk()
        
        # Agregar contenido a la ventana
        etiqueta = tk.Label(self.ventana, text="ELIGE UN CANDIDATO")
        etiqueta.pack(pady=10)

        # Configurar propiedades de la ventana
        self.ventana.title("EasyVote")
        self.ventana.geometry("400x600")  # Tamaño de la ventana en píxeles

        # Funciones para los botones
        nuevo_voto =""
        def boton1_click():
            nuevo_voto = "candidato 1"
            cursor.execute(consulta, (nuevo_voto, dni))
            conexion.commit()
            cursor.close()
            conexion.close()
            
        def boton2_click():
            nuevo_voto = "candidato 2"
            cursor.execute(consulta, (nuevo_voto, dni))
        def boton3_click():
            nuevo_voto = "candidato 3"

        def boton4_click():
            nuevo_voto = "candidato 4"

        def boton5_click():
            nuevo_voto = "candidato 5"

        def boton6_click():
            nuevo_voto = "candidato 6"

        def boton7_click():
            nuevo_voto = "candidato 7"

        def boton8_click():
            nuevo_voto = "candidato 8"
            
        def boton9_click():
            nuevo_voto = "candidato 9"

        def boton10_click():
            nuevo_voto = "candidato 10"

        # Crear un contenedor para los botones
        contenedor = tk.Frame(self.ventana)
        contenedor.pack(pady=10)

        # Crear los botones dentro del contenedor
        boton1 = tk.Button(contenedor, text="Botón 1", width=10, height=5, command=boton1_click)
        boton2 = tk.Button(contenedor, text="Botón 2", width=10, height=5, command=boton2_click)
        boton3 = tk.Button(contenedor, text="Botón 3", width=10, height=5, command=boton3_click)
        boton4 = tk.Button(contenedor, text="Botón 4", width=10, height=5, command=boton4_click)
        boton5 = tk.Button(contenedor, text="Botón 5", width=10, height=5, command=boton5_click)
        boton6 = tk.Button(contenedor, text="Botón 6", width=10, height=5, command=boton6_click)
        boton7 = tk.Button(contenedor, text="Botón 7", width=10, height=5, command=boton7_click)
        boton8 = tk.Button(contenedor, text="Botón 8", width=10, height=5, command=boton8_click)
        boton9 = tk.Button(contenedor, text="Botón 9", width=10, height=5, command=boton9_click)
        boton10 = tk.Button(contenedor, text="Botón 10", width=10, height=5, command=boton10_click)
        etiqueta1 = tk.Label(contenedor, text="Etiqueta 1")
        etiqueta2 = tk.Label(contenedor, text="Etiqueta 2")
        etiqueta3 = tk.Label(contenedor, text="Etiqueta 3")
        etiqueta4 = tk.Label(contenedor, text="Etiqueta 4")
        etiqueta5 = tk.Label(contenedor, text="Etiqueta 5")
        etiqueta6 = tk.Label(contenedor, text="Etiqueta 6")
        etiqueta7 = tk.Label(contenedor, text="Etiqueta 7")
        etiqueta8 = tk.Label(contenedor, text="Etiqueta 8")
        etiqueta9 = tk.Label(contenedor, text="Etiqueta 9")
        etiqueta10 = tk.Label(contenedor, text="Etiqueta 10")
        
        # Ubicar los botones dentro del contenedor usando grid()
        etiqueta1.grid(row=0, column=0, pady=10)
        etiqueta2.grid(row=1, column=0, pady=10)
        etiqueta3.grid(row=2, column=0, pady=10)
        etiqueta4.grid(row=3, column=0, pady=10)
        etiqueta5.grid(row=4, column=0, pady=10)

        boton1.grid(row=0, column=1, pady=10)
        boton2.grid(row=1, column=1, pady=10)
        boton3.grid(row=2, column=1, pady=10)
        boton4.grid(row=3, column=1, pady=10)
        boton5.grid(row=4, column=1, pady=10)

        espacio = tk.Label(contenedor, width=10)
        espacio.grid(row=0, column=2, rowspan=5)  # rowspan=5 para ocupar 5 filas

        etiqueta6.grid(row=0, column=3, pady=10)
        etiqueta7.grid(row=1, column=3, pady=10)
        etiqueta8.grid(row=2, column=3, pady=10)
        etiqueta9.grid(row=3, column=3, pady=10)
        etiqueta10.grid(row=4, column=3, pady=10)

        boton6.grid(row=0, column=4, pady=10)
        boton7.grid(row=1, column=4, pady=10)
        boton8.grid(row=2, column=4, pady=10)
        boton9.grid(row=3, column=4, pady=10)
        boton10.grid(row=4, column=4, pady=10)
        
        # Establecer la conexión a la base de datos
        conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="easyvote"
        )

        # Crear un cursor para ejecutar consultas SQL
        cursor = conexion.cursor()
        
        # Consulta SQL para actualizar el valor del voto
        consulta = "UPDATE votantes SET voto = %s WHERE dni = %s"

        # Ejecutar la consulta SQL con los valores de voto y dni
        #cursor.execute(consulta, (nuevo_voto, dni))
        
        
        
    def iniciar_ventana(self):
        # Ejecutar el bucle principal de la aplicación
        self.ventana.mainloop()


