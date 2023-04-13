import json
import movie
import config
import pokemon


def main():
    conn = config.getdb()
    cur = conn.cursor()

    for i in range(1, 6):
        movie.moviedata(cur, 1)
    movie.get_genres

    j = 1

    for i in range (4):
        pokemon.pokemondata(cur, j, j+25)
        j += 25
    pokemon.getpokemon
    config.closedb(conn)