"""O motor de técnicas do Capítulo Seis, em código.

Serve para duas coisas: conferir as contas das técnicas impressas no livro, e
montar as técnicas que os lutadores do simulador usam.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from regras import TAMANHO_MAXIMO

DURACAO = {"instantanea": 1, "sustentada": 2, "cena": 4}
ATIVACAO = {"acao": 0, "bonus": 1, "reacao": 1}

# O custo do alcance depende da natureza: o Cosmo já nasce com alcance curto,
# o Golpe nasce no toque.
ALCANCE = {
    "cosmo": {"pessoal": 0, "toque": 0, "curto": 0, "medio": 1, "longo": 2, "vista": 3},
    "golpe": {"pessoal": 0, "toque": 0, "curto": 1, "medio": 2, "longo": 3, "vista": 4},
}

# Pontos por efeito. Condições custam pelo grau delas; teletransporte custa 2.
PESO = {
    "dano": 1, "area": 1, "continuo": 1, "pv_temp": 1, "cura": 1, "defesa": 1,
    "movimento": 1, "empurrar": 1, "teleporte": 2, "vantagem": 1,
    "cond_fraca": 1, "cond_media": 2, "cond_forte": 4,
}


@dataclass
class Tecnica:
    nome: str
    natureza: str                       # "golpe" ou "cosmo"
    efeitos: dict = field(default_factory=dict)   # efeito -> quantidade
    duracao: str = "instantanea"
    ativacao: str = "acao"
    alcance: str = "toque"
    area_dobrada: bool = False
    area_seletiva: bool = False
    mais: tuple = ()                    # modificadores de +1, por nome
    limitacoes: int = 0                 # quantos −1
    grau: int = 1
    assento: bool = False               # Golpe do Assento: +1 no tamanho máximo
    condicao: str = ""                  # a condição que impõe (o peso está em efeitos)
    limites: tuple = ()                 # as limitações, por nome, para o simulador:
                                        # fere · desprevenido · uma_vez · carregar · teto

    # ------------------------------------------------------------------
    def pontos_de_efeito(self) -> int:
        return sum(PESO[k] * v for k, v in self.efeitos.items())

    def tamanho(self) -> int:
        t = DURACAO[self.duracao]
        t += max(0, self.pontos_de_efeito() - 1)   # o primeiro vem na duração
        t += ALCANCE[self.natureza][self.alcance]
        t += ATIVACAO[self.ativacao]
        t += 2 if self.area_dobrada else 0
        t += 1 if self.area_seletiva else 0
        t += len(self.mais)
        return max(1, t)

    def custo(self) -> int:
        t = self.tamanho()
        piso = -(-t // 2)
        return max(1, piso, t - self.limitacoes)

    def tamanho_maximo(self) -> int:
        return TAMANHO_MAXIMO[self.grau] + (1 if self.assento else 0)

    def valida(self) -> bool:
        return self.tamanho() <= self.tamanho_maximo()

    # ------------------------------------------------------------------
    @property
    def dados_de_dano(self) -> int:
        """Quantos dados a técnica rola: pontos de dano × Grau."""
        return (self.efeitos.get("dano", 0) + self.efeitos.get("area", 0)) * self.grau

    @property
    def lado(self) -> int:
        return 8 if self.efeitos.get("dano") else 6

    @property
    def atravessa(self) -> bool:
        return "atravessa" in self.mais

    @property
    def quebra(self) -> bool:
        return "quebra" in self.mais


def tecnica_de_dano(pontos: int, grau: int, natureza: str = "golpe",
                    mais: tuple = (), nome: str = "") -> Tecnica:
    """Uma técnica de dano puro em alvo único, instantânea, no toque."""
    return Tecnica(nome or f"dano {pontos}", natureza, {"dano": pontos},
                   mais=mais, grau=grau)
