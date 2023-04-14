import numpy as np
import matplotlib.pyplot as plt
import config

def avg_rating_by_genre():
    conn = config.getdb()
    cur = conn.cursor()

    cur.execute('''
        SELECT g.name, AVG(m.rating) as avg_rating
        FROM genres g
        JOIN movies m ON g.id = m.genre_id
        GROUP BY g.name
    ''')
    results = cur.fetchall()

    with open("avg_rating_by_genre.txt", "w") as file:
        for genre, avg_rating in results:
            file.write(f"Average rating for {genre}: {avg_rating: .2}\n")

    config.closedb(conn)

avg_rating_by_genre()

def avg_stats_by_type():
    conn = config.getdb()
    cur = conn.cursor()

    cur.execute('''
        SELECT type, AVG(attack) as avg_attack, AVG(defense) as avg_defense, AVG(speed) as avg_speed
        FROM pokemon
        GROUP BY type
    ''')
    results = cur.fetchall()

    with open("avg_stats_by_type.txt", "w") as file:
        for _type, avg_attack, avg_defense, avg_speed in results:
            file.write(f"Average stats for {_type} Pokemon: Attack {avg_attack:.2f}, Defense {avg_defense:.2f}, Speed {avg_speed:.2f}\n")

    config.closedb(conn)

avg_stats_by_type()

def avg_bark_by_energy():
    conn = config.getdb()
    cur = conn.cursor()

    cur.execute('''
        SELECT energy, AVG(barking) as avg_barking
        FROM dogs
        GROUP BY energy
    ''')
    results = cur.fetchall()

    with open ("avg_bark_by_energy.text", "w") as file:
        for energy, avg_barking in results:
            file.write(f"Average barking level for dogs with energy {energy}: {avg_barking:.2f}\n")
    
    config.closedb(conn)

avg_bark_by_energy()