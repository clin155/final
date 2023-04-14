import numpy as np
import matplotlib.pyplot as plt
import config
import sqlite3

def genre_rev():
    conn = config.getdb()
    cur = conn.cursor()

    cur.execute('''
        SELECT g.name, AVG 
    ''')