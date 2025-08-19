# FastAPI CRUD Ejemplo

Este proyecto es un ejemplo de aplicación CRUD (Crear, Leer, Actualizar, Eliminar) de usuarios utilizando FastAPI y SQLAlchemy.

## Estructura del Proyecto

```
main.py
app/
    config/
    models/
    repositories/
    routes/
    schemas/
```

- **main.py**: Punto de entrada de la aplicación FastAPI.
- **app/config/**: Configuración de la base de datos.
- **app/models/**: Definición de modelos ORM.
- **app/repositories/**: Lógica de acceso a datos (CRUD).
- **app/routes/**: Definición de rutas/endpoints.
- **app/schemas/**: Esquemas Pydantic para validación y serialización.

## Instalación

1. Clona el repositorio.
2. Instala las dependencias:
    ```sh
    pip install fastapi sqlalchemy pydantic
    ```
3. Ejecuta la aplicación:
    ```sh
    fastapi dev app.py
    ```

## Endpoints Principales

- `GET /`: Mensaje de bienvenida.
- `GET /users/`: Lista todos los usuarios.
- `GET /users/{user_id}`: Obtiene un usuario por ID.
- `POST /users/`: Crea un nuevo usuario.
- `PUT /users/{user_id}`: Actualiza un usuario existente.
- `DELETE /users/{user_id}`: Elimina un usuario.

## Base de Datos

Utiliza SQLite por defecto (`mi_base_de_datos.db`). Puedes cambiar la configuración en [`app/config/db.py`](app/config/db.py).

## Notas

- Los modelos y esquemas están definidos en [`app/models/user_model.py`](app/models/user_model.py) y [`app/schemas/user_schema.py`](app/schemas/user_schema.py).
- La lógica CRUD está en [`app/repositories/user_repository.py`](app/repositories/user_repository.py).
- Las rutas están en [`app/routes/user.py`](app/routes/user.py).