import pytest
from app import APP

@pytest.fixture()
def client():
    app = APP
    app.config.update({
        "TESTING": True
    })

    yield app.test_client()

def test_index(client):
    resposta = client.get("/")
    conteudo_da_resposta = resposta.text

    conteudo_esperado = """<h1>Integrantes</h1>
<br>
Pedro Rocha Horchulhack"""

    assert conteudo_esperado == conteudo_da_resposta

def test_livros(client):
    resposta = client.get("/livros")
    conteudo_da_resposta = resposta.text

    assert "[]\n" == conteudo_da_resposta