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
    
    def contar_votos_por_candidato_en_region(self, region):
        votos_por_candidato_en_region = {}

        for persona in self.personas:
            if persona.region == region:
                candidato = persona.voto

                if candidato in votos_por_candidato_en_region:
                    votos_por_candidato_en_region[candidato] += 1
                else:
                    votos_por_candidato_en_region[candidato] = 1

        return votos_por_candidato_en_region
    
    def contar_votos_por_candidato_en_genero(self, genero):
        votos_por_candidato_en_genero = {}

        for persona in self.personas:
            if persona.genero == genero:
                candidato = persona.voto

                if candidato in votos_por_candidato_en_genero:
                    votos_por_candidato_en_genero[candidato] += 1
                else:
                    votos_por_candidato_en_genero[candidato] = 1

        return votos_por_candidato_en_genero
