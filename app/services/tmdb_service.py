
import requests

API_READ_ACCESS_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmZDZkMWIxNjc5NzcxYzc2YzM5NTkxZTJlMTE3ZjkzZSIsIm5iZiI6MTczNDgwMTA0OS45NjEsInN1YiI6IjY3NjZmNjk5NjdkZjg2ZDk4NDc0OGQwNiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.2pYaxaKqBNO2EAJHHOAowa9A4nEHz40u3vOC7riheDg"
BASE_URL = "https://api.themoviedb.org/3"

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
