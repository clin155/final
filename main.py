import json
import movie
import config
import pokemon
import dog

def main():
    conn = config.getdb()
    cur = conn.cursor()

    for i in range(1, 6):
        movie.moviedata(cur, i)

    pokemon.get_types(cur)
    j = 1
    for i in range(4):
        pokemon.getpokemon(cur, j, j+25)
        j += 25
    movie.get_genres(cur)
    for i in range(5):
        dog.get_dogs(cur, 20*i)
    config.closedb(conn)

    # put visualization functions here


if __name__ == "__main__":
    main()