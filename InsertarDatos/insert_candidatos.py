import mysql.connector

# Establecer la conexión a la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="easyvote"
)

# Crear un cursor para ejecutar las consultas SQL
cursor = conexion.cursor()

# Solicitar los datos al usuario y almacenarlos en una lista
lista_datos = []
num_datos = int(input("Ingrese el número de datos que desea ingresar: "))
for i in range(num_datos):
    print("Para el candidato:", i + 1)
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    partido_politico = input("Ingrese el partido_politico: ")
    lista_datos.append((nombre, apellido, partido_politico))

# Definir la consulta SQL para insertar los datos en la tabla
consulta = "INSERT INTO candidatos (nombre, apellido, partido_politico) VALUES (%s, %s, %s)"

# Iterar sobre los datos ingresados por el usuario y ejecutar la consulta para cada conjunto de valores
for datos in lista_datos:
    cursor.execute(consulta, datos)

# Confirmar los cambios en la base de datos
conexion.commit()

# Cerrar el cursor y la conexión a la base de datos
cursor.close()
conexion.close()
