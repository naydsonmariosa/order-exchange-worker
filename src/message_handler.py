from src.exchange_service import ExchangeService
from src.models import CotacaoRequest, CotacaoResponse
from src.utils import round_decimal

class MessageHandler:
    def __init__(self):
        self.exchange_service = ExchangeService()

    def process(self, raw_message: dict) -> dict:
        message = CotacaoRequest(**raw_message)

        rate = self.exchange_service.get_exchange_rate(
            message.moedaCotacao,
            message.dataPedido,
            message.tipo_boletim
        )

        valor_float = float(message.valor)
        valor_convertido = round_decimal(valor_float * rate)

        response = CotacaoResponse(
            **message.model_dump(),
            valorCotacaoMoeda=round_decimal(rate),
            valorCotacaoPedido=valor_convertido
        )

        return response.model_dump()