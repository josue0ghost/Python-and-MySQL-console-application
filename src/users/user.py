import mysql.connector
import datetime

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "pythondb",
    port = 3306
)
cursor = db.cursor() # optional parameter: buffered=True 

class User:
    def __init__(self, name, lastname, email, password):
        self.name = name
        self.lastname = lastname
        self.email = email
        self.password = password
    
    def register(self):
        sql = "INSERT INTO users VALUES(null, %s, %s, %s, %s, %s)"
        user = (self.name, self.lastname, self.email, self.password, datetime.date.today())

        cursor.execute(sql, user)
        db.commit()

        return [cursor.rowcount, self]

    def identify(self):
        return self.name