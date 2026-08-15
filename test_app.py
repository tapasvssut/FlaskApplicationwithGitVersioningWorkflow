import pytest
from app import app, votes


@pytest.fixture(autouse=True)
def clear_votes():
    """Reset vote store before every test so tests are independent."""
    votes.clear()
    yield
    votes.clear()


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


# ── Home endpoint ────────────────────────────────────────────────────────────

def test_home_status_code(client):
    response = client.get("/")
    assert response.status_code == 200


def test_home_response_text(client):
    response = client.get("/")
    assert b"Welcome to the App" in response.data


# ── Health endpoint ───────────────────────────────────────────────────────────

def test_health_status_code(client):
    response = client.get("/health")
    assert response.status_code == 200


def test_health_response_text(client):
    response = client.get("/health")
    assert b"App is running" in response.data


# ── Vote endpoint ─────────────────────────────────────────────────────────────

def test_vote_new_candidate_returns_200(client):
    response = client.get("/vote/alice")
    assert response.status_code == 200


def test_vote_new_candidate_count_starts_at_1(client):
    data = client.get("/vote/alice").get_json()
    assert data["votes"] == 1


def test_vote_same_candidate_increments_count(client):
    client.get("/vote/alice")
    data = client.get("/vote/alice").get_json()
    assert data["votes"] == 2


def test_vote_response_contains_candidate_name(client):
    data = client.get("/vote/alice").get_json()
    assert data["candidate"] == "alice"


def test_vote_response_contains_message(client):
    data = client.get("/vote/alice").get_json()
    assert "Vote recorded for alice" in data["message"]


def test_vote_name_is_lowercased(client):
    data = client.get("/vote/Alice").get_json()
    assert data["candidate"] == "alice"


def test_vote_multiple_candidates_are_independent(client):
    client.get("/vote/alice")
    data = client.get("/vote/bob").get_json()
    assert data["votes"] == 1


# ── Results endpoint ──────────────────────────────────────────────────────────

def test_results_empty_when_no_votes(client):
    data = client.get("/results").get_json()
    assert data == {}


def test_results_shows_all_candidates(client):
    client.get("/vote/alice")
    client.get("/vote/bob")
    data = client.get("/results").get_json()
    assert "alice" in data
    assert "bob" in data


def test_results_shows_correct_counts(client):
    client.get("/vote/alice")
    client.get("/vote/alice")
    client.get("/vote/bob")
    data = client.get("/results").get_json()
    assert data["alice"] == 2
    assert data["bob"] == 1


def test_results_returns_json_content_type(client):
    response = client.get("/results")
    assert response.content_type == "application/json"


# ── Reset endpoint ────────────────────────────────────────────────────────────

def test_reset_via_get_returns_200(client):
    response = client.get("/reset")
    assert response.status_code == 200


def test_reset_via_post_returns_200(client):
    response = client.post("/reset")
    assert response.status_code == 200


def test_reset_clears_all_votes(client):
    client.get("/vote/alice")
    client.get("/vote/bob")
    client.get("/reset")
    data = client.get("/results").get_json()
    assert data == {}


def test_reset_response_message(client):
    data = client.get("/reset").get_json()
    assert data["message"] == "All votes reset successfully"


def test_reset_then_vote_starts_fresh(client):
    client.get("/vote/alice")
    client.get("/reset")
    data = client.get("/vote/alice").get_json()
    assert data["votes"] == 1
