import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome to Our Portfolio' in response.data

def test_services_page(client):
    response = client.get('/services')
    assert response.status_code == 200
    assert b'Services We Offer' in response.data

def test_portfolio_page(client):
    response = client.get('/portfolio')
    assert response.status_code == 200
    assert b'Our Work' in response.data

def test_contact_page(client):
    response = client.get('/contact')
    assert response.status_code == 200
    assert b'Contact Us' in response.data

def test_404_page(client):
    response = client.get('/non-existent-page')
    assert response.status_code == 404
    assert b'Page Not Found' in response.data