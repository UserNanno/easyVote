nombres=["Candidato A","Candidato B","Candidato C","Candidato D",
            "Candidato E","Candidato F","Candidato G","Candidato H",
            
            ]

votos=[3215,6518,8495,6284,8495,9184,152,9514]


def quicksort_votos_candidatos(nombres, votos):
    if len(votos) <= 1:
        return nombres, votos

    pivot = votos[len(votos) // 2]
    nombres_menores, votos_menores = [], []
    nombres_iguales, votos_iguales = [], []
    nombres_mayores, votos_mayores = [], []

    for nombre, voto in zip(nombres, votos):
        if voto > pivot:
            nombres_mayores.append(nombre)
            votos_mayores.append(voto)
        elif voto == pivot:
            nombres_iguales.append(nombre)
            votos_iguales.append(voto)
        else:
            nombres_menores.append(nombre)
            votos_menores.append(voto)

    nombres_ordenados_mayores, votos_ordenados_mayores = quicksort_votos_candidatos(nombres_mayores, votos_mayores)
    nombres_ordenados_menores, votos_ordenados_menores = quicksort_votos_candidatos(nombres_menores, votos_menores)

    return nombres_ordenados_mayores + nombres_iguales + nombres_ordenados_menores, votos_ordenados_mayores + votos_iguales + votos_ordenados_menores

nombres_ordenados, votos_ordenados = quicksort_votos_candidatos(nombres, votos)

for nombre, voto in zip(nombres_ordenados, votos_ordenados):
    print(nombre, ":", voto)


