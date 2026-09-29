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

# O dano de cada ponto de técnica: o dado + o bônus do ponto, que é o nível − 1 (0.7.0;
# até a 0.6.0 era 1d8 por Grau). Cresce um pouco a cada nível em vez de saltar na
# fronteira do Grau. A técnica soma no máximo o último nível do Grau dela − 1: a que
# ficou para trás para de crescer até ser evoluída.


def bonus_do_ponto(nivel: int, grau_tecnica: int | None = None) -> int:
    g = grau(nivel) if grau_tecnica is None else grau_tecnica
    return min(nivel, 4 * g) - 1


def dano_do_ponto(nivel: int, grau_tecnica: int | None = None) -> tuple[int, int]:
    """(dados, bônus fixo) de um ponto de dano."""
    return 1, bonus_do_ponto(nivel, grau_tecnica)


# PV: uma base que sobe a cada nível, e a Constituição soma a cada nível. A base
# cresce mais rápido que o dano das técnicas: a luta é curta e decisiva no começo e
# longa e destrutiva no fim (0.6.0). Desde a 0.7.0 ela sobe nível a nível, sem o
# salto na fronteira do Grau.
PV_BASE = {1: 14, 2: 18, 3: 23, 4: 30, 5: 38, 6: 46, 7: 55, 8: 65, 9: 76, 10: 88,
           11: 101, 12: 115, 13: 130, 14: 146, 15: 163, 16: 181, 17: 200, 18: 220,
           19: 240, 20: 260}


