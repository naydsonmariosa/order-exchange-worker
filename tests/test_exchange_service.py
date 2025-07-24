import pytest
from src.exchange_service import ExchangeService, BulletinType

@pytest.fixture
def service():
    return ExchangeService()

def test_valid_abertura(service):
    """Deve retornar a cotação de compra do boletim ABERTURA"""
    rate = service.get_exchange_rate("USD", "2025-07-01", BulletinType.ABERTURA)
    assert rate > 0, "A cotação de abertura deve ser maior que zero"

def test_valid_fechamento(service):
    """Deve retornar a cotação de compra do boletim FECHAMENTO PTAX"""
    rate = service.get_exchange_rate("USD", "2025-07-01", BulletinType.FECHAMENTO_PTAX)
    assert rate > 0, "A cotação de fechamento deve ser maior que zero"

def test_valid_intermediario_media(service):
    """Deve retornar a média das cotações de compra do boletim INTERMEDIÁRIO"""
    rate = service.get_exchange_rate("USD", "2025-07-01", BulletinType.INTERMEDIARIO)
    assert rate > 0, "A média da cotação intermediária deve ser maior que zero"

def test_invalid_currency_returns_zero(service):
    """Moeda inexistente deve retornar 0.0"""
    rate = service.get_exchange_rate("XXX", "2025-07-01", BulletinType.ABERTURA)
    assert rate == 0.0

def test_invalid_date_returns_zero(service):
    """Data inválida deve retornar 0.0"""
    rate = service.get_exchange_rate("USD", "9999-99-99", BulletinType.ABERTURA)
    assert rate == 0.0

def test_boletim_inexistente(service):
    """Tipo de boletim inexistente deve retornar 0.0"""
    rate = service.get_exchange_rate("USD", "2025-07-01", "BOLETIM_FANTASIA")
    assert rate == 0.0
