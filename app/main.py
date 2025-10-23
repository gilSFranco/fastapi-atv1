from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()


class Estudante(BaseModel):
    id: int
    nome: str
    email: str


class CriarEstudante(BaseModel):
    nome: str
    email: str


lista_estudantes: List[Estudante] = [
    Estudante(id=1, nome="Gilmar", email="gilmar@gmail.com")
]


@app.get("/estudantes", response_model=List[Estudante])
def listar_estudantes():
    return lista_estudantes


@app.get("/estudantes/{id_estudante}", response_model=Estudante)
def listar_estudante_por_id(id_estudante: int):
    for estudante in lista_estudantes:
        if estudante.id == id_estudante:
            return estudante
    raise HTTPException(status_code=404, detail="Estudante não encontrado.")


@app.post("/estudantes", status_code=201, response_model=Estudante)
def criar_estudante(estudante: CriarEstudante):
    id_gerado = (
        max([estudante.id for estudante in lista_estudantes], default=0) + 1
    )

    novo_estudante = Estudante(
        id=id_gerado, nome=estudante.nome, email=estudante.email
    )
    lista_estudantes.append(novo_estudante)
    return novo_estudante
