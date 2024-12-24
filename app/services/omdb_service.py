import requests

API_READ_ACCESS_TOKEN = "4f9f28b9"
BASE_URL = "https://www.omdbapi.com"

def get_genres():
    url = f"{BASE_URL}/genre/movie/list"
    headers = {"Authorization": f"Bearer {API_READ_ACCESS_TOKEN}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get("genres", [])
    return []

def get_movies_by_genre(genre_id=None):
    if genre_id:
        # Busca pel·lícules del gènere específic
        url = f"https://api.themoviedb.org/3/discover/movie?with_genres={genre_id}&sort_by=vote_average.desc"
    else:
        # Busca pel·lícules sense filtrar per gènere
        url = "https://api.themoviedb.org/3/discover/movie?sort_by=vote_average.desc"
    params = {
        "with_genres": genre_id,
        "primary_release_date.gte": "2016-01-01",
        "vote_average.gte": 6,
        "vote_count.gte": 200,
        "sort_by": "vote_average.desc",
        "language": "en-US"
    }
    headers = {"Authorization": f"Bearer {API_READ_ACCESS_TOKEN}"}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json().get("results", [])
    return []



#test --> http://www.omdbapi.com/?i=tt3896198&apikey=4f9f28b9&type=series