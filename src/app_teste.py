import pytest
from app import app, db
from models.employeeModel import EmployeeModel

@pytest.fixture
def client():
    
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///memory:' 
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client 
        #limpar o banco em memória.
        with app.app_context():
            db.drop_all()

  #PARA RODAR O TESTE:
    # No terminal digite: pytest --cov=src 

""" Teste para o servidor levar para a pagina inicial """
def test_index(client):
    test = client.get('/')
    assert test.status_code == 200


"""Teste para ver se o primeiro nome """
def teste2_index(client):
    teste2 = client.get('/')
    assert teste2.status_code == 200
    assert b'Bem-vindo a Personalite' in teste2.data


""" Testar acesso a pagina de create e cadastrar um usuário e direcionar para outra pagina"""
def test3create(client):
    test = client.get('/create')
    test2 = client.post('/create', data={'cpf':'32165498713', 'nome':'leoz', 'cargo':'dev'},follow_redirects=True)
    assert test.status_code == 200
    assert test2.status_code == 200


""" Teste de contagem de funcionario cadastrado no banco, e se recebeu os parametros que foi cadastro corretamente """
with app.app_context():
        employeer = EmployeeModel.query.all()
        assert len(employeer) == 1
        assert employeer[0].name == 'leoz'
        assert employeer[0].cpf == '32165498713'
        assert employeer[0].cargo == 'dev'




