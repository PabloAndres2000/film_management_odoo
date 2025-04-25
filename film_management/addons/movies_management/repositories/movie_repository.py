from odoo.http import request


class MovieRepository:

    @staticmethod
    def get_top_movies(limit=10):
        """
        Retorna las películas ordenadas por ranking descendente.
        """
        return request.env['movie.movie'].sudo().search([], order='ranking desc', limit=limit)