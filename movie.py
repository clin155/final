import json
import requests
import urllib

from config import getdb, closedb
MOVIEKEY = "0d615c57fb35d0bf9fbfdddd23fd2b92"

def moviedata(cur, page):
    
    #20 results per page (pages start at 1)
    # companies_dict = defaultdict(lambda: {})
    url = "https://api.themoviedb.org/3/movie/popular?"
    url += urllib.parse.urlencode({
        "api_key": MOVIEKEY,
        "page": page
    })

    response = requests.get(url)
    if response.status_code == 200:

        data = json.loads(response.text)

        for it in data["results"]:
            url = f"https://api.themoviedb.org/3/movie/{it['id']}?"
            url = url + urllib.parse.urlencode({
                "api_key": MOVIEKEY
            })
            response = requests.get(url)
            if response.status_code != 200:
                print("Request failed movie details")
                return
            data2 = json.loads(response.text)
            
            if "release_date" not in it:
                it["release_date"] = None

            cur.execute("""
            INSERT INTO movies(id, title, genre_id, popularity, rating, release_date, revenue) 
            VALUES (?,?,?,?,?,?,?)""", (it["id"], it["title"], it["genre_ids"][0], it["popularity"], 
            it["vote_average"], it["release_date"], data2["revenue"]))
            # for val in data2["production_companies"]:
            #     cur.execute("""INSERT INTO 
            #     company_to_movie(movie_id, company_id) VALUES (?,?)""", (it["id"],val['id']))
            #     companies_dict[val['id']]['name'] = val['name']
            #     companies_dict[val['id']]['country'] = val['origin_country']
    else:
        print("Request failed")
        return
    
    # for key,val in companies_dict.items():
    #     cur.execute("""INSERT INTO 
    #     companies(id, name, country) VALUES (?,?,?)""", (key,val['name'], val['country']))
    print("data created")


def get_genres(cur):
    url = "https://api.themoviedb.org/3/genre/movie/list?"
    url += urllib.parse.urlencode({
        "api_key": MOVIEKEY
    })
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.text)
        for it in data["genres"]:
            cur.execute("""INSERT INTO genres(id, name) VALUES (?,?)""", (it["id"], it["name"]))
        print("genres created")
    else:
        print("Request failed")
        return


if __name__ == "__main__":
    conn = getdb()
    cur = conn.cursor()
    get_genres(cur)
    closedb(conn)

