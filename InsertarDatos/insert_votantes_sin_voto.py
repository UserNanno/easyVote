import random
import string
import mysql.connector

# Conectarse a la base de datos
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="easyvote"
)
cursor = conn.cursor()

# Definir los departamentos
departamentos_peru = ['Amazonas', 'Ancash', 'Apurímac', 'Arequipa', 'Ayacucho',
                                  'Cajamarca', 'Callao', 'Cusco', 'Huancavelica', 'Huánuco',
                                  'Ica', 'Junín', 'La Libertad', 'Lambayeque', 'Lima', 'Loreto',
                                  'Madre de Dios', 'Moquegua', 'Pasco', 'Piura', 'Puno', 'San Martín',
                                  'Tacna', 'Tumbes', 'Ucayali']


# Generar 1000 datos aleatorios e insertarlos en la base de datos
for _ in range(4047):
    # Generar valores aleatorios
    dni = ''.join(random.choices(string.digits, k=8))
    nombre = ''.join(random.choices(string.ascii_uppercase, k=10))
    apellido = ''.join(random.choices(string.ascii_uppercase, k=10))
    departamento = random.choice(departamentos_peru)
    genero = random.choice(["M", "F"])
    edad = random.randint(18, 65)

    # Crear la consulta SQL
    sql = "INSERT INTO votantes (dni, nombre, apellido, departamento, genero, edad) VALUES (%s, %s, %s, %s, %s, %s)"
    valores = (dni, nombre, apellido, departamento, genero, edad)

    # Ejecutar la consulta
    cursor.execute(sql, valores)
    conn.commit()

# Cerrar la conexión a la base de datos
cursor.close()
conn.close()
