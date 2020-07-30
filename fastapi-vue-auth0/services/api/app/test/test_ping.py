from app.test.utils import API_BASE


def test_ping(client):
    response = client.get(f'{API_BASE}/ping')
    assert response.status_code == 200
    assert response.json() == {"message": "pong"}
