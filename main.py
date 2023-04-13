import json
import movie
import config
import pokemon

def main():
    conn = config.getdb()
    cur = conn.cursor()

    for i in range(1, 6):
        movie.moviedata(cur, i)
    
    j = 1
    for i in range(4):
        pokemon.getpokemon(cur, j, j+25)
        j += 25
    movie.get_genres(cur)
    config.closedb(conn)
if __name__ == "__main__":
    main()