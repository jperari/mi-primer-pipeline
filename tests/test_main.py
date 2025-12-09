import pytest
from app.main import app

@pytest.fixture
def client():
    """Crea un cliente de test para nuestra app"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    """Test de la ruta principal"""
    response = client.get('/')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'success'
    assert 'mensaje' in data

def test_health(client):
    """Test del endpoint de salud"""
    response = client.get('/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'healthy'

def test_saludar(client):
    """Test del endpoint personalizado"""
    response = client.get('/api/saludar/Pedro')
    assert response.status_code == 200
    data = response.get_json()
    assert data['nombre'] == 'Pedro'
    assert 'Bienvenido' in data['mensaje']