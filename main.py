import json
import movie
import config
import pokemon
import dog
import vis1
import vis2
import vis3
import vis4
import vis5

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
    
    vis1.speed_vs_weight()
    vis2.pokemon_pie()
    vis3.genre_rev()
    vis4.pop_vs_rating()
    vis5.weight_vs_energy()


    config.closedb(conn)

    # put visualization functions here


if __name__ == "__main__":
    main()