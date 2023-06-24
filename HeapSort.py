
def heapify(arr, n, i):
    largest = i  # Inicializar el nodo raíz como el más grande
    l = 2 * i + 1  # Índice del hijo izquierdo
    r = 2 * i + 2  # Índice del hijo derecho

    # Verificar si el hijo izquierdo del nodo raíz existe y es mayor que la raíz
    if l < n and arr[i][1] < arr[l][1]:
        largest = l

    # Verificar si el hijo derecho del nodo raíz existe y es mayor que la raíz
    if r < n and arr[largest][1] < arr[r][1]:
        largest = r

    # Cambiar la raíz si es necesario
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Intercambiar los valores
        heapify(arr, n, largest)  # Heapify recursivamente el subárbol afectado

def heapSort(arr):
    n = len(arr)

    # Construir un max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extraer elementos uno por uno del heap
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Intercambiar el máximo actual con el último elemento sin ordenar
        heapify(arr, i, 0)  # Heapify el subárbol reducido

# Ejemplo de uso:
votos = {
    'Region A': 10,
    'Region B': 5,
    'Region C': 8,
    'Region D': 3,
    'Region E': 12
}

# Convertir el diccionario en una lista de tuplas (país, cantidad de votos)
lista_votos = list(votos.items())

heapSort(lista_votos)

print("Cantidad de votos del canditato X por regiones (orden descendente):")
for pais, votos in lista_votos:
    print(pais, ':', votos)