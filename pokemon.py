import json
import requests
import urllib

from collections import defaultdict
from config import getdb, closedb


TYPES = {
    "Fire": 1,
    "Grass": 2,
    "Water": 3,
    "Electric": 4,
    "Ground": 5,
    "Rock": 6,
    "Fighting": 7,
    "Normal": 8,
    "Ghost": 9,
    "Psychic": 10,
    "Flying": 11,
    "Poison": 12,
    "Ice": 13,
    "Dragon": 14,
    "Bug": 15,
    "Fairy": 16,
}

def getpokemon(cur, st, end):
    
    for i in range(st, end):
        url = f'https://pokeapi.co/api/v2/pokemon/{i}/'

        r = requests.get(url)

        if r.status_code!= 200:
            print("bad status code")
            return
        
        data = json.loads(r.text)
        poke_type = data['types'][0]['type']['name'].capitalize()
        type_id = TYPES[poke_type]
        query = """
            INSERT INTO pokemon(id, name, height, weight, type_id, attack, defense, speed) VALUES 
            (?, ?, ?, ?, ?, ?, ?, ?)
        """

        cur.execute(query, (data['id'], data['name'], data['height'], data['weight'],
                            type_id, data['stats'][1]['base_stat'],
                            data['stats'][2]['base_stat'],data['stats'][5]['base_stat']))


def get_types(cur):
    for type, id in TYPES.items():
        cur.execute("""
        INSERT INTO type (id, type) VALUES (?, ?)
        """, (id, type))


if __name__ == "__main__":
    conn = getdb()
    cur = conn.cursor()
    getpokemon(cur, 1, 26)
    closedb(conn)