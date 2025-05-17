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

## Instalación

1. Clonar el repositorio

2. Crear un entorno virtual: `python -m venv venv`

3. Activar el entorno virtual:

   - Windows: `venv\Scripts\activate`
   - MacOS/Linux: `source venv/bin/activate`

4. Instalar dependencias: `pip install -r requirements.txt`

5. Ejecutar el servidor:

```
uvicorn main:app --reload
```

7. Visitar la documentación en `http://localhost:8000/docs`

## Ejercicio de Pull Requests

Este repositorio está diseñado para practicar Pull Requests en GitHub. Cada equipo debe:

1. Hacer un Fork del repositorio y clonar el fork en local.

2. Crear una rama en la que trabajar la aportación al proyecto (`git checkout -b feature/nombre-del-feature`) y subirla al repositorio forkeado en github (`git push -u origin feature/nombre-del-feature`).

3. Realizar commits claros y concisos que describan cada pequeño cambio funcional.

4. Una vez terminada y revisada la nueva característica del proyecto (lanzando servidor y tests), realizar la Pull Request pertinente apuntando a la rama dev del repositorio original.

### Funcionalidades a implementar (ejercicio por grupos):

#### Grupo 1: Filtro por edad mínima en el endpoint `/candidates/`

**Objetivo:** Permitir filtrar candidatos por edad mínima.

**Pista:**

```
python
# router/candidates.py
@router.get("/", response_model=List[Candidate])
async def get_candidates(
    ...,
    min_age: Optional[int] = Query(None, ge=18, description="Edad mínima del candidato")
):
    ...
    if min_age is not None:
        candidates = [c for c in candidates if c.age >= min_age]
```

#### Grupo 2: Nuevo endpoint `/candidates/top-votes`

**Objetivo:** Mostrar los 3 candidatos con más votos ficticios.

**Pista:**

```
python
# router/candidates.py
@router.get("/top-votes", response_model=List[Candidate])
async def get_top_candidates():
    candidates = db.get_candidates()
    sorted_candidates = sorted(candidates, key=lambda c: c.fictional_votes, reverse=True)
    return sorted_candidates[:3]
```

#### Grupo 3: Añadir campo `quote` (frase célebre del candidato)

**Objetivo:** Añadir una cita representativa.

**Pista:**

```
python
# schemas/candidate.py
class CandidateBase(BaseModel):
    ...
    quote: Optional[str] = Field(None, max_length=300, description="Frase célebre del candidato")

# router/candidates.py (POST / PUT adaptado como en Grupo 1)
```

#### Grupo 4: Filtro por presupuesto mínimo

**Objetivo:** Permitir filtrar por candidatos con alto presupuesto de campaña.

**Pista:**

```
python
# router/candidates.py
@router.get("/", ...)
async def get_candidates(
    ...,
    min_budget: Optional[float] = Query(None, ge=0, description="Presupuesto mínimo")
):
    ...
    if min_budget is not None:
        candidates = [c for c in candidates if c.campaign_budget >= min_budget]
```

#### Grupo 5: Añadir campo `absurdity_index` (solo lectura)

**Objetivo:** Agregar un índice calculado entre populism y edad (por diversión).

**Pista:**

```
python
# schemas/candidate.py
class Candidate(CandidateBase):
    id: int
    created_at: datetime
    absurdity_index: float

    @property
    def absurdity_index(self):
        return round(self.populism_level / (self.age or 1), 2)
```

> También se puede agregar desde el modelo o como método en el router (@router.get("/absurdity")) si prefieres separar lógica.

#### Grupo 6: Endpoint `/candidates/random`

**Objetivo:** Devolver un candidato aleatorio.

**Pista:**

```
python
# router/candidates.py
@router.get("/", ...)
import random

@router.get("/random", response_model=Candidate)
async def get_random_candidate():
    candidates = db.get_candidates()
    if not candidates:
        raise HTTPException(status_code=404, detail="No hay candidatos")
    return random.choice(candidates)
```
