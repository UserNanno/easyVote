class Persona:
    def __init__(self, dni, nombre, apellido, region, genero, edad, voto):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.region = region
        self.genero = genero
        self.edad = edad
        self.voto = voto

class Votante:
    def __init__(self, personas):
        
        self.personas=personas
        self.dnis=[]
        self.nombre=[]
        self.apellido=[]
        self.region=[]
        self.genero=[]
        self.edad =[]
        self.voto=[]

                
        for persona in personas:
            self.dnis.append(persona.dni)
            self.nombre.append(persona.nombre )
            self.apellido.append(persona.apellido)
            self.region.append(persona.region )
            self.genero.append(persona.genero )
            self.edad.append(persona.edad )
            self.voto.append(persona.voto)
            
    def contar_votos_por_candidato(self):
        votos_por_candidato = {}
        
        for persona in self.personas:
            candidato = persona.voto
            
            if candidato in votos_por_candidato:
                votos_por_candidato[candidato] += 1
            else:
                votos_por_candidato[candidato] = 1
        
        return votos_por_candidato
    
    def contar_votos_por_genero(self):
        votos_por_genero = {}

        for persona in self.personas:
            genero = persona.genero

            if genero in votos_por_genero:
                votos_por_genero[genero] += 1
            else:
                votos_por_genero[genero] = 1

        return votos_por_genero

persona1 = Persona("11111111A", "Juan", "Pérez", "América", "Masculino", 30, "Candidato A")
persona2 = Persona("22222222B", "María", "Gómez", "Europa", "Femenino", 28, "Candidato A")
persona3 = Persona("33333333C", "Carlos", "López", "Asia", "Masculino", 35, "Candidato B")
persona4 = Persona("44444444D", "Ana", "Rodríguez", "África", "Femenino", 25, "Candidato A")
persona5 = Persona("11111111A", "Juan", "Pérez", "América", "Masculino", 30, "Candidato A")
persona6 = Persona("22222222B", "María", "Gómez", "Europa", "Femenino", 28, "Candidato D")
persona7 = Persona("33333333C", "Carlos", "López", "Asia", "Masculino", 35, "Candidato D")
persona8 = Persona("44444444D", "Ana", "Rodríguez", "África", "Femenino", 25, "Candidato C")

arreglo_votante = [persona1, persona2, persona3, persona4, persona5, persona6, persona7, persona8]

votantes = Votante(arreglo_votante)

for dni in votantes.dnis:
    print(dni)
