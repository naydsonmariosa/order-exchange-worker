import json
from src.exchange_service import obter_cotacao
from queue.producer import enviar_resposta

def processar_mensagem():
    with open("queue_request.json", "r", encoding="utf-8") as f:
        mensagem = json.load(f)

    cotacao = obter_cotacao(
        mensagem["moedaCotacao"],
        mensagem["dataPedido"],
        mensagem["tipo_boletim"]
    )

    valor_pedido = float(mensagem["valor"])
    valor_convertido = round(valor_pedido * cotacao, 2)

    resposta = {
        **mensagem,
        "valorCotacaoMoeda": f"{cotacao:.2f}",
        "valorCotacaoPedido": f"{valor_convertido:.2f}"
    }

    enviar_resposta(resposta)
