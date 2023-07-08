import mysql.connector
from votante import Votante
from candidato import Candidato

class Database:
    def __init__(self, host, user, password, db):
        self.host = host
        self.user = user
        self.password = password
        self.db = db
        self.conn = None
        self.cursor = None

    def connect(self):
        try:
            self.conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                db=self.db
            )
            self.cursor = self.conn.cursor()
        except mysql.connector.Error as error:
            print("Error al conectarse a la base de datos:", error)

    def fetch_votantes(self, query):
        self.cursor.execute(query)
        resultados = self.cursor.fetchall()

        votantes = []
        for fila in resultados:
            votante = Votante(fila[0], fila[1], fila[2],
                              fila[3], fila[4], fila[5], fila[6])
            votantes.append(votante)

        return votantes
    
    def fetch_candidatos(self, query):
        self.cursor.execute(query)
        resultados = self.cursor.fetchall()

        candidatos = []
        for fila in resultados:
            candidato = Candidato(fila[0], fila[1], fila[2],fila[3])
            candidatos.append(candidato)

        return candidatos

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
