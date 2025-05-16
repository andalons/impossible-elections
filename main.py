from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import candidates

app = FastAPI(
    title="Absurd Candidates API",
    description="API para gestionar candidatos presidenciales absurdos",
    version="0.1.0",
)

# Configuración CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir routers
app.include_router(candidates.router)

@app.get("/")
async def root():
    return {
        "message": "Welcome to the Absurd Candidates API!",
        "description": "An API for managing absurd presidential candidates",
        "docs": "/docs"
    }