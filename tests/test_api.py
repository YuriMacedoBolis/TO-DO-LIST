import pytest
import requests
from unittest.mock import patch
from main import obter_clima_atual

def test_deve_retornar_temperatura_da_api():
    # Teste de Integração: Bate na API real e verifica se retorna um número (float)
    temperatura = obter_clima_atual()
    assert isinstance(temperatura, float)

@patch('main.requests.get')
def test_falha_na_api_deve_lancar_excecao(mock_get):
    # Mock: Simula uma falha de conexão para garantir que a função lida bem com erros
    mock_get.side_effect = requests.exceptions.RequestException("Erro de conexão")
    
    with pytest.raises(requests.exceptions.RequestException):
        obter_clima_atual()