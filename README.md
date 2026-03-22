# FastAPI Películas API

Proyecto simple de ejemplo usando FastAPI + SQLAlchemy + SQLite.

## 📁 Estructura del proyecto

- `main.py`: API endpoints (CRUD) para películas
- `models.py`: definición del modelo SQLAlchemy
- `database.py`: configuración de conexión SQLite y base de datos
- `dtos.py`: modelos de Pydantic para request/response
- `peliculas/crud.py`: operaciones CRUD de la tabla `peliculas`
- `sql_app.db`: base de datos SQLite local

## ⚙️ Requisitos

- Python 3.10+ (recomendado 3.11)
- pip

## 🛠️ Instalación rápida

1. Clona o descarga el repositorio

```bash
cd C:/Users/Pedro/.vscode/FastApi
```

2. Crea y activa un entorno virtual (Windows PowerShell/Command Prompt)

```bash
python -m venv venv
venv\Scripts\activate
```

3. Instala dependencias

```bash
pip install fastapi uvicorn sqlalchemy pydantic
```


## 🚀 Ejecutar la aplicación

```bash
uvicorn main:app --reload
```

Esto inicia el servidor en `http://127.0.0.1:8000`.

## 📚 Endpoints disponibles

- `GET /peliculas` - Listar todas las películas
- `GET /peliculas/{pelicula_id}` - Obtener película por ID
- `POST /peliculas` - Crear película
- `PUT /peliculas/{pelicula_id}` - Actualizar película
- `DELETE /peliculas/{pelicula_id}` - Eliminar película

## 📄 Esquema de película (DTO)

Request/response (`PeliculaCreate` / `PeliculaResponse`):

- `title`: `str`
- `overview`: `str`
- `year`: `int`
- `rating`: `float`
- `category`: `str`
- `id` (solo response)

## 🧪 Ejemplos con `curl`

### Crear película

```bash
curl -X POST "http://127.0.0.1:8000/peliculas" -H "Content-Type: application/json" -d "{\"title\":\"The Matrix\",\"overview\":\"Cyberpunk action\",\"year\":1999,\"rating\":8.7,\"category\":\"Ciencia ficción\"}"
```

### Listar películas

```bash
curl http://127.0.0.1:8000/peliculas
```

### Obtener película por ID

```bash
curl http://127.0.0.1:8000/peliculas/1
```

### Actualizar película

```bash
curl -X PUT "http://127.0.0.1:8000/peliculas/1" -H "Content-Type: application/json" -d "{\"title\":\"The Matrix Reloaded\",\"overview\":\"Second film\",\"year\":2003,\"rating\":7.2,\"category\":\"Ciencia ficción\"}"
```

### Eliminar película

```bash
curl -X DELETE http://127.0.0.1:8000/peliculas/1
```

## 🧰 Documentación interactiva

FastAPI ofrece Swagger UI aqui:

- `http://127.0.0.1:8000/docs`
- `http://127.0.0.1:8000/redoc`

## 🗂️ Notas adicionales

- El archivo `sql_app.db` se crea/usa por defecto en el directorio del proyecto.
- Si quieres reiniciar datos, detén servidor, borra `sql_app.db` y reinicia.
