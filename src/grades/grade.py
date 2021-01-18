import users.connection as connection

conn = connection.conn()
db = conn[0]
cursor = conn[1]
class Grade:
    
    def __init__(self, userID, title, description):
        self.userID = userID
        self.title = title
        self.description = description

    def save(self):
        sql = "INSERT INTO grades VALUES(null, %s, %s, %s, NOW())"
        grade = (self.userID, self.title, self.description)

        cursor.execute(sql, grade)
        db.commit()

        return [cursor.rowcount, self]
    
    def select(self):
        sql = f"SELECT * FROM grades WHERE user_id = {self.userID}"

        cursor.execute(sql)
        result = cursor.fetchall()

        return result

    def delete(self):
        sql = f"DELETE FROM grades WHERE user_id = {self.userID} AND title LIKE '%{self.title}%'"

        cursor.execute(sql)
        db.commit()

        return [cursor.rowcount, self]
