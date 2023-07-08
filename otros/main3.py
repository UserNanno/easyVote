from modelo.votantes import Votante
from modelo.persona import Persona

persona1 = Persona("11111111A", "Juan", "Pérez", "América", "Masculino", 30, "Candidato A")
persona2 = Persona("22222222B", "María", "Gómez", "Europa", "Femenino", 28, "Candidato A")
persona3 = Persona("33333333C", "Carlos", "López", "Asia", "Masculino", 35, "Candidato B")
persona4 = Persona("44444444D", "Ana", "Rodríguez", "África", "Femenino", 25, "Candidato A")
persona5 = Persona("11111111A", "Juan", "Pérez", "América", "Masculino", 30, "Candidato B")
persona6 = Persona("22222222B", "María", "Gómez", "Europa", "Femenino", 28, "Candidato D")
persona7 = Persona("33333333C", "Carlos", "López", "Asia", "Masculino", 35, "Candidato D")
persona8 = Persona("44444444D", "Ana", "Rodríguez", "África", "Femenino", 25, "Candidato C")
persona9 = Persona("33333333C", "Carlos", "López", "Asia", "Masculino", 35, "Candidato D")
persona10 = Persona("44444444D", "Ana", "Rodríguez", "África", "Femenino", 25, "Candidato C")

arreglo_votante = [persona1, persona2, persona3, persona4, persona5, persona6, persona7, persona8, persona9, persona10]


votantes=Votante(arreglo_votante)

#contar votos totales
print("votos globales")
votos_por_candidato = votantes.contar_votos_por_candidato()

for candidato, cantidad_votos in votos_por_candidato.items():
    print("Candidato:", candidato,": ", cantidad_votos)
    
print()

#contar por región
region_especifica = "América"
votos_por_candidato_en_region = votantes.contar_votos_por_candidato_en_region(region_especifica)

print(f"Votos por candidato en la región {region_especifica}:")
for candidato, votos in votos_por_candidato_en_region.items():
    print(f"{candidato}: {votos}")
print()

#contar votos por genero 
genero_especifico = "Masculino"
votos_por_candidato_en_genero = votantes.contar_votos_por_candidato_en_genero(genero_especifico)

print(f"Votos por candidato en el género {genero_especifico}:")
for candidato, votos in votos_por_candidato_en_genero.items():
    print(f"{candidato}: {votos}")
print()