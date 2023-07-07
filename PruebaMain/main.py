from voter_analyzer import VoterAnalyzer

if __name__ == "__main__":
    host = 'localhost'
    user = 'root'
    password = ''
    database_name = 'easyvote'

    analyzer = VoterAnalyzer(host, user, password, database_name)

    rango_edad_min = int(input("Ingrese el rango de edad mínimo: "))
    rango_edad_max = int(input("Ingrese el rango de edad máximo: "))

    analyzer.analyze_voters(rango_edad_min, rango_edad_max)
