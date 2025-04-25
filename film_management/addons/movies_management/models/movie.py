# film_management/addons/movies_management/models/movie.py
from odoo import models, fields, api
import requests
import logging

_logger = logging.getLogger(__name__)

class Movie(models.Model):
    _name = 'movie.movie'
    _description = 'Movie'
    
    title = fields.Char(string='Title', required=True)
    ranking = fields.Float(string='Ranking', digits=(3, 1)) 
    last_update = fields.Datetime(string='Last Update', default=fields.Datetime.now)
    api_data = fields.Text(string='Raw API Data')
    
    @api.model
    def fetch_movie_from_api(self):
        """Cron job mejorado con manejo de errores y validación"""
        settings = self.env['movie.api.settings'].search([], limit=1)
        if not settings:
            _logger.error("Configuración de API no encontrada en movie.api.settings")
            return False

        api_url = settings.get_api_url()
        if not api_url:
            _logger.error("URL de API no configurada")
            return False

        try:
            response = requests.get(api_url, timeout=10)
            response.raise_for_status() 
            
            movie_data = response.json()

            title = movie_data.get('movie_title')
            ranking = movie_data.get('ranking_movie', 0)

            if not title:
                _logger.error("La API no devolvió título de película: %s", movie_data)
                return False

            try:
                ranking = float(ranking)
            except (TypeError, ValueError):
                _logger.error("Ranking inválido: %s", ranking)
                ranking = 0.0

            _logger.info("DEBUG - Ranking convertido a float: %.1f", ranking)

            movie = self.create({
                'title': title,
                'ranking': ranking,
                'last_update': fields.Datetime.now(),
                'api_data': str(movie_data)
            })

            _logger.info("Película creada: %s (Ranking: %.1f)", movie.title, movie.ranking)
            return True
            
        except requests.exceptions.RequestException as e:
            _logger.error("Error de conexión con la API %s: %s", api_url, str(e))
        except ValueError as e:
            _logger.error("Error procesando datos JSON: %s", str(e))
        except Exception as e:
            _logger.exception("Error inesperado en fetch_movie_from_api: %s", str(e))
            
        return False