def pv_da_vida(nivel: int) -> int:
    """Quanto cada escolha de Vida soma: metade do nível, arredondada para cima.
    É recalculada quando você sobe — as escolhas antigas crescem junto."""
    return -(-nivel // 2)


def pv_maximo(nivel: int, con: int, vigor: int = 0, extra_por_nivel: int = 0) -> int:
    return PV_BASE[nivel] + con * nivel + vigor * pv_da_vida(nivel) + extra_por_nivel * nivel


# ---------------------------------------------------------------------------
# Antes do Sexto Sentido: o status base (Capítulo Três)
# ---------------------------------------------------------------------------

# Todo mundo começa humano. Antes de despertar há os níveis humanos (0.9.1, pedido do
# usuário): o nível 1 é o humano comum, automático; do 2 em diante, o aprendiz. O 4 é
# o limite do corpo humano, e a prova pode acontecer a partir do 3. Quem desperta
# recomeça no nível 1 — de guerreiro. Sem Cosmo, sem técnica, sem armadura; diante de
# um guerreiro desperto, um humano é figurante (Capítulo Dez).
NIVEIS_HUMANOS = (1, 2, 3, 4)
NIVEL_APRENDIZ = 2
NIVEL_DA_PROVA = 3
HUMANO_DEF = 10                # + DES
HUMANO_DEFESA_PASSIVA = 10     # + atributo (+ proficiência nas treinadas, do nível 2)
DESPERTO_DEFESA_PASSIVA = 14   # o nível 1 de guerreiro (14 + atributo)


def pv_humano(nivel_humano: int, mod_con: int) -> int:
    """4, 6, 8 e 10, + CON."""
    return max(1, 2 + 2 * nivel_humano + mod_con)


def dado_golpe_humano(nivel_humano: int) -> int:
    """O soco de gente: 1d4; o aprendiz de nível 3 em diante, 1d6."""
    return 6 if nivel_humano >= 3 else 4


def conviccoes_humanas(nivel_humano: int) -> int:
    """Gente comum não levanta; o aprendiz tem uma: o motivo pelo qual treina."""
    return 1 if nivel_humano >= NIVEL_APRENDIZ else 0


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
# Os do humano, antes de despertar (0.9.3, sugestão do usuário). Ao despertar, cada valor
# sobe para o do guerreiro na mesma posição: 12→15, 11→14, 11→13, 10→12, 9→10, 8→8.
DISTRIBUICAO_HUMANA = (12, 11, 11, 10, 9, 8)
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


# O preço em vida de cada ponto que o Cosmo não paga (ou que você queima além do
# custo). "grau": 1d4 × o Grau da técnica (o do livro). "nivel": 1d4 + metade do seu
# nível — testado na 0.7.0 e descartado: sem o degrau do preço, o pico de um nível acima
# no nível 13 subia de 86% para 92%.
PRECO_POR_PONTO = "grau"


def preco_do_ponto(nivel: int, grau_tecnica: int) -> tuple[int, int, int]:
    """(dados, lados, bônus fixo) do preço de um ponto."""
    if PRECO_POR_PONTO == "nivel":
        return 1, 4, nivel // 2
    return grau_tecnica, 4, 0


def media_preco(nivel: int, grau_tecnica: int) -> float:
    dados, lados, fixo = preco_do_ponto(nivel, grau_tecnica)
    return dados * (lados + 1) / 2 + fixo


def resistencia_do_corpo(mod_con: int) -> int:
    """A Resistência que é sua, não da armadura: o modificador de CON, mínimo 0 (0.8.0;
    antes, +1 nos níveis 5, 7, 13 e 17). O corpo que aguenta a armadura."""
    return max(0, mod_con)


def resistencia_da_vida(escolhas_de_vida: int) -> int:
    """+1 de Resistência a cada duas escolhas de Vida, como o piso sobe a cada duas de
    Cosmo (0.8.0). Sem isso, quem escolhia só Vida ficava sem armadura nas lutas longas
    do nível 17 em diante e vencia 4% a 6% contra quem alterna."""
    return escolhas_de_vida // 2


# A DEF usa a DES ou o Atributo do Cosmo, o maior. Com a armadura no corpo, também a FOR
# ou a CON: a guarda — o golpe bate no braço cruzado ou no corpo e não entra (0.8.0). Sem
# isso, quem lutava pela FOR vencia 13% a 51% contra quem luta pela DES.
ATRIBUTOS_DA_GUARDA = ("for", "con")


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

# Sozinho contra muitos: um inimigo com Convicções que luta sozinho contra um grupo
# responde depois do turno de cada personagem, contra quem acabou de agir, com a técnica
# de dano mais barata dele, sem gastar Cosmo (0.8.0). Os PV não se multiplicam mais: com
# PV × 1¼ a 2¼ e golpes comuns a mais, o grupo contra a elite levava 13 a 18 rodadas, e o
# golpe comum, que não cresce com o nível, quase não pesava no nível 20.
def chefe_pv(oponentes: int) -> float:
    return 1.0


CHEFE_ACAO = "pequena"    # a resposta: "pequena" (a do livro), "golpe" ou "tecnica"


def chefe_acoes(oponentes: int) -> int:
    """Uma resposta por personagem, de 2 oponentes em diante."""
    return oponentes if oponentes >= 2 else 0


# O aliado de luta (Capítulo Onze): um inimigo da tabela rápida na metade do nível do
# grupo, com metade dos PV e sem Convicção. Não é personagem: não conta para Sozinho
# contra muitos. (0.7.0: dois níveis abaixo e com os PV inteiros, ele virava um segundo
# personagem nos níveis altos — 96% contra um rival que o grupo venceria na metade.)
ALIADO_PV = 0.5


def nivel_do_aliado(nivel_do_grupo: int) -> int:
    return -(-nivel_do_grupo // 2)

# ---------------------------------------------------------------------------
# Figurantes (Capítulo Dez)
# ---------------------------------------------------------------------------

# Quantos figurantes caem com um acerto: o golpe comum derruba dois; a técnica de
# alvo único, três; a técnica em área, os que pegar, até FIGURANTES_POR_AREA.
FIGURANTES_POR_GOLPE = 2
FIGURANTES_POR_TECNICA = 3
# A técnica em área derruba os que pegar, até seis (0.10.0). No playtest, uma área de
# tamanho 3 apagava bandos de doze de uma vez, turno após turno.
FIGURANTES_POR_AREA = 6


def figurante(nivel: int) -> tuple[int, int, int]:
    """(DEF, ataque do bando, dano por acerto) do bando no nível do grupo. O dano é
    fixo e acompanha a base de PV: um bando de seis custa de 16% a 30% dos PV de quem
    luta sozinho (medido em sim/mestre.py)."""
    return 11 + nivel // 3, prof(nivel) + 2, PV_BASE[nivel] // 5


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
# O primeiro Sétimo do Bronze e do Prata é um marco (0.10.0): antes deste nível ele
# não acontece, nem levantando. O simulador mede uma luta de cada vez, então do nível
# mínimo em diante trata o primeiro despertar como já acontecido.
NIVEL_SETIMO = 5
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
