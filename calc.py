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

    with open("calc.txt", "a") as file:
        file.write ("Average Rating of Each Genre\n\n")
        for genre, avg_rating in results:
            file.write(f"Average rating for {genre} films: {avg_rating: .2}\n")

    config.closedb(conn)

def avg_stats_by_type():
    conn = config.getdb()
    cur = conn.cursor()

    cur.execute('''
        SELECT t.type, AVG(p.attack) as avg_attack, AVG(p.defense) as avg_defense, AVG(p.speed) as avg_speed
        FROM pokemon p
        JOIN type t on p.type_id = t.id
        GROUP BY t.type
    ''')
    results = cur.fetchall()

    with open("calc.txt", "a") as file:
        file.write("\n\nAverage Stats for Each Pokemon Type\n\n")
        for _type, avg_attack, avg_defense, avg_speed in results:
            file.write(f"Average stats for {_type} pokemon: Attack {avg_attack:.2f}, Defense {avg_defense:.2f}, Speed {avg_speed:.2f}\n")

    config.closedb(conn)

def avg_weight_by_energy():
    conn = config.getdb()
    cur = conn.cursor()

    cur.execute('''
        SELECT energy, AVG(weight) as avg_weight
        FROM dogs
        GROUP BY energy
    ''')
    results = cur.fetchall()

    with open ("calc.txt", "a") as file:
        file.write("\n\nAverage Weight for Each Dog Energy Levl\n\n")
        for energy, avg_weight in results:
            file.write(f"Average weight for dogs with energy {energy}: {avg_weight:.2f}\n")
    
    config.closedb(conn)

if __name__ == "__main__":
    avg_rating_by_genre()
    avg_stats_by_type()
    avg_weight_by_energy()