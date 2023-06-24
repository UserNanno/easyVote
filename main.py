import random

from TablaHash import TablaHashVotantes

#Lista de votantes generada aleatoriamente para simular la base de datos
def generar_lista_votantes(cant):
    lista_votantes = []
    for _ in range(cant):
        votante = {
            'DNI': str(random.randint(10000000, 99999999)),
            'nombres': generar_nombre_aleatorio(),
            'apellido_paterno': generar_apellido_aleatorio(),
            'apellido_materno': generar_apellido_aleatorio(),
            'edad': random.randint(18, 70),
            'sexo': random.choice(['M', 'F']),
            'region': generar_region_aleatoria(),
            'voto_candidato': random.choice([0, 1, 2, 3, 4, 5])
        }
        lista_votantes.append(votante)
    return lista_votantes

def generar_nombre_aleatorio():
    nombres = ['Juan', 'María', 'Carlos', 'Laura', 'Luis', 'Ana', 'Pedro', 'Mónica', 'Javier', 'Elena']
    return random.choice(nombres)

def generar_apellido_aleatorio():
    apellidos = ['Gómez', 'López', 'González', 'Rodríguez', 'Martínez', 'Pérez', 'Fernández', 'García', 'Hernández', 'Torres']
    return random.choice(apellidos)

def generar_region_aleatoria():
    regiones = ['Lima', 'Arequipa', 'Cusco', 'Trujillo', 'Piura', 'Iquitos', 'Chiclayo', 'Tacna', 'Cajamarca', 'Puno']
    return random.choice(regiones)

def mostrar_lista_votantes(lista_votantes):
    for votante in lista_votantes:
        print("\n--------------------")
        print("DNI:", votante['DNI'])
        print("Apellido Paterno:", votante['apellido_paterno'])
        print("Voto Candidato:", votante['voto_candidato'])
        print("--------------------")

# Se genera la lista de votantes
lista_votantes = generar_lista_votantes(5)

# Se crea una instancia de la tabla hash de votantes
tabla_votantes = TablaHashVotantes()

# Se llena la tabla hash con los votantes generados
tabla_votantes.llenar_tabla(lista_votantes)

# Muestra la lista de votantes
mostrar_lista_votantes(lista_votantes)

# Verifica la identidad de un votante ingresando su DNI
print("\t\t\t\tSISTEMA DE VOTO ELECTRONICO easyVote\n")
dni = input("Ingrese su DNI para verificar su identidad: ")
votante = tabla_votantes.obtener_votante(dni)

if votante is not None:
    if votante['voto_candidato'] == 0:
        print("Por favor, proceda a realizar su voto.")
    else:
        print("Usted ya ha realizado su voto.")
else:
    print("Votante no encontrado en la base de datos.")




