import json
from quote_request.quote_request_queue import RequestQuoteQueue
from datetime import date, timedelta
import random
import time

class QuoteRequestProducer:
    
    __requestQuoteQueue: RequestQuoteQueue
    
    
    # Private methods -------------------------------------------------------------------------------------
    
    def __init__(self, requestQuoteQueue):
                
        
        self._validateInitArgs(requestQuoteQueue)
        
        self.__requestQuoteQueue = requestQuoteQueue
        
        
    def _validateInitArgs(self, requestQuoteQueue):
           
        if not requestQuoteQueue:
            raise ValueError("RequestQuoteQueue is not set")


    # Public methods -------------------------------------------------------------------------------------
    
    
    def generateQuoteRequest(self):
        
        lastday = date.today() - timedelta(days=1)        
        
        while True:
            try:
                valor = random.randint(1, 30000)
                numeroPedido = random.randint(100000, 999999)
                randomDay = random.randint(1, 28)
                dataPedido = lastday - timedelta(days=randomDay)
                tipo_boletim = random.choice(["INTERMEDIÁRIO", "ABERTURA", "FECHAMENTO PTAX"])
                
                quoteRequest = {
                    "numeroPedido": numeroPedido,
                    "valor": valor,
                    "moedaCotacao": "USD",
                    "dataPedido": dataPedido.strftime("%Y-%m-%d"),
                    "tipo_boletim": tipo_boletim
                }

                self.__requestQuoteQueue.sendMessageRequestQuoteQueue(json.dumps(quoteRequest))
                print(f"Quote request generated and sent: {quoteRequest}")
                
                time.sleep(1) 
            except Exception as e:
                print(f"Error generating quote request: {e}")
                print("Retrying...")
                continue