import os
import pytest
from main import ler_tarefas_csv, salvar_tarefas_csv_logica

ARQUIVO_NOVO_TESTE = "teste_limpo.csv"

@pytest.fixture(autouse=True)
def preparar_ambiente():
    if os.path.exists(ARQUIVO_NOVO_TESTE):
        os.remove(ARQUIVO_NOVO_TESTE)
    yield
    if os.path.exists(ARQUIVO_NOVO_TESTE):
        os.remove(ARQUIVO_NOVO_TESTE)

def test_deve_criar_arquivo_ao_salvar():
    dados = [("Fazer café", 0)]
    salvar_tarefas_csv_logica(ARQUIVO_NOVO_TESTE, dados)
    
    assert os.path.exists(ARQUIVO_NOVO_TESTE) is True

def test_arquivo_inexistente_deve_retornar_lista_vazia():
    resultado = ler_tarefas_csv("arquivo_fantasma.csv")
    assert type(resultado) == list
    assert len(resultado) == 0

def test_salvar_e_ler_uma_unica_tarefa():
    dados = [("Pagar boletos", 1)]
    salvar_tarefas_csv_logica(ARQUIVO_NOVO_TESTE, dados)
    tarefas_carregadas = ler_tarefas_csv(ARQUIVO_NOVO_TESTE)
    assert len(tarefas_carregadas) == 1
    tarefa_isolada = tarefas_carregadas[0] 
    assert tarefa_isolada[0] == "Pagar boletos"
    assert tarefa_isolada[1] == 1