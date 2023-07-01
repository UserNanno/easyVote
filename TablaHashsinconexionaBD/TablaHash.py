class TablaHashVotantes:
    def __init__(self):
        self.tabla_hash = [[] for _ in range(100)]
        # La función __init__ inicializa la clase y crea una tabla hash vacía
        # utilizando una lista de listas. La longitud de la tabla hash se establece en 10.

    def calcular_hash(self, dni):
        return int(dni) % len(self.tabla_hash)
        # La función calcular_hash recibe un número de identificación (dni) como entrada
        # y utiliza el operador de módulo (%) para calcular el índice de la tabla hash
        # correspondiente al dni. El resultado es un número entero que representa el índice.

    def llenar_tabla(self, votantes):
        for votante in votantes:
            dni = votante['DNI']
            indice_hash = self.calcular_hash(dni)
            self.tabla_hash[indice_hash].append(votante)
        # La función llenar_tabla recibe una lista de votantes como entrada y
        # recorre cada votante en la lista. Para cada votante, se obtiene su dni y
        # se calcula el índice de la tabla hash correspondiente utilizando la función
        # calcular_hash. Luego, el votante se agrega a la lista ubicada en ese índice de la tabla hash.

    def obtener_votante(self, dni):
        indice_hash = self.calcular_hash(dni)
        for votante in self.tabla_hash[indice_hash]:
            if votante['DNI'] == dni:
                return votante
        return None
        # La función obtener_votante recibe un dni como entrada y utiliza la función
        # calcular_hash para obtener el índice de la tabla hash correspondiente.
        # Luego, se recorre la lista ubicada en ese índice y se compara el dni de cada votante
        # con el dni proporcionado. Si se encuentra un votante con el mismo dni, se devuelve
        # ese votante. Si no se encuentra ningún votante con el dni dado, se devuelve None.