import sqlite3

def getdb():
    conn = sqlite3.connect("database.sqlite3")
    
    return conn

def closedb(conn):
    if conn is not None:
        conn.commit()
        conn.close()