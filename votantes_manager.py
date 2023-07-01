from votante import Votante
from database_manager import DatabaseManager

class VotantesManager:
    def __init__(self):
        self.db_manager = DatabaseManager()

    def iniciar_sesion(self, dni, password):
        query = "SELECT * FROM Votantes WHERE dni = %s AND password = %s"
        result = self.db_manager.execute_query(query, (dni, password))

        if result:
            votante_data = result[0]
            votante = Votante(votante_data[0], votante_data[1], votante_data[2])
            return votante

        return None

    def buscar_por_dni(self, dni):
        query = "SELECT * FROM Votantes USE INDEX (dni) WHERE dni = %s"
        result = self.db_manager.execute_query(query, (dni,))
        
        if result:
            votante_data = result[0]
            votante = Votante(votante_data[0], votante_data[1], votante_data[2])
            return votante

        return None
