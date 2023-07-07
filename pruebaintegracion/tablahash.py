#ESTRUCTURA TABLA HASH
#Esta estructura solo almacena los datos de los votantes que han realizado su voto
#ALGORITMO DE BUSQUEDA HASHMAP
from database_manager import DatabaseManager
class TablaHash:
    def __init__(self,tamano):
        self.tamano=tamano
        self.tabla = {}
        self.db_manager = DatabaseManager()
        self.insertar_votantes_registrados()

    def _calcular_hash(self, dni):
        # Función de hash para calcular el índice de la tabla hash a partir del DNI
        hash_value = sum(int(digit) for digit in dni) % self.tamano
        return hash_value

    def insertar(self, dni, voto):
        # Insertar un DNI y su voto en la tabla hash
        hash_key = self._calcular_hash(dni)
        if hash_key not in self.tabla:
            self.tabla[hash_key] = {}
        self.tabla[hash_key][dni] = voto

    def buscar(self, dni):
        # Buscar el voto asociado a un DNI en la tabla hash
        hash_key = self._calcular_hash(dni)
        if hash_key in self.tabla and dni in self.tabla[hash_key]:
            return self.tabla[hash_key][dni]
        return None

    def insertar_votantes_registrados(self):
        # Insertar los votantes registrados en la base de datos que han realizado su voto a la tabla hash
        query = "SELECT dni, voto FROM votantes WHERE voto IS NOT NULL"
        result = self.db_manager.execute_query(query)
        for row in result:
            dni = row[0]
            voto = row[1]
            self.insertar(dni, voto)