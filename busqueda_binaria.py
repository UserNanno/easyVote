def busqueda_binaria(columna, dni):
    columna = sorted(columna)
    
    inicio = 0
    fin = len(columna) - 1
    resultado = False

    while inicio <= fin:
        medio = (inicio + fin) // 2
        valor_medio = columna[medio]

        if valor_medio == dni:
            # El DNI fue encontrado
            resultado = True
            break
        elif valor_medio < dni:
            inicio = medio + 1
        else:
            fin = medio - 1
    
    return resultado
