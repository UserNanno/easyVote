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
        if left[i][1] < right[j][1]: # Ordenar por la cantidad de votos: > paa que muestre el que tiene menos votos y < para que muestre el que tiene mas votos
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

    # Obtener el rango de edades
    rango_edad_min = int(input("Ingrese el rango de edad mínimo: "))
    rango_edad_max = int(input("Ingrese el rango de edad máximo: "))

    # Filtrar los votantes dentro del rango de edad especificado
    cursor.execute(f"SELECT dni, nombre, apellido, region, genero, edad, voto FROM votantes WHERE edad >= {rango_edad_min} AND edad <= {rango_edad_max}")
    resultados = cursor.fetchall()

    if resultados:
        # Contar los votos por candidato
        votos_por_candidato = {}
        for fila in resultados:
            candidato = fila[6]
            if candidato in votos_por_candidato:
                votos_por_candidato[candidato] += 1
            else:
                votos_por_candidato[candidato] = 1

        # Obtener el candidato con más votos utilizando Merge Sort
        resultados_ordenados = merge_sort(list(votos_por_candidato.items()))
        candidato_mas_votos = resultados_ordenados[-1][0]
        cantidad_votos = resultados_ordenados[-1][1]

        # Obtener los detalles de los votos del candidato con más votos
        cursor.execute(f"SELECT dni, nombre, apellido, region FROM votantes WHERE edad >= {rango_edad_min} AND edad <= {rango_edad_max} AND voto = '{candidato_mas_votos}'")
        detalles_votos = cursor.fetchall()

        print(f"Resultados para el rango de edad {rango_edad_min}-{rango_edad_max}:")
        print(f"El candidato con más votos es {candidato_mas_votos} con {cantidad_votos} votos.")
        print("Detalles de los votos:")
        for fila in detalles_votos:
            print(f"DNI: {fila[0]}, Nombre: {fila[1]}, Apellido: {fila[2]}, Región: {fila[3]}")

    else:
        print("No se encontraron votos para el rango de edad especificado.")

    # Cerrar el cursor y la conexión con la base de datos
    cursor.close()
    conn.close()

except mysql.connector.Error as error:
    print("Error al conectarse a la base de datos:", error)
