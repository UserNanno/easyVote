# FUNCION PRINCIPAL DEL PROGRAMA QUE FUNCIONA EN BUCLE
from votante_manager import VotanteManager
import tkinter as tk
from tkinter import messagebox


class Login:
    def __init__(self):
        self.votos_manager = VotanteManager()
        self.root = tk.Tk()
        self.root.title("Voter Analyzer")

        self.label_dni = tk.Label(self.root, text="Dni:")
        self.label_dni.pack()
        self.entry_dni = tk.Entry(self.root)
        self.entry_dni.pack()

    def iniciar(self):
        self.votos_manager.llenar_tabla_hash()

        while True:
            # Reemplazar por el otro metodo de búsqueda
            if self.votos_manager.iniciar_sesion(self.entry_dni):

                print("Ingreso exitoso.")
                input("Presione Enter para continuar...")
                if self.votos_manager.validar_voto(self.entry_dni):

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
                        self.votos_manager.votar(
                            self.entry_dni, "Candidato "+voto.upper())

                        print("Voto registrado correctamente.")
                        input("Presione Enter para continuar...")
                    else:
                        print("Opción inválida. Intente nuevamente.")
                else:

                    print("Usted ya ha realizado su voto.")
                    input("Presione Enter para continuar...")
            else:

                print("Su DNI no está registrado.")
                input("Presione Enter para continuar...")

            pregunta = input("¿Desea salir? (S/N): ")
            if pregunta.upper() == "S":

                break
