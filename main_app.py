import logging
import os
from flask import Flask, render_template

import clima_app
import peliculas_app
import divisas_app
import github_app
import libros_app
import lugares_app
import reddit_app
import spotify_app
import chat_app
import productos_api

main = Flask(__name__)
main.secret_key = os.environ.get('SECRET_KEY', os.urandom(24))

# Sub-app registry: (name, module, path, emoji, title, description)
APP_CONFIGS = [
    ('clima',     clima_app,     '/clima',     '🌤',  'Clima',            'Consulta el clima de tu ubicación actual'),
    ('peliculas', peliculas_app, '/peliculas', '🎬',  'Películas & Series','Busca películas y series con TMDB API'),
    ('divisas',   divisas_app,   '/divisas',   '💰',  'Divisas',          'Convierte monedas en tiempo real'),
    ('github',    github_app,    '/github',    '🐙',  'GitHub',           'Explora perfiles y repositorios de GitHub'),
    ('libros',    libros_app,    '/libros',    '📚',  'Libros',           'Busca libros con Google Books API'),
    ('lugares',   lugares_app,   '/lugares',   '📍',  'Lugares',          'Encuentra lugares cercanos a ti'),
    ('reddit',    reddit_app,    '/reddit',    '🤖',  'Reddit',           'Explora posts y subreddits de Reddit'),
    ('spotify',   spotify_app,   '/spotify',   '🎵',  'Spotify',          'Busca música y artistas en Spotify'),
    ('chat',      chat_app,      '/chat',      '💬',  'Chat',             'Chat en tiempo real con Firebase'),
    ('productos', productos_api, '/productos', '🛍️', 'Productos',        'API REST de gestión de productos'),
]


@main.route('/')
def index():
    return render_template('index.html')


# Register routes from each sub-app into the main app
for _app_name, _module, _path, _emoji, _title, _desc in APP_CONFIGS:
    for _rule in _module.app.url_map.iter_rules():
        if _rule.endpoint == 'static':
            continue
        _view_func = _module.app.view_functions[_rule.endpoint]
        _endpoint = f'{_app_name}_{_rule.endpoint}'

        if _rule.rule == '/':
            # Map each sub-app's root page to /app_name
            main.add_url_rule(_path, _endpoint, _view_func)
        else:
            # API routes keep their original absolute paths
            try:
                main.add_url_rule(
                    str(_rule),
                    _endpoint,
                    _view_func,
                    methods=_rule.methods,
                )
            except AssertionError:
                logging.debug("Skipping duplicate route: %s (%s)", _rule.rule, _endpoint)


if __name__ == '__main__':
    productos_api.init_db()
    print("=" * 60)
    print("🚀 Página Principal - Todas las Apps")
    print("=" * 60)
    for _, _, path, emoji, title, _ in APP_CONFIGS:
        print(f"  {emoji}  {title:20s} → http://127.0.0.1:5000{path}")
    print("=" * 60)
    print("🌐 Servidor corriendo en: http://127.0.0.1:5000")
    print("=" * 60)
    main.run(debug=os.environ.get("FLASK_DEBUG", "0") == "1")
