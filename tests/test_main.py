from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def testando_listar_estudante_sucesso():
    response = client.get("/estudantes")
    assert response.status_code == 200
    assert response.json() == [
        {"id": 1, "nome": "Gilmar", "email": "gilmar@gmail.com"}
    ]


def testando_listar_estudante_por_id_sucesso():
    id_estudante = 1
    response = client.get(f"/estudantes/{id_estudante}")
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "nome": "Gilmar",
        "email": "gilmar@gmail.com",
    }


def testando_listar_estudante_por_id_falha():
    id_estudante = 2
    response = client.get(f"/estudantes/{id_estudante}")
    assert response.status_code == 404
    assert response.json() == {"detail": "Estudante não encontrado."}


def testando_criar_estudante_sucesso():
    response = client.post(
        "/estudantes", json={"nome": "Victor", "email": "victor@gmail.com"}
    )
    assert response.status_code == 201
    assert response.json() == {
        "id": 2,
        "nome": "Victor",
        "email": "victor@gmail.com",
    }


def testando_criar_estudante_falha():
    response = client.post("/estudantes", json={"email": "lucas@gmail.com"})
    assert response.status_code == 422
