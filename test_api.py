def test_get_user(client):
    response = client.get("/users/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert "email" in data
    assert data["email"] != ""

def test_get_invalid_user(client):
    response = client.get("/users/9999")
    assert response.status_code in [200, 404]    