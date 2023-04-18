import json
import config
import movie
import pokemon
import dog
import visrunnner

def main():
    conn = config.getdb()
    cur = conn.cursor()
    
    cur.execute("SELECT COUNT(*) FROM pokemon")
    page_count = cur.fetchone()[0]
    poke_page = (page_count // 20) + 1
    movie_page = (page_count // 20) + 1
    dog_page = (29*(page_count - 1))


    dog.get_dogs(cur, 29 * dog_page)
    pokemon.getpokemon(cur, (poke_page-1)*20+1, poke_page *20+1)
    pokemon.get_types(cur)
    movie.moviedata(cur, movie_page)
    movie.get_genres(cur)

    config.closedb(conn)

if __name__ == "__main__":
    main()