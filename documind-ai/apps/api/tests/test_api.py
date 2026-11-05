from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root_health() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_v1_health() -> None:
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json()["service"] == "documind-ai"


def test_analyze_repository() -> None:
    response = client.post(
        "/api/v1/repositories/analyze",
        json={"url": "https://github.com/example/project"},
    )
    assert response.status_code == 200
    body = response.json()
    assert body["repository"] == "project"
    assert body["language"] == "Python"
    assert body["framework"] == "FastAPI"
    assert body["files"] > 0
