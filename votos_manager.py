from database_manager import DatabaseManager

class VotosManager:
    def __init__(self):
        self.db_manager = DatabaseManager()

    def verificar_voto(self, votante):
        query = "SELECT * FROM Votos WHERE id_votante = %s"
        result = self.db_manager.execute_query(query, (votante.id,))

        if result:
            return True
        return False

    def registrar_voto(self, votante, candidato_id):
        query = "INSERT INTO Votos (id_votante, id_candidato) VALUES (%s, %s)"
        self.db_manager.execute_query(query, (votante.id, candidato_id))
        self.db_manager.commit()
