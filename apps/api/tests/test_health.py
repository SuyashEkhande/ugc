from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health() -> None:
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json() == {"status": "ok"}


def test_projects_empty() -> None:
    resp = client.get("/projects")
    assert resp.status_code == 200
    assert resp.json() == {"items": []}
