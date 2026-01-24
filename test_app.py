import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to Task Manager API" in response.data

def test_get_tasks(client):
    response = client.get('/tasks')
    assert response.status_code == 200
    json_Data = response.get_json()
    assert isinstance(json_Data, list)
    assert len(json_Data) >= 1

def test_add_task(client):
    new_task = {"title": "Write unit test for add_tasks"}
    response = client.post('/tasks', json = new_task)
    assert response.status_code == 201
    json_data = response.get_json()
    assert json_data['title'] == 'Write unit test for add_tasks'
    assert not json_data['done']

def test_add_task_without_title(client):
    response = client.post('/tasks', json = {})
    assert response.status_code == 400
    json_data = response.get_json()
    assert "error" in json_data
