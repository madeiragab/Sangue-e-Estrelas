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

# PV: cada Grau tem uma base, e a Constituição soma a cada nível. A base cresce
# mais rápido que o dano das técnicas: a luta é curta e decisiva no começo e
# longa e destrutiva no fim (pedido do usuário, 0.6.0).
PV_POR_GRAU = {1: 14, 2: 40, 3: 80, 4: 135, 5: 205}
# Cada escolha de Vida soma VIGOR_PV por Grau — e cresce junto quando o Grau sobe.
VIGOR_PV = 2


def pv_maximo(nivel: int, con: int, vigor: int = 0, extra_por_nivel: int = 0) -> int:
    g = grau(nivel)
    return PV_POR_GRAU[g] + con * nivel + round(vigor * VIGOR_PV * g) + extra_por_nivel * nivel


# ---------------------------------------------------------------------------
# Progressão por escolha
# ---------------------------------------------------------------------------

# Todo nível do 2 ao 20: Vida ou Cosmo. Nestes níveis, também: uma técnica nova
# ou +2 num atributo; e nestes outros, uma perícia ou uma defesa treinada.
NIVEIS_TECNICA_OU_ATRIBUTO = (4, 6, 8, 10, 12, 14, 16, 18, 20)
NIVEIS_PERICIA_OU_DEFESA = (3, 7, 11, 15, 19)


def escolhas_padrao(nivel: int) -> dict:
    """As escolhas do lutador de referência: Vida e Cosmo alternados (Vida no 2),
    técnica nova nos níveis 4, 8, 12, 16 e 20 e atributo nos outros, e a terceira
    defesa treinada no 11."""
    vc = "".join("v" if n % 2 == 0 else "c" for n in range(2, nivel + 1))
    ta = "".join("t" if n % 4 == 0 else "a" for n in NIVEIS_TECNICA_OU_ATRIBUTO if n <= nivel)
    pd = "".join("d" if n == 11 else "p" for n in NIVEIS_PERICIA_OU_DEFESA if n <= nivel)
    return {"vida_cosmo": vc, "tecnica_atributo": ta, "pericia_defesa": pd}


def atributos_das_escolhas(escolhas: dict, principal: int = 15, segundo: int = 14) -> tuple[int, int]:
    """Cada 'a' dá +2: no principal até 20, o resto no segundo."""
    pontos = 2 * escolhas["tecnica_atributo"].count("a")
    p = min(20, principal + pontos)
    s = min(20, segundo + max(0, principal + pontos - 20))
    return p, s


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


def cosmo_inicial(mod_cosmo: int, escolhas_de_cosmo: int, teto: int) -> int:
    """O modificador (mínimo 1), +1 por escolha de Cosmo, até o Teto."""
    return min(teto, max(1, mod_cosmo) + escolhas_de_cosmo)


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

# Sozinho contra muitos: um inimigo com Convicções que luta sozinho contra um
# grupo multiplica os PV e ganha ações a mais por rodada.
def chefe_pv(oponentes: int) -> float:
    """× 1¼, 1½, 1¾, 2, 2¼ para 2 a 6 oponentes."""
    return (oponentes + 3) / 4 if oponentes >= 2 else 1.0


CHEFE_ACAO_SO_GOLPE = True    # a ação a mais do chefe é só um golpe comum


def chefe_acoes(oponentes: int) -> int:
    """0, 1, 2, 3, 4 golpes comuns a mais por rodada para 2 a 6 oponentes."""
    return max(0, oponentes - 2)


# Características da armadura: quantas por Posto, e as que o simulador dá aos
# lutadores de referência (as de efeito médio, medidas em sim/extremos.py).
CARACTERISTICAS_POR_POSTO = {"bronze": 1, "prata": 2, "ouro": 3}
CARACTERISTICAS_PADRAO = ("ressonante", "ofuscante", "pesada")


# Uma condição forte, quando acaba, não volta com a mesma técnica no mesmo alvo
# naquela luta: o mesmo golpe não funciona duas vezes.
CONDICOES_FORTES = ("atordoado", "paralisado")

# A Hierarquia: um Prata diante de um Bronze soma isto nas rolagens contra
# ele, e o Bronze perde isto nas rolagens contra o Prata. A elite não usa a
# Hierarquia: ela tem o Sétimo quando quer e o domínio.
HIERARQUIA = 2

# A forma nova: cada vez que a armadura revive, o sangue deixa um bônus
# permanente, pequeno. As formas de guerreiro alternam: a 1ª, 3ª, 5ª… dão +1 no
# acerto; a 2ª, 4ª, 6ª… dão +1 de Resistência.
FORMA = {
    "guerreiro": {},
    "elite": {"def": 1},
    "deus": {"def": 1, "acerto": 1},
}
# Quantas vezes cada armadura revive com cada sangue. Quanto mais alto o Posto,
# mais vidas. A armadura de elite não tem o degrau de elite: para ela, o sangue
# de elite é o sangue normal, e conta como de guerreiro.
REVIVIDAS_MAX = {
    "guerreiro": {"bronze": 3, "prata": 4, "ouro": 6},
    "elite": {"bronze": 1, "prata": 1, "ouro": 0},
    "deus": {"bronze": 1, "prata": 1, "ouro": 1},
}
FORCA_DO_SANGUE = {"guerreiro": 0, "elite": 1, "deus": 2}


def formas_validas(posto: str, formas: tuple) -> bool:
    """A escada: cada sangue igual ou mais forte que o anterior, dentro do limite."""
    if posto not in REVIVIDAS_MAX["guerreiro"]:
        return not formas
    forcas = [FORCA_DO_SANGUE[f] for f in formas]
    if forcas != sorted(forcas):
        return False
    return all(formas.count(s) <= REVIVIDAS_MAX[s][posto] for s in FORMA)


def bonus_das_formas(formas: tuple) -> dict:
    """DEF, Resistência e acerto somados de todas as formas que a armadura já teve."""
    g = formas.count("guerreiro")
    total = {"def": 0, "res": g // 2, "acerto": (g + 1) // 2}
    for f in formas:
        for k, v in FORMA[f].items():
            total[k] += v
    return total

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

# O Cosmo não acaba: gastar nunca o leva abaixo do piso. O piso é o modificador do
# Atributo do Cosmo (mínimo 1). PISO_COSMO muda a regra para medir alternativas:
# "mod" (o modificador), "um" (sempre 1), "metade" (metade do modificador, mínimo 1).
PISO_COSMO = "um"
PISO_POR_COSMO = 0.5   # cada escolha de Cosmo sobe o piso meio ponto: +1 a cada duas


def piso_cosmo(mod_cosmo: int) -> int:
    if PISO_COSMO == "um":
        return 1
    if PISO_COSMO == "metade":
        return max(1, mod_cosmo // 2)
    return max(1, mod_cosmo)


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
CHOQUE_MINIMO = 16     # o natural igual do choque: de 16 a 20 (com técnica toda rodada, 1 a 20 travava metade das lutas)
APARAR_USA_REACAO = True


def media_dado(lados: int) -> float:
    return (lados + 1) / 2


def ceil_div(a: int, b: int) -> int:
    return -(-a // b)


def arred_cima(x: float) -> int:
    return int(math.ceil(x))
