def burbuja(nombres, votos):
    n = len(votos)

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if votos[j] < votos[j + 1]:
                # Intercambiar los elementos si están en el orden incorrecto
                nombres[j], nombres[j + 1] = nombres[j + 1], nombres[j]
                votos[j], votos[j + 1] = votos[j + 1], votos[j]

    return nombres, votos
