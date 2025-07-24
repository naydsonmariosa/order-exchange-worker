import json

class Consumer:
    def __init__(self, filepath: str = "queue_request.json"):
        self.filepath = filepath

    def consume(self) -> dict:
        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                return json.load(f)
        except (OSError, json.JSONDecodeError) as e:
            print(f"[Consumer] Erro ao ler arquivo: {e}")
            return {}
