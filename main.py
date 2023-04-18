import json
import movie
import config
import pokemon
import dog
import visrunnner

def main():
    conn = config.getdb()
    cur = conn.cursor()

    for i in range(1, 6):
        movie.moviedata(cur, i)

    pokemon.get_types(cur)
    j = 1
    for i in range(6):
        pokemon.getpokemon(cur, j, j+20)
        j += 20
    movie.get_genres(cur)
    for i in range(5):
        dog.get_dogs(cur, 20*i)

    config.closedb(conn)
    visrunnner.visrunner()

if __name__ == "__main__":
    main()