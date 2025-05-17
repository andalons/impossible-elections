from typing import List, Dict, Optional
from datetime import datetime, timezone

# Modelo simple para almacenar candidatos (simulando una base de datos)
class CandidateModel:
    def __init__(self, id: int, name: str, party: str, main_proposal: str, 
                 populism_level: int, fictional_votes: int, slogan: str, 
                 age: int, campaign_budget: float, created_at: datetime):
        self.id = id
        self.name = name
        self.party = party
        self.main_proposal = main_proposal
        self.populism_level = populism_level
        self.fictional_votes = fictional_votes
        self.slogan = slogan
        self.age = age
        self.campaign_budget = campaign_budget
        self.created_at = created_at or datetime.now(timezone.utc)
    
    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "name": self.name,
            "party": self.party,
            "main_proposal": self.main_proposal,
            "populism_level": self.populism_level,
            "fictional_votes": self.fictional_votes,
            "slogan": self.slogan,
            "age": self.age,
            "campaign_budget": self.campaign_budget,
            "created_at": self.created_at.isoformat()
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> "CandidateModel":
        return cls(
            id=data["id"],
            name=data["name"],
            party=data["party"],
            main_proposal=data["main_proposal"],
            populism_level=data["populism_level"],
            fictional_votes=data["fictional_votes"],
            slogan=data["slogan"],
            age=data["age"],
            campaign_budget=data["campaign_budget"],
            created_at=datetime.fromisoformat(data["created_at"]) if isinstance(data["created_at"], str) else data["created_at"]
        )