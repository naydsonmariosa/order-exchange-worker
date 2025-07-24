from quote_request.quote_request_queue import RequestQuoteQueue
from quote_request.quote_request_producer import QuoteRequestProducer   

servicebus_conn_str = "Endpoint=sb://omnichain-dev.servicebus.windows.net/;SharedAccessKeyName=OmniChainApp;SharedAccessKey=24V4l/5mSTbbiFDcVDvd3s3co4JDr2gkQ+ASbNXq6WI="
input_queue_name  = "sc-puc-entrypoint"


requestQuoteQueue = RequestQuoteQueue(
    servicebus_conn_str = servicebus_conn_str,
    request_quote_queue_name = input_queue_name
)

quoteRequestProducer = QuoteRequestProducer(requestQuoteQueue)

quoteRequestProducer.generateQuoteRequest()