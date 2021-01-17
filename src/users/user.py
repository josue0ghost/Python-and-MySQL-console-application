import datetime
import hashlib
import users.connection as connection

conn = connection.conn()
db = conn[0]
cursor = conn[1]

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
        # query
        sql = "SELECT * FROM users WHERE email = %s AND password = %s"

        # Ciph
        cipher = hashlib.sha256()
        cipher.update(self.password.encode('utf8'))

        # data for query
        user = (self.email, cipher.hexdigest())

        cursor.execute(sql, user)        
        result = cursor.fetchone()

        return result