from fastapi import APIRouter, HTTPException, Query, Path
from typing import List, Optional

from app.schemas.candidate import Candidate, CandidateCreate, CandidateUpdate
from app.db.database import db
from app.models.candidate import CandidateModel

router = APIRouter(
    prefix="/candidates",
    tags=["candidates"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=List[Candidate])
async def get_candidates(
    name: Optional[str] = Query(None, description="Filtrar por nombre"),
    party: Optional[str] = Query(None, description="Filtrar por partido político"),
    min_populism: Optional[int] = Query(None, ge=0, le=100, description="Nivel mínimo de populismo"),
    max_populism: Optional[int] = Query(None, ge=0, le=100, description="Nivel máximo de populismo")
):
    """
    Obtiene la lista de todos los candidatos absurdos.
    Se pueden aplicar filtros opcionales.
    """
    candidates = db.get_candidates()
    
    if name:
        candidates = [c for c in candidates if name.lower() in c.name.lower()]
    
    if party:
        candidates = [c for c in candidates if party.lower() in c.party.lower()]
    
    if min_populism is not None:
        candidates = [c for c in candidates if c.populism_level >= min_populism]
    
    if max_populism is not None:
        candidates = [c for c in candidates if c.populism_level <= max_populism]
    
    return candidates

@router.get("/{candidate_id}", response_model=Candidate)
async def get_candidate(candidate_id: int = Path(..., gt=0, description="ID del candidato")):
    """
    Obtiene un candidato específico por su ID.
    """
    candidate = db.get_candidate(candidate_id)
    if candidate is None:
        raise HTTPException(status_code=404, detail="Candidato no encontrado")
    return candidate

@router.post("/", response_model=Candidate, status_code=201)
async def create_candidate(candidate: CandidateCreate):
    """
    Crea un nuevo candidato absurdo.
    """
    new_candidate = db.add_candidate(
        name=candidate.name,
        party=candidate.party,
        main_proposal=candidate.main_proposal,
        populism_level=candidate.populism_level,
        fictional_votes=candidate.fictional_votes,
        slogan=candidate.slogan,
        age=candidate.age,
        campaign_budget=candidate.campaign_budget
    )
    return new_candidate

@router.put("/{candidate_id}", response_model=Candidate)
async def update_candidate(
    candidate_data: CandidateUpdate,
    candidate_id: int = Path(..., gt=0, description="ID del candidato")
):
    """
    Actualiza un candidato existente.
    """
    candidate = db.get_candidate(candidate_id)
    if candidate is None:
        raise HTTPException(status_code=404, detail="Candidato no encontrado")
    
    update_data = {k: v for k, v in candidate_data.dict().items() if v is not None}
    updated_candidate = db.update_candidate(candidate_id, update_data)
    
    return updated_candidate

@router.delete("/{candidate_id}", status_code=204)
async def delete_candidate(candidate_id: int = Path(..., gt=0, description="ID del candidato")):
    """
    Elimina un candidato existente.
    """
    success = db.delete_candidate(candidate_id)
    if not success:
        raise HTTPException(status_code=404, detail="Candidato no encontrado")
    return None

@router.get("/stats/populism", response_model=dict)
async def get_populism_stats():
    """
    Obtiene estadísticas sobre el nivel de populismo de los candidatos.
    """
    candidates = db.get_candidates()
    
    if not candidates:
        return {
            "average_populism": 0,
            "max_populism": 0,
            "min_populism": 0,
            "total_candidates": 0
        }
    
    populism_levels = [c.populism_level for c in candidates]
    
    return {
        "average_populism": sum(populism_levels) / len(populism_levels),
        "max_populism": max(populism_levels),
        "min_populism": min(populism_levels),
        "total_candidates": len(candidates)
    }