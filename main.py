# main.py
from src.queue.consumer import Consumer
from src.queue.producer import Producer
from src.message_handler import MessageHandler

def main():
    consumer = Consumer()
    producer = Producer()
    handler = MessageHandler()

    input_message = consumer.consume()
    output_message = handler.process(input_message)
    producer.produce(output_message)

    print("[OK] Mensagem processada com sucesso.")

if __name__ == "__main__":
    main()
