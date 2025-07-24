from pydantic import BaseModel, Field
from typing import Literal


class CotacaoRequest(BaseModel):
    numeroPedido: int
    valor: float
    moedaCotacao: str
    dataPedido: str  # YYYY-MM-DD
    tipo_boletim: Literal["INTERMEDIÁRIO", "ABERTURA", "FECHAMENTO PTAX"]


class CotacaoResponse(CotacaoRequest):
    valorCotacaoMoeda: str = Field(..., description="Cotação da moeda no dia")
    valorCotacaoPedido: str = Field(..., description="Valor convertido do pedido")
