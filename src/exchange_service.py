import requests
from enum import Enum
from typing import List, Dict


class BulletinType(str, Enum):
    """Enum com os tipos de boletins suportados."""
    INTERMEDIARIO = "INTERMEDIÁRIO"
    ABERTURA = "ABERTURA"
    FECHAMENTO_PTAX = "FECHAMENTO PTAX"


class ExchangeService:
    API_URL = "https://brasilapi.com.br/api/cambio/v1/cotacao/{currency}/{date}"

    def get_exchange_rate(self, currency: str, date: str, bulletin_type: str) -> float:
        """
        Retorna a cotação de compra da moeda informada para a data e tipo de boletim.
        Se o tipo for INTERMEDIÁRIO, retorna a média das cotações de compra desse tipo.
        """
        try:
            url = self.API_URL.format(currency=currency.upper(), date=date)
            response = requests.get(url)
            response.raise_for_status()

            data = response.json()
            rates = data.get("cotacoes", [])
            return self._calculate_rate_by_bulletin(rates, bulletin_type)

        except (requests.RequestException, ValueError) as e:
            print(f"[ExchangeService] Erro ao buscar cotação: {e}")
            return 0.0

    def _calculate_rate_by_bulletin(self, rates: List[Dict], bulletin_type: str) -> float:
        """
        Calcula a cotação com base no tipo de boletim.
        Para INTERMEDIÁRIO, calcula a média. Para os demais, retorna a primeira ocorrência.
        """
        normalized_type = bulletin_type.upper()

        if normalized_type == BulletinType.INTERMEDIARIO:
            return self._calculate_intermediario_average(rates)

        return self._get_first_rate(rates, normalized_type)

    def _calculate_intermediario_average(self, rates: List[Dict]) -> float:
        """
        Retorna a média das cotações de compra do boletim INTERMEDIÁRIO.
        """
        values = [
            rate["cotacao_compra"]
            for rate in rates
            if rate.get("tipo_boletim", "").upper() == BulletinType.INTERMEDIARIO
        ]
        return round(sum(values) / len(values), 6) if values else 0.0

    def _get_first_rate(self, rates: List[Dict], bulletin_type: str) -> float:
        """
        Retorna a primeira cotação de compra correspondente ao tipo de boletim informado.
        """
        for rate in rates:
            if rate.get("tipo_boletim", "").upper() == bulletin_type:
                return float(rate.get("cotacao_compra", 0.0))
        return 0.0
