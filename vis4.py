import numpy as np
import matplotlib.pyplot as plt
import config

color_dict = {'Adventure': 'red', 'Fantasy': 'blue', 'Animation': 'green', 'Drama': 'orange', 'Horror': 'purple', 'Action': 'yellow', 'Comedy': 'pink', 'History': 'gray', 'Western': 'brown', 'Thriller': 'teal', 'Crime': 'olive', 'Documentary': 'gold', 'Science Fiction': 'magenta', 'Mystery': 'navy', 'Music': 'maroon', 'Romance': 'indigo', 'Family': 'lime', 'War': 'khaki', 'TV Movie': 'coral'}

def pop_vs_rating():
    conn = config.getdb()
    cur = conn.cursor()

    cur.execute("SELECT movies.popularity, movies.rating, genres.name FROM movies INNER JOIN genres ON movies.genre_id = genres.id")
    data = cur.fetchall()
    popularity, rating, genres = zip(*data)

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

if __name__ == "__main__":
    pop_vs_rating()