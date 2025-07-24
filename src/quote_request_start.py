from quote_request.quote_request_queue import RequestQuoteQueue
from quote_request.quote_request_producer import QuoteRequestProducer   

servicebus_conn_str = ""
input_queue_name  = "sc-puc-entrypoint"


requestQuoteQueue = RequestQuoteQueue(
    servicebus_conn_str = servicebus_conn_str,
    request_quote_queue_name = input_queue_name
)

quoteRequestProducer = QuoteRequestProducer(requestQuoteQueue)

quoteRequestProducer.generateQuoteRequest()