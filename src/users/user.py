import mysql.connector
import datetime
import hashlib

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

        # Ciph
        cipher = hashlib.sha256()
        cipher.update(self.password.encode('utf8'))

        user = (self.name, self.lastname, self.email, cipher.hexdigest(), datetime.date.today())

        try:
            cursor.execute(sql, user)
            db.commit()
            result = [cursor.rowcount, self]
        except:
            result = [0, self]

        return result

    def identify(self):
        return self.name