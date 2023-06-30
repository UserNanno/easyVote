import mysql.connector

class DatabaseManager:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="easyVote"
        )
        self.cursor = self.db.cursor()

    def execute_query(self, query, params=None):
        if params is None:
            self.cursor.execute(query)
        else:
            self.cursor.execute(query, params)
        result = self.cursor.fetchall()
        return result

    def commit(self):
        self.db.commit()

    def close(self):
        self.cursor.close()
        self.db.close()
