import numpy as np
import matplotlib.pyplot as plt
import config

def pokemon_pie():
    conn = config.getdb()
    cur = conn.cursor()

    cur.execute('''
        SELECT t.type, COUNT (p.id) as count
        FROM pokemon p
        JOIN type t on p.type_id = t.id
        GROUP BY t.type
    ''')
    data = cur.fetchall()
    types, counts = zip(*data)

    type_colors = {
        'Bug': '#A6B91A',
        'Dark': '#705746',
        'Dragon': '#6F35FC',
        'Electric': '#F7D02C',   
        'Fairy': '#D685AD',
        'Fighting': '#C22E28',
        'Fire': '#EE8130',
        'Flying': '#A98FF3',
        'Ghost': '#735797',
        'Grass': '#7AC74C',
        'Ground': '#E2BF65',
        'Ice': '#96D9D6',
        'Normal': 'beige',
        'Poison': '#A33EA1',
        'Psychic': '#F95587',
        'Rock': '#B6A136',
        'Steel': '#B7B7CE',
        'Water': '#6390F0'
    }

    colors = [type_colors[type] for type in types]

    plt.figure(figsize =(8,8))
    plt.pie(counts, labels=types, colors=colors, autopct='%1.1f%%', startangle=90)
    plt.axis('equal')
    plt.title('Pie Chart of Pokemon Types')
    plt.show()

    config.closedb(conn)

if __name__ == "__main__":
    pokemon_pie()