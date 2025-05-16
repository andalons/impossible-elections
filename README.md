# Absurd Candidates API

Una API divertida para gestionar candidatos presidenciales absurdos con propuestas delirantes y estadísticas inventadas.

## Características

- CRUD completo para candidatos presidenciales absurdos
- Búsqueda y filtrado de candidatos
- Estadísticas ficticias

## Estructura del proyecto

El proyecto sigue una estructura modular para facilitar la colaboración:

```
absurd-candidates-api/
├── main.py               # Punto de entrada de la aplicación
├── README.md             # Documentación del proyecto
├── requirements.txt      # Dependencias del proyecto
├── .gitignore            # Archivos a ignorar por git
├── app/
│   ├── models/           # Modelos de datos
│   ├── routers/          # Rutas de la API
│   ├── schemas/          # Esquemas Pydantic
│   └── db/               # Simulación de base de datos
└── tests/                # Tests unitarios
```

## Instalación y uso

1. Clonar el repositorio
2. Instalar dependencias:

```
pip install -r requirements.txt
```

3. Ejecutar el servidor:

```
uvicorn main:app --reload
```

4. Visitar la documentación en `http://localhost:8000/docs`

## Ejercicio de Pull Requests

Este repositorio está diseñado para practicar Pull Requests en GitHub. Cada equipo debe:

1. Crear un fork del repositorio
2. Trabajar en una rama feature específica
3. Implementar una funcionalidad asignada
4. Crear un Pull Request hacia el repositorio principal

### Funcionalidades a implementar (ramas)

- `feature/campaign-promises`: Añadir endpoints para gestionar promesas de campaña
- `feature/political-parties`: Añadir endpoints para gestionar partidos políticos
- `feature/voting-stats`: Añadir endpoints para estadísticas de votación
- `feature/debates`: Añadir endpoints para debates entre candidatos
- `feature/campaign-funds`: Añadir endpoints para gestionar fondos de campaña
