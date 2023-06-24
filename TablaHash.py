import random
#Estructura TablaHash utilizada para realizar la Búsqueda por Transformación Hash
class TablaHashVotantes:
    # Crea una lista de (tamaño de la lista de votantes) elementos, donde cada elemento es una lista vacía. 
    # Esto se conoce como una lista de listas o una lista anidada (lista de buckets).
    def __init__(self, len):
        self.tabla_hash = [[] for _ in range(len)]

    # Calcula un índice numérico. 
    # Se utiliza para determinar en qué bucket de la tabla hash se almacenará el votante.
    def calcular_hash(self, dni):
        return int(dni) % len(self.tabla_hash)

    #Agrega en los buckets correspondientes de la tabla hash según su número de identificación.
    def llenar_tabla(self, votantes):
        for votante in votantes:
            dni = votante['DNI']
            indice_hash = self.calcular_hash(dni)
            self.tabla_hash[indice_hash].append(votante)

    # Recibe un número de identificación (DNI), calcula el índice hash correspondiente 
    # y busca ese DNI dentro del bucket correspondiente en la tabla hash.
    def obtener_votante(self, dni):
        indice_hash = self.calcular_hash(dni)
        for votante in self.tabla_hash[indice_hash]:
            if votante['DNI'] == dni:
                return votante
        return None