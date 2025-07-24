# Desafio Clean Code com Fila e API de Cotação

## Objetivo

Você deve criar um microserviço que:

1. Leia uma mensagem JSON de uma fila (simulada por `queue_request.json`)
2. Chame a API de cotação de moeda do BrasilAPI
3. Calcule o valor do pedido na moeda especificada
4. Publique uma nova mensagem (em `queue_response.json`) com a cotação e o valor convertido

## Mensagem de entrada

```json
{
  "numeroPedido": "13213213221",
  "valor": "10.00",
  "moedaCotacao": "USD",
  "dataPedido": "2025-01-01",
  "tipo_boletim": "INTERMEDIÁRIO"
}
```

## Resposta esperada

```json
{
  "numeroPedido": "13213213221",
  "valor": "10.00",
  "moedaCotacao": "USD",
  "dataPedido": "2025-01-01",
  "valorCotacaoMoeda": "5.67",
  "valorCotacaoPedido": "56.70",
  "tipo_boletim": "INTERMEDIÁRIO"
}
```

## Avaliação

- Código limpo e bem estruturado
- Nomes claros e responsabilidades separadas
- Testes para funções críticas
- Uso correto da API e tratamento de erros

## Rodando

```bash
pip install -r requirements.txt
python main.py
```

## Testando

```bash
pytest
```
