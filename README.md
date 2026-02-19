# APIS_PYTHON_U2

Colección de ejercicios prácticos con Flask y APIs de terceros - Unidad 2.

## 🚀 Instalación rápida

```bash
# Crear y activar entorno virtual
python -m venv venv
source venv/bin/activate   # Linux/Mac
# venv\Scripts\activate   # Windows

# Instalar dependencias
pip install -r requirements.txt
```

## 📋 Ejercicios disponibles

| Ejercicio | Archivo | API requerida |
|-----------|---------|---------------|
| 1.1 Sistema de Clima | `clima_app.py` | OpenWeatherMap (`WEATHER_API_KEY`) |
| 1.2 Buscador de Lugares | `lugares_app.py` | Overpass/OSM (sin API key) |
| 2.1 Analizador de Reddit | `reddit_app.py` | Reddit JSON (sin API key) |
| 2.2 Dashboard de GitHub | `github_app.py` | GitHub API (sin API key) |
| 3.1 API REST con SQLite | `productos_api.py` | Sin API externa |
| 3.2 Chat con Firebase | `chat_app.py` | Firebase Admin SDK |
| 4.1 Buscador de Libros | `libros_app.py` | Google Books (sin API key) |
| 4.2 Conversor de Divisas | `divisas_app.py` | ExchangeRate-API (`API_KEY`) |
| 5.1 Buscador de Películas | `peliculas_app.py` | TMDB (`TMDB_API_KEY`) |
| 5.2 Buscador de Música | `spotify_app.py` | Spotify (`CLIENT_ID`, `CLIENT_SECRET`) |

## 🔑 Configuración de API Keys

Abre cada archivo `.py` y reemplaza el placeholder de la API key:

- **clima_app.py** → `WEATHER_API_KEY = 'TU_API_KEY_AQUI'`
- **divisas_app.py** → `API_KEY = 'TU_API_KEY_AQUI'`
- **peliculas_app.py** → `TMDB_API_KEY = 'TU_API_KEY_AQUI'`
- **spotify_app.py** → `CLIENT_ID = 'TU_CLIENT_ID_AQUI'` y `CLIENT_SECRET = 'TU_CLIENT_SECRET_AQUI'`
- **chat_app.py** → Coloca `firebase-credentials.json` en la raíz y actualiza `databaseURL`

## ▶️ Ejecutar un ejercicio

```bash
python clima_app.py        # Ejercicio 1.1 - Puerto 5000
python lugares_app.py      # Ejercicio 1.2 - Puerto 5000
python reddit_app.py       # Ejercicio 2.1 - Puerto 5000
python github_app.py       # Ejercicio 2.2 - Puerto 5000
python productos_api.py    # Ejercicio 3.1 - Puerto 5000
python chat_app.py         # Ejercicio 3.2 - Puerto 5000
python libros_app.py       # Ejercicio 4.1 - Puerto 5000
python divisas_app.py      # Ejercicio 4.2 - Puerto 5000
python peliculas_app.py    # Ejercicio 5.1 - Puerto 5000
python spotify_app.py      # Ejercicio 5.2 - Puerto 5000
```

Abre tu navegador en: **http://127.0.0.1:5000**

## 📁 Estructura del proyecto

```
APIS_PYTHON_U2/
├── templates/           # Interfaces HTML de cada ejercicio
│   ├── clima.html
│   ├── lugares.html
│   ├── reddit.html
│   ├── github.html
│   ├── productos.html
│   ├── chat.html
│   ├── libros.html
│   ├── divisas.html
│   ├── peliculas.html
│   └── spotify.html
├── static/              # Archivos estáticos (CSS, JS, imágenes)
├── screenshots/         # Capturas de pantalla de la aplicación
├── clima_app.py
├── lugares_app.py
├── reddit_app.py
├── github_app.py
├── productos_api.py
├── chat_app.py
├── libros_app.py
├── divisas_app.py
├── peliculas_app.py
├── spotify_app.py
└── requirements.txt
```

## 📸 Capturas de Pantalla


### 1.2 Buscador de Lugares
![Buscador de Lugares](screenshots/API-LUGARES.png)

### 2.1 Analizador de Reddit
![Analizador de Reddit](screenshots/API-REDDIT.png)

### 2.2 Dashboard de GitHub
![Dashboard de GitHub](screenshots/API-GITHUB.png)

### 3.1 API REST con SQLite
![API REST con SQLite](screenshots/API-PRODUCTOS.png)

### 3.2 Chat con Firebase
![Chat con Firebase](screenshots/API-FIREBASE.png)

### 4.2 Conversor de Divisas
![Conversor de Divisas](screenshots/API-DIVISAS.png)

### 5.1 Buscador de Películas
![Buscador de Películas](screenshots/API-PELICULAS.png)

### 5.2 Buscador de Música
![Buscador de Música](screenshots/API-SPOTIFY.png)
