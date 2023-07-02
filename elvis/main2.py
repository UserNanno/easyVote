import tkinter as tk

# Crear la ventana
ventana = tk.Tk()

# Agregar contenido a la ventana
etiqueta = tk.Label(ventana, text="SISTEMA DE VOTACIÓN ELECTRÓNICO")

etiqueta.pack(pady=30)


# Configurar propiedades de la ventana
ventana.title("EasyVote")
ventana.geometry("500x400")  # Tamaño de la ventana en píxeles

# Funciones para los botones
def boton1_click():
    print("Botón 1 fue clickeado")

def boton2_click():
    print("Botón 2 fue clickeado")



# Crear un contenedor para los botones
contenedor = tk.Frame(ventana)
contenedor.pack(pady=50)

# Crear los botones dentro del contenedor
boton1 = tk.Button(contenedor, text="Votar",width=20, height=10, command=boton1_click)
boton2 = tk.Button(contenedor, text="Estadistica",width=20, height=10, command=boton2_click)




# Ubicar los botones dentro del contenedor
boton1.pack(side="left", padx=10)
boton2.pack(side="left", padx=10)


# Ejecutar el bucle principal de la aplicación
ventana.mainloop()
