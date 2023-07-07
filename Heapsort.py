import mysql.connector

def ordenar_votos_por_region(region):
    # Establecer conexión con la base de datos
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="easyvote"
    )

    # Crear un cursor para ejecutar consultas SQL
    cursor = conexion.cursor()

    # Ejemplo de consulta SQL para obtener los candidatos de una región específica
    consulta = """
        SELECT voto, COUNT(*) AS cantidad_votos
        FROM votantes
        GROUP BY voto
        WHERE region = '{region}'
        """

    # Ejecutar la consulta
    cursor.execute(consulta)

    # Obtener los resultados
    resultados = cursor.fetchall()
    
    # extrayendo la informacón en listas
    for candidato, votos in resultados:
            self.candidatos.append(candidato)
            self.votos.append(votos)

    def heapify(arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and arr[i][2] < arr[l][2]:
            largest = l

        if r < n and arr[largest][2] < arr[r][2]:
            largest = r

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)


    def heapSort(arr):
        n = len(arr)

        for i in range(n // 2 - 1, -1, -1):
            heapify(arr, n, i)

        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            heapify(arr, i, 0)

    # Ordenar los candidatos por votos utilizando HeapSort en orden descendente
    heapSort(resultados)
    resultados.reverse()

    # Mostrar los candidatos ordenados
    for candidato in resultados:
        print(f"Región: {region}, Voto: {candidato[0]}, Género: {candidato[1]}, Edad: {candidato[2]}")

    # Cerrar la conexión con la base de datos
    conexion.close()



