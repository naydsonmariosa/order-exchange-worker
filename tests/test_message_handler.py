import pytest
from src.message_handler import MessageHandler

@pytest.fixture
def default_message():
    return {
        "numeroPedido": "13213213221",
        "valor": "10.00",
        "moedaCotacao": "USD",
        "dataPedido": "2025-07-01",
        "tipo_boletim": "INTERMEDIÁRIO"
    }

def test_process_with_mocked_exchange(monkeypatch, default_message):
    class MockService:
        def get_exchange_rate(self, moeda, data, tipo_boletim):
            return 5.0

    monkeypatch.setattr("src.message_handler.ExchangeService", MockService)

    handler = MessageHandler()
    result = handler.process(default_message)

    assert result["valorCotacaoMoeda"] == "5.00"
    assert result["valorCotacaoPedido"] == "50.00"

def test_moeda_invalida(monkeypatch, default_message):
    default_message["moedaCotacao"] = "XXX"

    class MockService:
        def get_exchange_rate(self, moeda, data, tipo_boletim):
            return 0.0  # Simula moeda inexistente

    monkeypatch.setattr("src.message_handler.ExchangeService", MockService)

    handler = MessageHandler()
    result = handler.process(default_message)

    assert result["valorCotacaoMoeda"] == "0.00"
    assert result["valorCotacaoPedido"] == "0.00"    

def test_valor_fracionado(monkeypatch, default_message):
    default_message["valor"] = "7.25"

    class MockService:
        def get_exchange_rate(self, moeda, data, tipo_boletim):
            return 4.50

    monkeypatch.setattr("src.message_handler.ExchangeService", MockService)

    handler = MessageHandler()
    result = handler.process(default_message)

    assert result["valorCotacaoMoeda"] == "4.50"
    assert result["valorCotacaoPedido"] == "32.62"