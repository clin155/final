import click
import dog
import pokemon
import movie
import config
import config


@click.command()
@click.argument('datatype', type=str, required=True)
@click.option('--table', '-t', default=None, type=str)
@click.option('--page', '-p', default=1, type=int)
def main(datatype, table, page):
    conn = config.getdb()
    cur = conn.cursor()

    if datatype.lower() == 'dog':
        dog.get_dogs(cur, 29*(page - 1))
    elif datatype.lower() == 'pokemon':
        if table == None:
            pokemon.getpokemon(cur, (page-1)*20 + 1, (page * 20)+1)
        elif table == 'type':
            pokemon.get_types(cur)
        else:
            print("not a valid table")
    elif datatype.lower() == 'movie':
        if table == None:
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