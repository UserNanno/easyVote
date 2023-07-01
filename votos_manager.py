from database_manager import DatabaseManager
from TablaHash import HashTable
class VotosManager:
    def __init__(self):
        self.db_manager = DatabaseManager()
        self.votos_realizados = HashTable() 

    def verificar_voto(self, votante):
        if self.votos_realizados.contains(votante.id):
            return True
        else:
            query = "SELECT * FROM Votos WHERE id_votante = %s"
            result = self.db_manager.execute_query(query, (votante.id,))

            if result:
                self.votos_realizados.insert(votante.id, True)  # Actualizamos la tabla hash con el voto realizado
                return True
            return False

    def registrar_voto(self, votante, candidato_id):
        query = "INSERT INTO Votos (id_votante, id_candidato) VALUES (%s, %s)"
        self.db_manager.execute_query(query, (votante.id, candidato_id))
        self.db_manager.commit()
