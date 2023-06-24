from votantes_manager import VotantesManager
from candidatos_manager import CandidatosManager
from votos_manager import VotosManager

class EasyVoteApp:
    def __init__(self):
        self.votantes_manager = VotantesManager()
        self.candidatos_manager = CandidatosManager()
        self.votos_manager = VotosManager()

    def run(self):
        votante = self.iniciar_sesion()
        if votante is not None:
            self.votar(votante)

    def iniciar_sesion(self):
        username = input("Ingrese su nombre de usuario: ")
        password = input("Ingrese su contraseña: ")

        votante = self.votantes_manager.iniciar_sesion(username, password)
        if votante is None:
            print("Nombre de usuario o contraseña incorrectos.")
        return votante

    def votar(self, votante):
        if self.votos_manager.verificar_voto(votante):
            print("Usted ya ha emitido su voto.")
        else:
            candidatos = self.candidatos_manager.obtener_candidatos()
            self.mostrar_candidatos(candidatos)

            candidato_id = input("Ingrese el ID del candidato al que desea votar: ")

            if self.candidatos_manager.validar_candidato(candidato_id, candidatos):
                self.votos_manager.registrar_voto(votante, candidato_id)
                print("¡Voto registrado con éxito!")
            else:
                print("ID de candidato inválido.")

    def mostrar_candidatos(self, candidatos):
        print("Opciones de candidatos:")
        for candidato in candidatos:
            print(f"ID: {candidato.id}, Nombre: {candidato.nombre}, Partido: {candidato.partido}")
