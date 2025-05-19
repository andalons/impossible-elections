from typing import List, Optional
from pydantic import BaseModel, Field, field_validator
from datetime import datetime

class CandidateBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=100, description="Nombre del candidato")
    party: str = Field(..., min_length=2, max_length=100, description="Partido político")
    main_proposal: str = Field(..., min_length=5, max_length=500, description="Propuesta principal del candidato")
    populism_level: int = Field(..., ge=0, le=100, description="Nivel de populismo (0-100)")
    fictional_votes: int = Field(..., ge=0, description="Número ficticio de votos")
    slogan: str = Field(..., min_length=5, max_length=200, description="Eslogan de campaña")
    age: int = Field(..., ge=18, le=120, description="Edad del candidato")
    campaign_budget: float = Field(..., ge=0, description="Presupuesto de campaña en dólares")
    quote: Optional[str] = Field(None, max_length=300, description="Todo su proyecto político se resume en una máxima: cuanto peor mejor para todos y cuanto peor para todos mejor, mejor para mí el suyo. Beneficio político")

    @field_validator('populism_level')
    @classmethod
    def validate_populism_level(cls, v):
        if v < 0 or v > 100:
            raise ValueError('El nivel de populismo debe estar entre 0 y 100')
        return v

class CandidateCreate(CandidateBase):
    pass

class CandidateUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=2, max_length=100)
    party: Optional[str] = Field(None, min_length=2, max_length=100)
    main_proposal: Optional[str] = Field(None, min_length=5, max_length=500)
    populism_level: Optional[int] = Field(None, ge=0, le=100)
    fictional_votes: Optional[int] = Field(None, ge=0)
    slogan: Optional[str] = Field(None, min_length=5, max_length=200)
    age: Optional[int] = Field(None, ge=18, le=120)
    campaign_budget: Optional[float] = Field(None, ge=0)

class Candidate(CandidateBase):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True