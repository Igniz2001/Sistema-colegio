import mysql.connector
class Database:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host = "localhost",
            user="root",
            password="",
            database="colegio"
        )
        self.cursor=self.connection.cursor()