from votante import Votante
from database_manager import DatabaseManager

class VotantesManager:
    def __init__(self):
        self.db_manager = DatabaseManager()

    def buscar_por_username(self, username):
        query = "SELECT id, dni, username, password FROM Votantes WHERE username = %s"
        result = self.db_manager.execute_query(query, (username,))

        if result:
            votante_data = result[0]
            votante = Votante(*votante_data)  # Utilizar * para desempaquetar los valores
            return votante

        return None

