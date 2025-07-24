import json

class Producer:
    def produce(self, message: dict) -> None:
        with open("queue_response.json", "w", encoding="utf-8") as f:
            json.dump(message, f, indent=2)
