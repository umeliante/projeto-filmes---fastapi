from fastapi import FastAPI
import funcao

#Como executar o fastapi
# python -m uvicorn main:app --reload


app = FastAPI(title="Gerenciador de filmes")

#Criando a rota inicial
@app.get("/")
def home():
    return {"mensagem": "Bem-vindo ao gerenciador de filmes"}

@app.post("/filmes")
def criar_filme(titulo: str, genero: str, ano: int, nota: float):
    funcao.cadastrar_filme(titulo, genero, ano, nota)
    return{"200": "Filme cadastrado com sucesso!"}

@app.get("/filmes")
def listar_filmes():
    filmes = funcao.listar_filme()
    lista = []
    for linha in filmes:
        lista.append(
            {
                "id": linha[0],
                "titulo": linha[1],
                "gerero": linha[2],
                "ano": linha[3],
                "nota": linha[4]
            }
        )
    return{"filmes": lista}

@app.delete("/filmes/{id_filmes}")
def deletar_filme(id_filmes: int):
    filmes = funcao.buscar_filme(id_filmes)
    if filmes:
        funcao.deletar_filme(id_filmes)
        return {"mensagem": "Filme excluído com sucesso!"}
    else:
        return {"erro:": "Filme não encontrado"}
    
@app.put("/filmes/{id_filmes}")
def atulizar_filme(id_filmes: int):
    filmes = funcao.atualizar_filme(id_filmes)
    if filmes:
        funcao.atualizar_filme(id_filmes)
        return {"mensagem": "Filme atualizado com sucesso!"}
    else:
        return {"erro:": "Filme não encontrado"}

