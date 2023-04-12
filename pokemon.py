import json
import requests
import urllib

from collections import defaultdict
from config import getdb, closedb


def getpokemon(cur, st, end):
    
    for i in range(st, end):
        url = f'https://pokeapi.co/api/v2/pokemon/{i}/'

        r = requests.get(url)

        if r.status_code!= 200:
            print("bad status code")
            return
        
        data = json.loads(r.text)
        query = """
            INSERT INTO pokemon(id, name, height, weight, type, attack, defense, speed) VALUES 
            (?, ?, ?, ?, ?, ?, ?, ?)
        """

        cur.execute(query, (data['id'], data['name'], data['height'], data['weight'],
                            data['types'][0]['type']['name'],data['stats'][1]['base_stat'],
                            data['stats'][2]['base_stat'],data['stats'][5]['base_stat']))


if __name__ == "__main__":
    conn = getdb()
    cur = conn.cursor()
    getpokemon(cur, 1, 26)
    closedb(conn)