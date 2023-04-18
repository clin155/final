import numpy as np
import matplotlib.pyplot as plt
import config

#calc 1
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

#calc 2
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

#calc 3
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

#vis 1
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

#vis 2
def pokemon_radar():
    conn = config.getdb()
    cur = conn.cursor()

    cur.execute('''
        SELECT t.type, AVG (p.attack) as avg_attack, AVG (p.defense) as avg_defense, AVG (p.speed) as avg_speed
        FROM pokemon p
        JOIN type t on p.type_id = t.id
        GROUP BY t.type
    ''')
    data = cur.fetchall()
    
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

    angles = np.linspace(0, 2 * np.pi, 3, endpoint=False).tolist()
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

    for row in data:
        _type, attack, defense, speed = row
        color = type_colors[_type]
        values = [attack, defense, speed, attack]
        ax.plot(angles + [angles[0]], values, label=_type, color=color)

    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    ax.set_thetagrids(np.degrees(angles), labels=['Attack', 'Defense', 'Speed'])

    ax.set_rlabel_position(180 / len(data))
    plt.ylim(0, max(max([d[1] for d in data]), max([d[2] for d in data]), max([d[3] for d in data])))

    ax.legend(loc='upper right', bbox_to_anchor=(1, 1))
    plt.title("Radar Plot of Pokemon Types' Average Attack, Defense, and Speed")
    plt.show()

    config.closedb(conn)

#vis 3
def genre_rat():
    conn = config.getdb()
    cur = conn.cursor()

    cur.execute('''
        SELECT g.name, AVG (m.rating) as avg_rating
        FROM genres g
        JOIN movies m on G.id = m.genre_id
        GROUP BY g.name
    ''')
    data = cur.fetchall()

    genres = [entry[0] for entry in data]
    avg_ratings = [entry[1] for entry in data]

    color_dict = {'Adventure': 'red', 'Fantasy': 'skyblue', 'Animation': 'green', 'Drama': 'orange', 'Horror': 'purple', 'Action': 'yellow', 'Comedy': 'pink', 'History': 'gray', 'Western': 'brown', 'Thriller': 'teal', 'Crime': 'olive', 'Documentary': 'gold', 'Science Fiction': 'magenta', 'Mystery': 'navy', 'Music': 'maroon', 'Romance': 'indigo', 'Family': 'lime', 'War': 'khaki', 'TV Movie': 'coral'}
    colors = [color_dict[genre] for genre in genres]

    plt.figure(figsize=(14,6))
    plt.bar(genres, avg_ratings, color=colors)

    plt.title('Average Rating by Genre')
    plt.xlabel('Genres')
    plt.ylabel('Average Rating')
    plt.ylim(top=10)

    plt.xticks(rotation=45)
    plt.show()

    config.closedb(conn)

#vis 4
def pop_vs_rating():
    conn = config.getdb()
    cur = conn.cursor()

    cur.execute('''
        SELECT movies.popularity, movies.rating, genres.name 
        FROM movies
        INNER JOIN genres
        ON movies.genre_id = genres.id''')
    data = cur.fetchall()
    popularity, rating, genres = zip(*data)

    color_dict = {'Adventure': 'red', 'Fantasy': 'blue', 'Animation': 'green', 'Drama': 'orange', 'Horror': 'purple', 'Action': 'yellow', 'Comedy': 'pink', 'History': 'gray', 'Western': 'brown', 'Thriller': 'teal', 'Crime': 'olive', 'Documentary': 'gold', 'Science Fiction': 'magenta', 'Mystery': 'navy', 'Music': 'maroon', 'Romance': 'indigo', 'Family': 'lime', 'War': 'khaki', 'TV Movie': 'coral'}
    fig, ax = plt.subplots()

    for genre, color in color_dict.items():
        genre_popularity = [pop for pop, gen in zip(popularity, genres) if gen == genre]
        genre_rating = [rat for rat, gen in zip(rating, genres) if gen == genre]
        ax.scatter(genre_popularity, genre_rating, c=color, label=genre, edgecolor='black', alpha=0.7)

    plt.xlabel('Popularity')
    plt.ylabel('Rating')
    plt.title('Popularity vs Rating (Color by Genre)')

    ax.legend(loc='upper left', bbox_to_anchor=(1.05, 1), title='Genres')
    plt.tight_layout()

    plt.show()

    config.closedb(conn)

#vis 5
def weight_vs_energy():
    conn = config.getdb()
    cur = conn.cursor()

    cur.execute("SELECT energy, weight FROM dogs")
    data = cur.fetchall()
    energy_levels = sorted(set(entry[0] for entry in data))

    weights_by_energy = [[] for _ in range(len(energy_levels))]
    for energy, weight in data:
        index = energy_levels.index(energy)
        weights_by_energy[index].append(weight)

    plt.boxplot(weights_by_energy, labels = energy_levels)
    plt.xlabel('Energy Level')
    plt.ylabel('Weight')
    plt.title('Box Plot of Dog Weights by Energy Level')
    plt.show()
    
    config.closedb(conn)

if __name__ == "__main__":
    avg_rating_by_genre()
    avg_stats_by_type()
    avg_weight_by_energy()
    pokemon_pie()
    pokemon_radar()
    genre_rat()
    pop_vs_rating()
    weight_vs_energy()
