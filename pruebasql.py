import mysql.connector

# Función para realizar el ordenamiento Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i][1] > right[j][1]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result

# Conectarse a la base de datos
try:
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='easyvote'
    )
    cursor = conn.cursor()

    # Obtener los datos de la tabla de votantes
    cursor.execute("SELECT dni, nombre, apellido, region, genero, edad, voto FROM votantes")
    resultados = cursor.fetchall()

    # Guardar los datos en una lista
    datos_votantes = []
    for fila in resultados:
        dni = fila[0]
        nombre = fila[1]
        apellido = fila[2]
        region = fila[3]
        genero = fila[4]
        edad = fila[5]
        voto = fila[6]
        datos_votantes.append((dni, nombre, apellido, region, genero, edad, voto))

    # Cerrar el cursor y la conexión con la base de datos
    cursor.close()
    conn.close()

    # Determinar el candidato con más votos utilizando Merge Sort
    candidatos_ordenados = merge_sort(datos_votantes)

    # print("Resultados de los votos:")
    # for candidato in candidatos_ordenados:
    #     print(f"Candidato {candidato[6]}: {candidato[1]} votos")

    # Obtener los rangos de edad
    edades = set(votante[5] for votante in datos_votantes)

    # Filtrar y mostrar el candidato con más votos y la cantidad en cada rango de edad
    for edad in sorted(edades):
        votos_por_candidato = {}
        for votante in datos_votantes:
            if votante[5] == edad:
                voto = votante[6]
                if voto in votos_por_candidato:
                    votos_por_candidato[voto] += 1
                else:
                    votos_por_candidato[voto] = 1

        candidato_mas_votos = max(votos_por_candidato, key=votos_por_candidato.get)
        cantidad_votos = votos_por_candidato[candidato_mas_votos]
        print(f"Para el rango de edad {edad}, el candidato {candidato_mas_votos} tuvo {cantidad_votos} votos.")

except mysql.connector.Error as error:
    print("Error al conectarse a la base de datos:", error)
