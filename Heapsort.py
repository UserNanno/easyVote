import mysql.connector


def heapsort(departamento):
    candidatos = []
    votos = []
    
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
        WHERE departamento = '{}'
        GROUP BY voto
        """.format(departamento)

    # Ejecutar la consulta
    cursor.execute(consulta)

    # Obtener los resultados
    resultados = cursor.fetchall()
    
    # Extrayendo la información en listas
    for candidato, voto in resultados:
        candidatos.append(candidato)
        votos.append(voto)
        
    heapsort_candidatos(candidatos, votos) 

    return candidatos, votos
    

def heapsort_candidatos(candidatos, votos):
    n = len(votos)

    # Construir un heap máximo
    for i in range(n // 2 - 1, -1, -1):
        heapify(candidatos, votos, n, i)

    # Extraer los elementos uno por uno del heap
    for i in range(n - 1, 0, -1):
        # Intercambiar el elemento raíz (mayor) con el último elemento sin ordenar
        candidatos[i], candidatos[0] = candidatos[0], candidatos[i]
        votos[i], votos[0] = votos[0], votos[i]

        # Llamar a heapify en el heap reducido
        heapify(candidatos, votos, i, 0)

def heapify(candidatos, votos, n, i):
    largest = i  # Inicializar el nodo raíz como el más grande
    l = 2 * i + 1  # Hijo izquierdo
    r = 2 * i + 2  # Hijo derecho

    # Si el hijo izquierdo es más grande que la raíz
    if l < n and votos[l] > votos[largest]:
        largest = l

    # Si el hijo derecho es más grande que la raíz o el hijo izquierdo
    if r < n and votos[r] > votos[largest]:
        largest = r

    # Si el nodo raíz no es el más grande
    if largest != i:
        # Intercambiar la raíz con el nodo más grande
        candidatos[i], candidatos[largest] = candidatos[largest], candidatos[i]
        votos[i], votos[largest] = votos[largest], votos[i]

        # Llamar recursivamente a heapify en el subárbol afectado
        heapify(candidatos, votos, n, largest)
