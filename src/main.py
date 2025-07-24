# main.py
from message_handler import MessageHandler
from engine.broker_client import BrokerClient


input_queue_name  = "sc-puc-entrypoint"
output_queue_name = "sc-puc-output"
dlq_queue_name    = "sc-puc-dlq"


def main():
    
    messageProcessor = MessageHandler()

    brokerClient = BrokerClient(
        message_processor    = messageProcessor,
        servicebus_conn_str  = servicebus_conn_str,
        input_queue_name     = input_queue_name,
        output_queue_name    = output_queue_name,
        dlq_queue_name       = dlq_queue_name
    )

    brokerClient.listenForNewMessages()


if __name__ == "__main__":
    main()
