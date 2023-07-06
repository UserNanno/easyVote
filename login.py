#FUNCION PRINCIPAL DEL PROGRAMA QUE FUNCIONA EN BUCLE
from votante_manager import VotanteManager
import os

class Login:
    def __init__(self):
        self.votos_manager = VotanteManager()

    def limpiar_pantalla(self):
        # Limpia la pantalla de la consola
        os.system('cls' if os.name == 'nt' else 'clear')

    def iniciar(self):
        self.votos_manager.llenar_tabla_hash()

        while True:
            self.limpiar_pantalla()

            dni = input("Ingrese su DNI: ")

            if self.votos_manager.iniciar_sesion(dni): #Reemplazar por el otro metodo de búsqueda
                self.limpiar_pantalla()
                print("Ingreso exitoso.")
                input("Presione Enter para continuar...")
                if self.votos_manager.validar_voto(dni):
                    self.limpiar_pantalla()
                    print("Usted aún no ha realizado su voto.")
                    print("Candidatos:")
                    print("A) Candidato A")
                    print("B) Candidato B")
                    print("B) Candidato C")
                    print("B) Candidato D")
                    print("B) Candidato E")
                    print("B) Candidato F")
                    print("B) Candidato G")
                    print("B) Candidato H")
                    print("B) Candidato I")
                    print("B) Candidato J")

                    voto = input("Seleccione el candidato (A-J): ")

                    if voto.upper() in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']:
                        self.votos_manager.votar(dni, "Candidato "+voto.upper())
                        self.limpiar_pantalla()
                        print("Voto registrado correctamente.")
                        input("Presione Enter para continuar...")
                    else:
                        print("Opción inválida. Intente nuevamente.")
                else:
                    self.limpiar_pantalla()
                    print("Usted ya ha realizado su voto.")
                    input("Presione Enter para continuar...")
            else:
                self.limpiar_pantalla()
                print("Su DNI no está registrado.")
                input("Presione Enter para continuar...")

            pregunta = input("¿Desea salir? (S/N): ")
            if pregunta.upper() == "S":
                self.limpiar_pantalla()
                break