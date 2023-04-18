import click
import dog
import pokemon
import movie
import config
import config


@click.command()
@click.argument('datatype', type=str, required=True)
@click.option('--table', '-t', default=None, type=str, help='movie->(default movie, genre), pokemon->(default pokemon, type), dog -> no tables')
@click.option('--page', '-p', default=1, type=int, help='default 1, can go up to 5')
def main(datatype, table, page):
    '''pulls 20 entries from the database, page and table can be specified'''
    conn = config.getdb()
    cur = conn.cursor()

    if datatype.lower() == 'dog':
        dog.get_dogs(cur, 29*(page - 1))
    elif datatype.lower() == 'pokemon':
        if table == None or table == 'pokemon':
            pokemon.getpokemon(cur, (page-1)*20 + 1, (page * 20)+1)
        elif table == 'type':
            pokemon.get_types(cur)
        else:
            print("not a valid table")
    elif datatype.lower() == 'movie':
        if table == None or table == 'movie':
            movie.moviedata(cur, page)
        elif table == 'genre':
            movie.get_genres(cur)
        else:
            print("not a valid table")
    else:
        print("not a valid datatype")
    config.closedb(conn)

if __name__ == '__main__':
    main()