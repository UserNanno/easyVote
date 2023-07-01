from database_manager import DatabaseManager

class VotosManager:
    def __init__(self):
        self.db_manager = DatabaseManager()
        self.tabla_votos = {}  # Tabla hash para almacenar los votos
        self.cargar_votos_desde_base_de_datos()  # Cargar los votos al iniciar la instancia

    def cargar_votos_desde_base_de_datos(self):
        # Cargar todos los votos desde la base de datos y almacenarlos en la tabla hash
        query = "SELECT id_votante, id_candidato FROM Votos"
        result = self.db_manager.execute_query(query)
        for row in result:
            id_votante, id_candidato = row
            self.tabla_votos[id_votante] = id_candidato

    def verificar_voto(self, votante):
        # Verificar si el votante está en la tabla hash
        return votante.id in self.tabla_votos

    def registrar_voto(self, votante, candidato_id):
        query = "INSERT INTO Votos (id_votante, id_candidato) VALUES (%s, %s)"
        self.db_manager.execute_query(query, (votante.id, candidato_id))
        self.db_manager.commit()
        # También actualizar la tabla hash con el nuevo voto registrado
        self.tabla_votos[votante.id] = candidato_id
