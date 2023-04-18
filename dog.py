import json
import requests
import urllib

from config import getdb, closedb

APIKEY = "igOKfSigz0qT9h1c1wHM2Q==Ee81Du0GLxW0swrY"

def get_dogs(cur, offset):
    url = "https://api.api-ninjas.com/v1/dogs?"

    url += urllib.parse.urlencode({
        "offset": offset,
        "min_height": 24
    })

    res = requests.get(url, headers={'X-Api-Key': APIKEY})

    if res.status_code!= 200:
        print("error with request")
        return
    
    data = json.loads(res.text)
    for it in list(data):
        cur.execute("""INSERT INTO dogs (name, energy, barking, 
        weight, height) VALUES (?,?,?,?,?)""", (it["name"], it["energy"], it["barking"], 
        (it["max_weight_male"] + it["max_weight_female"])/2, (it["max_height_male"] + it["max_height_female"])/2))

    print("20 dogs added")


if __name__ == "__main__":
    get_dogs()