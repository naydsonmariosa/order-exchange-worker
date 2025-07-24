import json
from engine.processing_result import ProcessingResult
from engine.message_processor import MessageProcessor
from azure.servicebus import ServiceBusClient, ServiceBusMessage, ServiceBusReceiver, ServiceBusSender
#from azure.servicebus import ServiceBusMessage

import traceback

class BrokerClient:
    
    __messageProcessor: MessageProcessor
    __servicebusClient: ServiceBusClient
    __receiver : ServiceBusReceiver
    __sender : ServiceBusSender
    __dlqSender : ServiceBusSender
    

    # Private methods -------------------------------------------------------------------------------------
        
    def __init__(self, message_processor, servicebus_conn_str, input_queue_name, output_queue_name, dlq_queue_name) -> None:                
        
        self._validateInitArgs(message_processor, servicebus_conn_str, input_queue_name, output_queue_name)        
           
        self._configureServiceBusClient(servicebus_conn_str, input_queue_name, output_queue_name, dlq_queue_name)
        
        self.__messageProcessor = message_processor


    def _configureServiceBusClient(self, servicebus_conn_str, input_queue_name, output_queue_name, dlq_queue_name):

        print("Configuring ServiceBus client...")
        
        self.__servicebusClient = ServiceBusClient.from_connection_string(servicebus_conn_str)
        self.__receiver = self.__servicebusClient.get_queue_receiver(input_queue_name)
        self.__sender = self.__servicebusClient.get_queue_sender(output_queue_name)
        self.__dlqSender = self.__servicebusClient.get_queue_sender(dlq_queue_name)
        
        print(self.__servicebusClient)
        print(self.__receiver)
        print(self.__sender)
        print(self.__dlqSender)
        
        print("ServiceBus client configured successfully.")


    def _validateInitArgs(self, messageProcessor, servicebus_conn_str, input_queue_name, output_queue_name):

        if not messageProcessor:
            raise ValueError("MessageProcessor is not set")
            
        if not servicebus_conn_str:
            raise ValueError("ServiceBus connection string is not set")
            
        if not input_queue_name:
            raise ValueError("Input queue name is not set")
            
        if not output_queue_name:
            raise ValueError("Output queue name is not set")
    
    
    def _processMessage(self, message):

        print("New message received: *************************")
        strMessage = str(message)
        print(strMessage)
        
        payload = json.loads(strMessage)
        
        try:
                        
            resultingProcess = self.__messageProcessor.processMessage(payload)
        
            if resultingProcess.suceeded:
                print("Message processed successfully.")
                #resultingPayload = json.dumps(resultingProcess.payload)
                self._sendMessageToOutputQueue(resultingProcess.payload)
            else:
                print("Message processing failed.")
                self._sendMessageToDlqQueue(message)

        except Exception as e:
            
            print("Falied processing message:")
            print(e)
            traceback.print_exc()
            
            self._sendMessageToDlqQueue(message)


    def _sendMessageToOutputQueue(self, message):
        sbmessage = ServiceBusMessage(message)
        self.__sender.send_messages(sbmessage)
        print(f"Sent message to output queue: {message}")

        
    def _sendMessageToDlqQueue(self, message):
        sbmessage = ServiceBusMessage(message)
        self.__dlqSender.send_messages(sbmessage)
        print(f"Sent message to DLQ: {message}")            


    # Public methods -------------------------------------------------------------------------------------
    
    def listenForNewMessages(self):
        print("Listenming for new messages...")
        with self.__receiver:
            for message in self.__receiver:
                self._processMessage(message)
                self.__receiver.complete_message(message)
