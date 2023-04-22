import json
import config
import movie
import pokemon
import dog

def main():
    conn = config.getdb()
    cur = conn.cursor()
    with open('schema.sql') as f:
        query = f.read()

        cur.executescript(query)
    helper(cur)
    config.closedb(conn)



def helper(cur):
    cur.execute("SELECT COUNT(*) FROM pokemon")
    page_count = cur.fetchone()[0]
    page = (page_count // 20)

    if page < 5:
        pokemon.getpokemon(cur, (page)*20+1, (page+1) *20+1)
        return

    cur.execute("SELECT COUNT(*) FROM type")
    page_count = cur.fetchone()[0]

    if page_count == 0:
        pokemon.get_types(cur)
        return
    
    cur.execute("SELECT COUNT(*) FROM dogs")
    page_count = cur.fetchone()[0]
    page = (page_count // 20)
    if page < 5:
        dog.get_dogs(cur, (20*page))
        return
    
    cur.execute("SELECT COUNT(*) FROM movies")
    page_count = cur.fetchone()[0]
    page = (page_count // 20)

    if page < 5:
        movie.moviedata(cur, page+1)
        return

    cur.execute("SELECT COUNT(*) FROM genres")
    page_count = cur.fetchone()[0]
    if page_count == 0:

        movie.get_genres(cur)
        return

    print("No data left to retrieve")
if __name__ == "__main__":
    main()