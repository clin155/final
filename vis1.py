import numpy as np
import matplotlib.pyplot as plt
import config
import sqlite3

def speed_weight():
    conn = config.getdb()
    cur = conn.cursor()

    cur.execute ("SELECT weight, speed FROM pokemon")
    results = cur.fetchall()

    weights = [entry[0] for entry in results]
    speeds = [entry[1] for entry in results]

    plt.scatter(weights, speeds)

    plt.xlabel('Weight')
    plt.ylabel('Speed')
    plt.title('Scatter Plot of Weight and Speed')

    plt.show()

    config.closedb(conn)

speed_weight()