class ResultPresenter:
    @staticmethod
    def present_results(rango_edad_min, rango_edad_max, candidato_mas_votos, cantidad_votos, detalles_votos):
        print(f"Resultados para el rango de edad {rango_edad_min}-{rango_edad_max}:")
        print(f"El candidato con más votos es {candidato_mas_votos} con {cantidad_votos} votos.")
        print("Detalles de los votos:")
        for votante in detalles_votos:
            print(f"DNI: {votante.dni}, Nombre: {votante.nombre}, Apellido: {votante.apellido}, Región: {votante.region}")
