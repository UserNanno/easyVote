import mysql.connector
import random

# Establecer la conexión
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="easyVote"
)

# Verificar si la conexión fue exitosa
if conexion.is_connected():
    print("Conexión exitosa a la base de datos.")

    # Crear un cursor para ejecutar consultas SQL
    cursor = conexion.cursor()

    # Lista de nombres disponibles
    nombres_disponibles = [
    "Juan", "María", "Pedro", "Ana", "Luis", "Laura", "Carlos", "Sofía", "Diego", "Valentina",
    "Andrés", "Camila", "Gabriel", "Isabella", "Javier", "Lucía", "Manuel", "Valeria", "Óscar",
    "Carolina", "Miguel", "Fernanda", "Ricardo", "Julia", "Eduardo", "Mariana", "Gonzalo", "Paula",
    "Rodrigo", "Catalina", "Alejandro", "Florencia", "Sebastián", "Antonella", "Daniel", "Renata",
    "Hugo", "Vanesa", "Federico", "Julieta", "Emilio", "Melanie", "Raúl", "Abril", "Agustín", "Daniela",
    "Mario", "Celeste", "Ignacio", "Natalia", "Pablo", "Elena", "Gustavo", "Valentina", "Esteban", "Gabriela",
    "Héctor", "Victoria", "Leonardo", "Luciana", "Roberto", "Marina", "Ramón", "Alejandra", "Armando",
    "Verónica", "Mauricio", "Patricia", "Raquel", "Francisco", "Olivia", "Óscar", "Lorena", "Samuel",
    "Gabriela", "Benjamín", "Renata", "Erick", "Jazmín", "César", "Constanza", "Arturo", "Adriana",
    "Martín", "Carmen", "Ulises", "Paola", "Maximiliano", "Jimena", "Felipe", "Isabel", "Lorenzo",
    "María José", "Gael", "Daniela", "Jaime", "Bianca", "Alexandra", "Santiago", "Isabella"
    ]
    
    apellidos_disponibles = [
    "García", "Rodríguez", "González", "Hernández", "López", "Martínez", "Pérez", "Sánchez", "Ramírez", "Flores",
    "Torres", "Rivera", "Gómez", "Díaz", "Reyes", "Morales", "Ortiz", "Silva", "Rojas", "Vargas",
    "Romero", "Mendoza", "Guerrero", "Medina", "Ruiz", "Cruz", "Jiménez", "Paz", "Castillo", "Valdez",
    "Ramos", "Espinoza", "Cortez", "Chávez", "Acosta", "Molina", "Ochoa", "Vega", "Navarro", "Miranda",
    "Aguilar", "Soto", "Bautista", "Fernández", "Campos", "Zamora", "Guzmán", "Vásquez", "León", "Peralta",
    "Herrera", "Ríos", "Mejía", "Delgado", "Cabrera", "Padilla", "Montes", "Cordero", "Arias", "Santos",
    "Peña", "Carrillo", "Cruz", "Cervantes", "Sepúlveda", "Ibarra", "Escobar", "Rocha", "Barrera", "Salgado",
    "Pacheco", "Morán", "Arroyo", "Bustamante", "Villarreal", "Serrano", "Calderón", "Urrutia", "Mora", "Miramontes",
    "Benítez", "Ponce", "Navarrete", "Escalante", "Del Valle", "Ontiveros", "Roldán", "Treviño", "Villanueva", "Franco",
    "Munguía", "Paredes", "Salas", "Aldana", "Beltrán", "Ceja", "Estrada", "Lara", "Nieto", "Rico"
    ]
    
    genero_disponible=["M","F"]
    
    region_disponible=['La Libertad', 'Cajamarca', 'San Martín', 'Tacna', 'Junín', 
                       'Arequipa', 'Apurímac', 'Huancavelica', 'Piura', 'Ayacucho', 
                       'Puno', 'Cusco', 'Lima', 'Madre de Dios', 'Moquegua', 'Huánuco', 
                       'Lambayeque', 'Callao', 'Tumbes', 'Pasco', 'Ucayali', 'Amazonas', 
                       'Ancash', 'Ica', 'Loreto']
    
    candidato_disponible=["A","B","C","D",
            "E","F","G","H",
            "I","J" ]

    # Generar y insertar DNIs y nombres juntos
    registros = []  # Lista para almacenar los registros

    for _ in range(1000):
        dni = ''.join(random.choices("0123456789", k=8))  # Generar un DNI aleatorio
        nombre = random.choice(nombres_disponibles)  # Elegir un nombre aleatorio de la lista
        apellido=random.choice(apellidos_disponibles)
        genero=random.choice(genero_disponible)
        edad=random.randint(18, 90)
        region=random.choice(region_disponible)
        voto=random.choice(candidato_disponible)
        
        registro = (dni, nombre, apellido, region, genero, edad,voto)  # Crear una tupla con el DNI y el nombre
        registros.append(registro)  # Agregar el registro a la lista

    insertar_sql = "INSERT INTO votantes (dni, nombre, apellido, region, genero, edad, voto) VALUES (%s, %s, %s, %s, %s, %s, %s)"

    cursor.executemany(insertar_sql, registros)
    conexion.commit()

    print("Registros insertados exitosamente.")

    # Cerrar el cursor
    cursor.close()

# Cerrar la conexión
conexion.close()
