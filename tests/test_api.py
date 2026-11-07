from fastapi.testclient import TestClient
from app.main import app

def test_health():
    with TestClient(app) as client:
        assert client.get("/api/health").json()["status"] == "ok"

def test_dashboard():
    with TestClient(app) as client:
        assert "US CreatorOS" in client.get("/").text

def test_publish_is_disabled():
    with TestClient(app) as client:
        policy = client.get("/api/publishing/policy").json()
        assert policy["publishing_enabled"] is False
        assert policy["human_approval_required"] is True
