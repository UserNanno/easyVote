def burbuja(nombres, votos, comparacion=None):
    if len(nombres) != len(votos):
        raise ValueError("Las listas nombres y votos deben tener la misma longitud.")
    
    n = len(votos)

    for i in range(n - 1):
        intercambiado = False
        for j in range(0, n - i - 1):
            if comparacion is None:
                if votos[j] < votos[j + 1]:
                    # Intercambiar los elementos si están en el orden incorrecto
                    nombres[j], nombres[j + 1] = nombres[j + 1], nombres[j]
                    votos[j], votos[j + 1] = votos[j + 1], votos[j]
                    intercambiado = True
            else:
                if comparacion(votos[j], votos[j + 1]) < 0:
                    # Intercambiar los elementos si están en el orden incorrecto
                    nombres[j], nombres[j + 1] = nombres[j + 1], nombres[j]
                    votos[j], votos[j + 1] = votos[j + 1], votos[j]
                    intercambiado = True
        
        if not intercambiado:
            break

    return nombres, votos