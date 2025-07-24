import json
from engine.processing_result import ProcessingResult
from engine.message_processor import MessageProcessor
from azure.servicebus import ServiceBusClient, ServiceBusMessage, ServiceBusReceiver, ServiceBusSender


class RequestQuoteQueue:
    
    __servicebusClient: ServiceBusClient
    __sender : ServiceBusSender
    

    # Private methods -------------------------------------------------------------------------------------
        
    def __init__(self, servicebus_conn_str, request_quote_queue_name) -> None:
        
        self._validateInitArgs(servicebus_conn_str, request_quote_queue_name)        
           
        self._configureServiceBusClient(servicebus_conn_str, request_quote_queue_name)   


    def _configureServiceBusClient(self, servicebus_conn_str, request_quote_queue_name):

        print("Configuring ServiceBus client...")
        
        self.__servicebusClient = ServiceBusClient.from_connection_string(servicebus_conn_str)
        self.__sender = self.__servicebusClient.get_queue_sender(request_quote_queue_name)
       
        print(self.__servicebusClient)
        print(self.__sender)
        
        print("ServiceBus client configured successfully.")


    def _validateInitArgs(self, servicebus_conn_str, request_quote_queue_name):
           
        if not servicebus_conn_str:
            raise ValueError("ServiceBus connection string is not set")
            
        if not request_quote_queue_name:
            raise ValueError("Request quote queue name is not set")            
      

    # Public methods -------------------------------------------------------------------------------------
    
    def sendMessageRequestQuoteQueue(self, message):
        sbmessage = ServiceBusMessage(message)
        self.__sender.send_messages(sbmessage)
        print("Message sent to queue")