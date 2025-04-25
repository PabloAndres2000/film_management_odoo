# film_management/addons/movies_management/models/movie_api_settings.py
from odoo import models, fields
import requests
import logging
import os

from dotenv import load_dotenv

# Cargar variables desde el archivo .env
load_dotenv()

_logger = logging.getLogger(__name__)

class MovieApiSettings(models.Model):
    _name = 'movie.api.settings'
    _description = 'Movie API Settings'
    
    api_url = fields.Char(
        string='API URL',
        default=lambda self: os.getenv('MOVIE_API_URL', ''),
        required=True
    )
    
    api_key = fields.Char(
        string='API Key',
        default=lambda self: os.getenv('MOVIE_API_KEY', ''),
        required=True
    )
    
    # Campos modificados
    test_success = fields.Boolean(string="Test Success", default=False)
    test_message = fields.Text(string="Test Message") 
    test_failed = fields.Boolean(string="Test Failed", default=False) 
    
    def get_api_url(self):
        url = self.env['ir.config_parameter'].sudo().get_param(
            'movie.api_url', 
            self.api_url
        )
        _logger.info(f"[MovieApiSettings] Obteniendo API URL: {url}")
        return url
    
    def get_api_key(self):
        key = self.api_key
        _logger.info(f"[MovieApiSettings] Obteniendo API KEY: {key}")
        return key
   
    def test_api_connection(self):
        """Prueba simplificada de conexión con la API"""
        self.ensure_one()
        
        # Resetear estados
        self.write({
            'test_success': False,
            'test_failed': False,
            'test_message': "Probando conexión..."
        })
        
        api_url = self.get_api_url()
        
        if not api_url.startswith(('http://', 'https://')):
            return self._show_error("URL debe comenzar con http:// o https://")
        
        try:
            _logger.info(f"[MovieApiSettings] Probando conexión con: {api_url}")
            response = requests.get(api_url, timeout=5)
            response.raise_for_status()
            _logger.info(f"[MovieApiSettings] Conexión exitosa con código {response.status_code}")
            return self._show_success("✅ Conexión exitosa")
        
        except requests.exceptions.ConnectionError as ce:
            _logger.error(f"[MovieApiSettings] Error de conexión: {ce}")
            return self._show_error(f"No se pudo conectar a: {api_url.split('/')[2]}")
        except requests.exceptions.Timeout as te:
            _logger.error(f"[MovieApiSettings] Timeout: {te}")
            return self._show_error("Tiempo de espera agotado")
        except Exception as e:
            _logger.exception(f"[MovieApiSettings] Error inesperado: {e}")
            return self._show_error(f"Error inesperado: {str(e)}")

    def _show_success(self, message):
        """Muestra mensaje de éxito"""
        _logger.info(f"[MovieApiSettings] ✅ {message}")
        self.write({
            'test_success': True,
            'test_message': message
        })
        return self._show_notification("✅ Éxito", message, "success")

    def _show_error(self, message):
        """Muestra mensaje de error"""
        _logger.warning(f"[MovieApiSettings] ❌ {message}")
        self.write({
            'test_failed': True,
            'test_message': f"❌ {message}"
        })
        return self._show_notification("❌ Error", message, "danger")

    def _show_notification(self, title, message, type):
        """Muestra notificación en UI"""
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': title,
                'message': message,
                'type': type,
                'sticky': False,
            }
        }
    
    