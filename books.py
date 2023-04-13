import json
import requests
import urllib

from config import getdb, closedb


def get_books(cur, page=1):
    url = "https://gutendex.com/"

    url += urllib.parse.urlencode({
        "page": page
    })

    res = requests.get(url)

    if res.status_code!= 200:
        print("error with request")
        return
    
    data = json.loads(res.text)
    for it in data["items"]:
        