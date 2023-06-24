import random
#Estructura TablaHash utilizada para realizar la Búsqueda por Transformación Hash
class TablaHashVotantes:
    def __init__(self):
        self.tabla_hash = [[] for _ in range(10)]

    def calcular_hash(self, dni):
        return int(dni) % len(self.tabla_hash)

    def llenar_tabla(self, votantes):
        for votante in votantes:
            dni = votante['DNI']
            indice_hash = self.calcular_hash(dni)
            self.tabla_hash[indice_hash].append(votante)

    def obtener_votante(self, dni):
        indice_hash = self.calcular_hash(dni)
        for votante in self.tabla_hash[indice_hash]:
            if votante['DNI'] == dni:
                return votante
        return None