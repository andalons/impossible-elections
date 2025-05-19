from typing import List, Dict, Optional
from datetime import datetime
from app.models.candidate import CandidateModel

# Simulación de base de datos en memoria
class Database:
    def __init__(self):
        self.candidates: List[CandidateModel] = []
        self.counter = 1
        self._initialize_data()
    
    def _initialize_data(self):
        """Inicializa la base de datos con algunos candidatos predefinidos."""
        initial_candidates = [
            {
                "name": "Captain Cosmo",
                "party": "Intergalactic Party",
                "main_proposal": "Convert the national budget to space doubloons",
                "populism_level": 85,
                "fictional_votes": 42000,
                "slogan": "To infinity and beyond taxes!",
                "age": 45,
                "campaign_budget": 3000000.0,
                "vice_name": "Admiral Nebula"
            },
            {
                "name": "Lady Naps-A-Lot",
                "party": "Siesta Coalition",
                "main_proposal": "Mandatory 3-hour lunch breaks for all workers",
                "populism_level": 92,
                "fictional_votes": 56000,
                "slogan": "A pillow in every office!",
                "age": 39,
                "campaign_budget": 1500000.0,
                "vice_name": "Sir Snooze"
            },
            {
                "name": "Professor Meme",
                "party": "Viral Democracy Movement",
                "main_proposal": "All laws must be proposed in meme format",
                "populism_level": 78,
                "fictional_votes": 38000,
                "slogan": "Such leadership. Very democracy. Wow.",
                "age": 33,
                "campaign_budget": 750000.0,
                "vice_name": "Doge McVice"
            }
        ]
        
        for candidate_data in initial_candidates:
            self.add_candidate(
                name=candidate_data["name"],
                party=candidate_data["party"],
                main_proposal=candidate_data["main_proposal"],
                populism_level=candidate_data["populism_level"],
                fictional_votes=candidate_data["fictional_votes"],
                slogan=candidate_data["slogan"],
                age=candidate_data["age"],
                campaign_budget=candidate_data["campaign_budget"], 
                vice_name=candidate_data["vice_name"] 
            )
    
    def add_candidate(self, name: str, party: str, main_proposal: str, 
                     populism_level: int, fictional_votes: int, slogan: str, 
                     age: int, campaign_budget: float, vice_name=None) -> CandidateModel:
        """Añade un nuevo candidato a la base de datos."""
        new_candidate = CandidateModel(
            id=self.counter,
            name=name,
            party=party,
            main_proposal=main_proposal,
            populism_level=populism_level,
            fictional_votes=fictional_votes,
            slogan=slogan,
            age=age,
            campaign_budget=campaign_budget,
            vice_name=vice_name,
            created_at=datetime.now()
        )
        self.candidates.append(new_candidate)
        self.counter += 1
        return new_candidate
    
    def get_candidates(self) -> List[CandidateModel]:
        """Obtiene todos los candidatos."""
        return self.candidates
    
    def get_candidate(self, candidate_id: int) -> Optional[CandidateModel]:
        """Obtiene un candidato por su ID."""
        for candidate in self.candidates:
            if candidate.id == candidate_id:
                return candidate
        return None
    
    def update_candidate(self, candidate_id: int, data: Dict) -> Optional[CandidateModel]:
        """Actualiza un candidato existente."""
        candidate = self.get_candidate(candidate_id)
        if candidate:
            for key, value in data.items():
                if hasattr(candidate, key):
                    setattr(candidate, key, value)
            return candidate
        return None
    
    def delete_candidate(self, candidate_id: int) -> bool:
        """Elimina un candidato por su ID."""
        candidate = self.get_candidate(candidate_id)
        if candidate:
            self.candidates.remove(candidate)
            return True
        return False

# Instancia global de la base de datos
db = Database()