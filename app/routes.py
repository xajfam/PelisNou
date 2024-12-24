
from flask import Blueprint, render_template, request
from .services.tmdb_service import get_genres, get_movies_by_genre

bp = Blueprint('main', __name__)

@bp.route('/', methods=['GET', 'POST'])
def home():
    genre_name = None
    movies = []
    
    if request.method == 'POST':
        genre_id = request.form.get('genre')
        genre_name = request.form.get('genre_name')  # Captura el nom del gènere
        if genre_id:
            movies = get_movies_by_genre(genre_id)
        else:
            movies = get_movies_by_genre()

        
    
    genres = get_genres()
    return render_template('index.html', genres=genres, movies=movies, genre_name=genre_name)

