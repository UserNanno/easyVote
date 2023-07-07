from database import Database
from sort import merge_sort
from result_presenter import ResultPresenter

class VoterAnalyzer:
    def __init__(self, host, user, password, database):
        self.database = Database(host, user, password, database)

    def analyze_voters(self, rango_edad_min, rango_edad_max):
        self.database.connect()

        query = f"SELECT dni, nombre, apellido, region, genero, edad, voto FROM votantes WHERE edad >= {rango_edad_min} AND edad <= {rango_edad_max}"
        votantes = self.database.fetch_votantes(query)

        if votantes:
            votos_por_candidato = {}
            for votante in votantes:
                candidato = votante.voto
                if candidato in votos_por_candidato:
                    votos_por_candidato[candidato] += 1
                else:
                    votos_por_candidato[candidato] = 1

            resultados_ordenados = merge_sort(list(votos_por_candidato.items()))
            candidato_mas_votos = resultados_ordenados[-1][0]
            cantidad_votos = resultados_ordenados[-1][1]

            detalles_votos = [votante for votante in votantes if votante.voto == candidato_mas_votos]

            ResultPresenter.present_results(rango_edad_min, rango_edad_max, candidato_mas_votos, cantidad_votos, detalles_votos)

        else:
            print("No se encontraron votos para el rango de edad especificado.")

        self.database.close()
