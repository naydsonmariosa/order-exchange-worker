from engine.message_processor import MessageProcessor
from engine.processing_result import ProcessingResult
from exchange_service import ExchangeService
from models import CotacaoRequest, CotacaoResponse
from utils import round_decimal

class MessageHandler(MessageProcessor):
    
    def __init__(self):
        self.exchange_service = ExchangeService()

    
    def processMessage(self, data) -> ProcessingResult:
    
        processingResult: ProcessingResult = None
        
        try:
            payload = self.process(data)
        
            processingResult = ProcessingResult(suceeded=True, payload=payload.model_dump_json())
            
        except Exception as e:
            print(f"[ERROR] Failed to process message: {e}")
            processingResult = ProcessingResult(suceeded=False, payload=None)
        
        return processingResult


    def process(self, raw_message: dict) -> CotacaoResponse:
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

        return response