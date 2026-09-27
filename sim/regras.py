"""Os números do livro num lugar só.

Tudo que o simulador usa e que também está escrito no livro mora aqui. Quando
um número muda no livro, ele muda aqui primeiro — e o test.py confere se o que
está impresso bate com o que foi medido.
"""

from __future__ import annotations

import math

# ---------------------------------------------------------------------------
# Progressão
# ---------------------------------------------------------------------------


def prof(nivel: int) -> int:
    """+2 nos níveis 1–4, +3 nos 5–8 … +6 nos 17–20."""
    return 2 + (nivel - 1) // 4


def grau(nivel: int) -> int:
    """O Grau acompanha a proficiência: 1 nos níveis 1–4 … 5 nos 17–20."""
    return 1 + (nivel - 1) // 4


def teto_base(nivel: int) -> int:
    """Teto de Cosmo sem nada somado."""
    return 3 + prof(nivel)


TAMANHO_MAXIMO = {1: 5, 2: 6, 3: 6, 4: 6, 5: 6}

# PV: cada Grau tem uma base, e a Constituição soma a cada nível. A base sobe
# junto com o dano das técnicas, que também cresce por Grau — assim a luta
# dura parecido do começo ao fim de cada faixa, sem o dente de serra de uma
# vida que cresce todo nível contra um dano que só cresce de quatro em quatro.
PV_POR_GRAU = {1: 18, 2: 38, 3: 58, 4: 78, 5: 98}
PV_POR_NIVEL = 1   # além da CON, dentro da faixa


def pv_maximo(nivel: int, con: int, extra_por_nivel: int = 0) -> int:
    return (PV_POR_GRAU[grau(nivel)] + PV_POR_NIVEL * (nivel - 1 - 4 * (grau(nivel) - 1))
            + con * nivel + extra_por_nivel * nivel)


def mod(valor: int) -> int:
    return (valor - 10) // 2


# Os seis valores e os aumentos de atributo (+2 nos níveis 4, 8, 12, 16, 19).
DISTRIBUICAO = (15, 14, 13, 12, 10, 8)
NIVEIS_DE_ATRIBUTO = (4, 8, 12, 16, 19)


def atributo_no_nivel(inicial: int, nivel: int, prioridade: int = 0) -> int:
    """O atributo principal recebe todos os aumentos até 20; o segundo, o resto.

    prioridade 0 = atributo principal, 1 = segundo atributo."""
    pontos = 2 * sum(1 for n in NIVEIS_DE_ATRIBUTO if n <= nivel)
    if prioridade == 0:
        return min(20, inicial + pontos)
    sobra = max(0, pontos - (20 - 15))
    return min(20, inicial + sobra)


def tecnicas_conhecidas(nivel: int) -> int:
    return 2 + sum(1 for n in (4, 8, 12, 16, 20) if n <= nivel)


def gloria_para_subir(nivel: int) -> int:
    """Glória que você precisa juntar para sair deste nível."""
    return 3 if nivel <= 4 else (4 if nivel <= 12 else 5)


def conviccoes(nivel: int) -> int:
    return 4 if nivel >= 14 else 3


def cosmo_inicial(mod_cosmo: int, nivel: int) -> int:
    extra = (1 if nivel >= 3 else 0) + (1 if nivel >= 15 else 0)
    return max(1, mod_cosmo) + extra


NIVEL_ATAQUE_EXTRA = 9


def ataques_por_golpe(nivel: int) -> int:
    return 2 if nivel >= NIVEL_ATAQUE_EXTRA else 1


def dado_de_queima(nivel: int) -> int:
    """Queimar custa 1d4 por ponto, vezes o Grau da técnica."""
    return 4


def resistencia_por_nivel(nivel: int) -> int:
    """+1 de Resistência nos níveis 5, 7, 13 e 17 (é sua, não da armadura)."""
    return sum(1 for n in (5, 7, 13, 17) if n <= nivel)


# ---------------------------------------------------------------------------
# Posto e armadura
# ---------------------------------------------------------------------------

POSTO = {
    # posto: (bônus de DEF, Resistência)
    "bronze": (2, 3),
    "prata": (4, 4),
    "ouro": (6, 5),
    "divina": (7, 6),
}

# A Hierarquia: um Prata diante de um Bronze soma isto nas rolagens contra
# ele, e o Bronze perde isto nas rolagens contra o Prata. A elite não usa a
# Hierarquia: ela tem o Sétimo quando quer e o domínio.
HIERARQUIA = 2

# A forma nova: cada vez que a armadura revive, o sangue deixa um bônus
# permanente (DEF, Resistência). Quanto mais forte o sangue, maior o bônus.
FORMA = {
    "guerreiro": (1, 1),
    "elite": (2, 2),
    "deus": (3, 3),
}
REVIVIDAS_MAX = {"guerreiro": 3, "elite": 1, "deus": 1}


def bonus_das_formas(formas: tuple) -> tuple[int, int]:
    """(DEF, Resistência) somados de todas as formas que a armadura já teve."""
    return (sum(FORMA[f][0] for f in formas), sum(FORMA[f][1] for f in formas))

# Requisito de nível para subir de Posto (o momento vem da história)
NIVEL_PRATA = 9
NIVEL_ELITE = 15


def posto_existe(posto: str, nivel: int) -> bool:
    """Se alguém desse Posto pode ter esse nível."""
    minimo = {"prata": NIVEL_PRATA, "ouro": NIVEL_ELITE, "divina": NIVEL_ELITE}.get(posto, 1)
    return nivel >= minimo

# ---------------------------------------------------------------------------
# Sentidos
# ---------------------------------------------------------------------------

DEGRAU = {"sexto": 0, "setimo": 1, "nono": 2}
TETO_SETIMO = 2
DOMINIO_OURO = 3   # bônus do Sétimo dominado do Ouro contra um Sétimo despertado
TETO_NONO = 2

# ---------------------------------------------------------------------------
# Cosmo
# ---------------------------------------------------------------------------

COSMO_RELOGIO = 1          # por turno, a partir da segunda rodada
COSMO_ACERTO = 1           # golpe comum que acerta
COSMO_POR_CADA_ACERTO = False  # True: +1 por golpe que acerta; False: uma vez por turno
COSMO_CONCENTRAR = 2
COSMO_CENTELHA = 1
CENTELHA_VANTAGEM = True    # a Centelha dá Vantagem no próximo ataque
TETO_CENTELHA_MAX = 3
BONUS_LIDO = 2
LEVANTAR_POR_LUTA = 1      # quantas vezes se levanta numa mesma luta
MIL_DIAS_SEGMENTOS = 6
APARAR_USA_REACAO = True


def media_dado(lados: int) -> float:
    return (lados + 1) / 2


def ceil_div(a: int, b: int) -> int:
    return -(-a // b)


def arred_cima(x: float) -> int:
    return int(math.ceil(x))
