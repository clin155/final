import json
import data
import config


def main():
    conn = config.getdb()
    cur = conn.cursor()
    data.moviedata(cur)

    config.closedb(conn)