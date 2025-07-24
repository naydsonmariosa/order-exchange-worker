import json
from src.message_handler import MessageHandler

def main():
    with open("queue_request.json", "r", encoding="utf-8") as f:
        input_message = json.load(f)

    handler = MessageHandler()
    output_message = handler.process(input_message)

    with open("queue_response.json", "w", encoding="utf-8") as f:
        json.dump(output_message, f, indent=4, ensure_ascii=False)

    print("[OK] Mensagem processada com sucesso.")

if __name__ == "__main__":
    main()
