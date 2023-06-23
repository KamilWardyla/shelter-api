import pytest

from main import app, db


@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test_database.db'
    with app.app_context():
        db.create_all()
    with app.test_client() as client:
        yield client
    with app.app_context():
        db.drop_all()


def test_get_all_animals(client):
    response = client.get('/animals')
    assert response.status_code == 200


def test_get_animal(client):
    response = client.get('/animal/1')
    assert response.status_code == 404


def test_post_animal(client):
    data = {
        'name': 'Puszek',
        'type': 'Kot',
        'race': 'Dachowiec',
        'age': 3
    }
    response = client.post('/animal/1', json=data)
    assert response.status_code == 200


def test_patch_animal(client):
    data = {
        'name': 'Zaktualizowana Nazwa'
    }
    response = client.patch('/animal/1', json=data)
    assert response.status_code == 200


def test_delete_animal(client):
    response = client.delete('/animal/1')
    assert response.status_code == 200
