from fastapi.testclient import TestClient

from app import app


client = TestClient(app)


def test_home_page():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == "Welcome to the PubChem Compound Analyzer API"


def test_analyze_endpoint():
    response = client.post(
        "/analyze",
        json={"compounds": ["caffeine", "aspirin"]}
    )

    data = response.json()

    assert response.status_code == 200
    assert "compounds" in data
    assert "average_molecular_weight" in data
    assert "heaviest_compound" in data
    assert len(data["compounds"]) == 2
