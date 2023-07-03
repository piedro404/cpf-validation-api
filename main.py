from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from cpf import CPF # Importa meu modulo CPF


app = FastAPI()

# Configura o middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_methods=["*"], 
    allow_headers=["*"], 
    allow_credentials=True, 
    allow_origins=["*"],
)

# Define a rota inicial ("/") da API que retorna um JSON com uma descrição
@app.get("/")
def home():
    return {
        "Status": True,
        "Description": "Api de validação CPF ON!"
    }

# Define a rota "/cpf/valid/{cpf}" que recebe um CPF e retorna um JSON com o resultado da validação
@app.get("/cpf/valid/{cpf}", tags=["CPF","Validador"])
def valida_cpf(cpf:str):
    cpf_s = CPF.valid_cpf(cpf)
    return {
        "Valid": cpf_s[0],
        "CPF": cpf_s[1],
        "Status": cpf_s[2]
    }

# Define a rota "/cpf/generator/{qtd}" que recebe a quantidade de CPFs a serem gerados e retorna uma lista de CPFs
@app.get("/cpf/generator/{qtd}", tags=["CPF","Gerador"])
def gerar_cpf(qtd:int):
    cpfs = CPF.gerarCPFs(qtd)
    return cpfs


uvicorn.run(app) # Iniciar a API
