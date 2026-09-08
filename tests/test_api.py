import json

import pytest
from fastapi.testclient import TestClient

import app.main as app_module


client = TestClient(app_module.app)


@pytest.fixture
def demo_credentials(monkeypatch):
    monkeypatch.setenv(
        "NEXVIGIL_ANALYST_PASSWORD",
        "synthetic-analyst-password",
    )
    monkeypatch.setenv(
        "NEXVIGIL_DEVELOPER_PASSWORD",
        "synthetic-developer-password",
    )


@pytest.fixture
def event_file(tmp_path, monkeypatch):
    path = tmp_path / "security_events.jsonl"
    monkeypatch.setattr(app_module, "EVENT_FILE", path)
    return path


def read_events(path):
    if not path.exists():
        return []

    return [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "service": "nexvigil-lab-api",
        "version": "1.0.2",
    }


def test_valid_login_generates_success_event(
    demo_credentials,
    event_file,
):
    password = "synthetic-analyst-password"

    response = client.post(
        "/auth/login",
        json={
            "username": "analyst@nexvigil.local",
            "password": password,
        },
    )

    assert response.status_code == 200
    assert response.json() == {"status": "success"}

    events = read_events(event_file)

    assert len(events) == 1
    assert events[0]["result"] == "success"
    assert events[0]["username"] == "analyst@nexvigil.local"
    assert events[0]["event_type"] == "authentication"
    assert events[0]["action"] == "login"


def test_invalid_login_generates_failed_event(
    demo_credentials,
    event_file,
):
    response = client.post(
        "/auth/login",
        json={
            "username": "analyst@nexvigil.local",
            "password": "wrong-password",
        },
    )

    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid credentials"

    events = read_events(event_file)

    assert len(events) == 1
    assert events[0]["result"] == "failed"


def test_password_is_never_written_to_telemetry(
    demo_credentials,
    event_file,
):
    password = "synthetic-developer-password"

    response = client.post(
        "/auth/login",
        json={
            "username": "developer@nexvigil.local",
            "password": password,
        },
    )

    assert response.status_code == 200

    raw_telemetry = event_file.read_text(encoding="utf-8")

    assert password not in raw_telemetry

    event = read_events(event_file)[0]

    assert "password" not in event
    assert "token" not in event


def test_missing_demo_credentials_raise_configuration_error(
    monkeypatch,
):
    monkeypatch.delenv(
        "NEXVIGIL_ANALYST_PASSWORD",
        raising=False,
    )
    monkeypatch.delenv(
        "NEXVIGIL_DEVELOPER_PASSWORD",
        raising=False,
    )

    with pytest.raises(
        RuntimeError,
        match="demo credentials are not configured",
    ):
        app_module.get_demo_users()