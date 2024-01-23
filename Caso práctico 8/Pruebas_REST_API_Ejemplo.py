import requests


def test_user_creation():
  url = "http://localhost:5000/users"
  user_data = {
      "username": "testuser",
      "email": "test@example.com",
      "password": "password123"
  }
  response = requests.post(url, json=user_data)
  assert response.status_code == 201
  assert response.json()['message'] == "Usuario creado con éxito"
