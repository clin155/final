import json
import requests
import urllib

from collections import defaultdict
from config import getdb, closedb


TYPES = {
    "Bug": 1,
    "Dark": 2,
    "Dragon": 3,
    "Electric": 4,
    "Fairy": 5,
    "Fighting": 6,
    "Fire": 7,
    "Flying": 8,
    "Ghost": 9,
    "Grass": 10,
    "Ground": 11,
    "Ice": 12,
    "Normal": 13,
    "Poison": 14,
    "Psychic": 15,
    "Rock": 16,
    "Steel": 17,
    "Water": 18,
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
    print ("20 pokemon added")


def get_types(cur):
    for type, id in TYPES.items():
        cur.execute("""
        INSERT INTO type (id, type) VALUES (?, ?)
        """, (id, type))
    print ("types created")


if __name__ == "__main__":
    conn = getdb()
    cur = conn.cursor()
    getpokemon(cur, 1, 26)
    closedb(conn)