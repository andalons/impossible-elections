import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_candidates():
    response = client.get("/candidates/")
    assert response.status_code == 200
    candidates = response.json()
    assert len(candidates) >= 3
    assert candidates[0]["name"] == "Captain Cosmo"

def test_read_candidate():
    response = client.get("/candidates/1")
    assert response.status_code == 200
    candidate = response.json()
    assert candidate["id"] == 1
    assert candidate["name"] == "Captain Cosmo"

def test_create_candidate():
    new_candidate = {
        "name": "Sir Nibbles",
        "party": "Feline First Party",
        "main_proposal": "Mandatory cat nap time for all citizens",
        "populism_level": 95,
        "fictional_votes": 67000,
        "slogan": "A mouse in every house!",
        "age": 42,
        "campaign_budget": 2500000.0
    }
    
    response = client.post("/candidates/", json=new_candidate)
    assert response.status_code == 201
    created = response.json()
    assert created["name"] == new_candidate["name"]
    assert created["party"] == new_candidate["party"]
    assert created["id"] is not None

def test_update_candidate():
    update_data = {
        "slogan": "New slogan for testing!",
        "populism_level": 50
    }
    
    response = client.put("/candidates/1", json=update_data)
    assert response.status_code == 200
    updated = response.json()
    assert updated["slogan"] == update_data["slogan"]
    assert updated["populism_level"] == update_data["populism_level"]

def test_delete_candidate():
    # First create a candidate to delete
    new_candidate = {
        "name": "Temporary Candidate",
        "party": "Delete Me Party",
        "main_proposal": "This candidate will be deleted",
        "populism_level": 50,
        "fictional_votes": 10000,
        "slogan": "Delete me!",
        "age": 40,
        "campaign_budget": 100000.0
    }
    
    create_response = client.post("/candidates/", json=new_candidate)
    assert create_response.status_code == 201
    candidate_id = create_response.json()["id"]
    
    # Now delete the candidate
    delete_response = client.delete(f"/candidates/{candidate_id}")
    assert delete_response.status_code == 204
    
    # Verify the candidate is deleted
    get_response = client.get(f"/candidates/{candidate_id}")
    assert get_response.status_code == 404