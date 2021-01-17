import mysql.connector

def conn():
    
    db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "",
        database = "pythondb",
        port = 3306
    )
    cursor = db.cursor() # optional parameter: buffered=True 

    return [db, cursor]