{
    'name': 'Movies Management',
    'version': '1.0',
    'summary': 'Manage Movies and API Integration',
    'description': """
        Module to manage movies with external API integration.
        Features:
        - Movie catalog
        - API configuration
        - Random movie importer
        - Automatic movie fetching via cron job
    """,
    'author': 'Pablo Torres Labraña',
    'category': 'Tools',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'data/cron_jobs.xml', 
        'views/movie_views.xml',
        'views/settings_views.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}