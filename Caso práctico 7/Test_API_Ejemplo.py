import pytest
from app import app, db
from models import User, Product

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    client = app.test_client()

    with app.app_context():
        db.create_all()

    yield client

    with app.app_context():
        db.drop_all()

def test_create_user(client):
    response = client.post('/users', json={'username': 'testuser', 'email': 'test@example.com', 'password': 'testpass'})
    assert response.status_code == 201
    assert response.json['message'] == 'Usuario creado con éxito'
