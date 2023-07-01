from candidato import Candidato
from database_manager import DatabaseManager

class CandidatosManager:
    def __init__(self):
        self.db_manager = DatabaseManager()

    def obtener_candidatos(self):
        query = "SELECT * FROM Candidatos"
        result = self.db_manager.execute_query(query)

        candidatos = []
        for candidato_data in result:
            candidato = Candidato(candidato_data[0], candidato_data[1], candidato_data[2])
            candidatos.append(candidato)

        return candidatos

    def validar_candidato(self, candidato_id, candidatos):
        for candidato in candidatos:
            if candidato.id == int(candidato_id):
                return True
        return False