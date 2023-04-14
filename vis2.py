import numpy as np
import matplotlib.pyplot as plt
import config
import sqlite3

def pokemon_pie():
    conn = config.getdb()
    cur = conn.cursor()

    cur.execute("SELECT type, COUNT(*) FROM pokemon GROUP BY type")
    data = cur.fetchall()
    types, counts = zip(*data)

    type_colors = {
        'bug': '#A6B91A',
        'dark': '#705746',
        'dragon': '#6F35FC',
        'electric': '#F7D02C',   
        'fairy': '#D685AD',
        'fighting': '#C22E28',
        'fire': '#EE8130',
        'flying': '#A98FF3',
        'ghost': '#735797',
        'grass': '#7AC74C',
        'ground': '#E2BF65',
        'ice': '#96D9D6',
        'normal': 'beige',
        'poison': '#A33EA1',
        'psychic': '#F95587',
        'rock': '#B6A136',
        'steel': '#B7B7CE',
        'water': '#6390F0'
    }

    colors = [type_colors[type] for type in types]

    plt.figure(figsize =(8,8))
    plt.pie(counts, labels=types, colors=colors, autopct='%1.1f%%', startangle=90)
    plt.axis('equal')
    plt.title('Pie Chart of Pokemon Types')
    plt.show()

    config.closedb(conn)

pokemon_pie()