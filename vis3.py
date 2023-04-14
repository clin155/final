import numpy as np
import matplotlib.pyplot as plt
import config

def genre_rev():
    conn = config.getdb()
    cur = conn.cursor()

    cur.execute('''
        SELECT g.name, AVG (m.rating) as avg_rating
        FROM genres g
        JOIN movies m on G.id = m.genre_id
        GROUP BY g.name
    ''')
    results = cur.fetchall()

    genres = [entry[0] for entry in results]
    avg_ratings = [entry[1] for entry in results]

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

    conn.close()

genre_rev()