import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# Teste 1: Verificar se a rota principal responde com status 200
def test_home_status_code(client):
    response = client.get('/')
    assert response.status_code == 200

# Teste 2: Verificar se a resposta é um JSON
def test_home_content_type(client):
    response = client.get('/')
    assert response.content_type == 'application/json'

# Teste 3: Verificar se existe a chave 'mensagem' no JSON
def test_home_json_key(client):
    response = client.get('/')
    data = response.get_json()
    assert 'mensagem' in data

# Teste 4: Verificar se o texto da mensagem está correto
def test_home_json_value(client):
    response = client.get('/')
    data = response.get_json()
    assert data['mensagem'] == "Olá! Aplicação Python rodando com Docker!"

# Teste 5: Verificar se rota inexistente retorna 404
def test_not_found(client):
    response = client.get('/rota-inexistente')
    assert response.status_code == 404