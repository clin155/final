import json
import movie
import config


def main():
    conn = config.getdb()
    cur = conn.cursor()
    movie.moviedata(cur)

    config.closedb(conn)