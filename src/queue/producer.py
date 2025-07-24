import json

def enviar_resposta(mensagem):
    print(f"Resposta final: {mensagem}")
    with open("queue_response.json", "w") as f:
        json.dump(mensagem, f, indent=2)
