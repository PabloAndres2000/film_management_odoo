from odoo import http
from odoo.http import request
import json
from ..repositories.movie_repository import MovieRepository

class MovieController(http.Controller):

    @http.route('/api/top_movies', type='http', auth='public', methods=['GET'], csrf=False)
    def get_top_movies(self):
        movies = MovieRepository.get_top_movies()

        result = [
            {
                'id': movie.id,
                'title': movie.title,
                'ranking': movie.ranking,
            }
            for movie in movies
        ]

        return request.make_response(
            json.dumps(result),
            headers=[('Content-Type', 'application/json')]
        )
