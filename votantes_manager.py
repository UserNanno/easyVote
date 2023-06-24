from votante import Votante
from database_manager import DatabaseManager

class VotantesManager:
    def __init__(self):
        self.db_manager = DatabaseManager()

    def iniciar_sesion(self, username, password):
        query = "SELECT * FROM Votantes WHERE username = %s AND password = %s"
        result = self.db_manager.execute_query(query, (username, password))

        if result:
            votante_data = result[0]
            votante = Votante(votante_data[0], votante_data[1], votante_data[2], votante_data[3])
            return votante

        return None
