"""As ferramentas do Mestre, medidas.

Os Capítulos Dez e Onze dão ao Mestre um jeito de montar quem está do outro lado
e quem luta ao lado. Este arquivo mede cada promessa desses dois capítulos: quanto
pesa cada inimigo, o que um bando de figurantes custa, quanto ajuda um aliado de
luta e o que as fichas prontas fazem contra o grupo.

    python sim/mestre.py            (alguns minutos; escreve sim/MESTRE.md)
    python sim/mestre.py --rapido   (menos lutas por célula)
"""

from __future__ import annotations

import pathlib
import random
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))

import regras as R  # noqa: E402
from luta import duelos, grupo_contra_um, montar, muitos_contra_muitos  # noqa: E402
from tecnica import Tecnica  # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

RAPIDO = "--rapido" in sys.argv
N = 300 if RAPIDO else 800
NG = 200 if RAPIDO else 400          # lutas de grupo são mais lentas


def pct(x: float) -> str:
    return f"{x:.0%}"


def faixa(valores) -> str:
    v = [round(100 * x) for x in valores]
    return f"{min(v)}% a {max(v)}%" if min(v) != max(v) else f"{v[0]}%"


# ---------------------------------------------------------------------------
# Quem é quem
# ---------------------------------------------------------------------------


def pc(n: int, posto: str = "bronze"):
    """O personagem: três Convicções, levanta no máximo uma vez por luta."""
    return lambda: montar("P", n, posto, conviccoes=3)


def inimigo(n: int, posto: str = "bronze", conviccoes: int = 0):
    """Um inimigo da tabela. Bronze e Prata sem Convicção não despertam o Sétimo."""
    pol = {"despertar": R.desperta_do_mestre(posto, conviccoes)}
    return lambda: montar("I", n, posto, conviccoes=conviccoes, politica=pol)


def aliado(n: int):
    """O aliado de luta: um inimigo da tabela rápida na metade do nível do grupo, com
    metade dos PV e sem Convicção."""
    a = montar("Aliado", R.nivel_do_aliado(n), conviccoes=0, politica={"despertar": False})
    a.pv_max = round(a.pv_max * R.ALIADO_PV)
    a.aliado = True                 # o chefe não responde ao turno dele
    a.reiniciar()
    return a


def grupo(n: int, k: int, com_aliado: bool = False):
    return lambda: ([montar(f"P{i}", n) for i in range(k)]
                    + ([aliado(n)] if com_aliado else []))


def contra_muitos(personagens: int) -> dict:
    """Sozinho contra muitos conta só os personagens: o aliado de luta fica de fora."""
    return {"pv_chefe": R.chefe_pv(personagens), "acoes_chefe": R.chefe_acoes(personagens)}


# ---------------------------------------------------------------------------
# Quanto pesa um inimigo (a tabela de dificuldade do Capítulo Dez)
# ---------------------------------------------------------------------------

IMPARES = (1, 3, 5, 7, 9, 11, 13, 15, 17)

DIFICULDADE = [
    ("Fácil", "Nomeado sem Convicção, do mesmo nível ou um acima",
     [(pc(n), inimigo(n + d)) for n in IMPARES for d in (0, 1)]),
    ("Justa", "Mesmo nível e mesmo Posto, com três Convicções, como o personagem",
     [(pc(n), inimigo(n, conviccoes=3)) for n in IMPARES + (19,)]),
    ("Difícil", "Rival um nível acima, com uma Convicção",
     [(pc(n), inimigo(n + 1, conviccoes=1)) for n in IMPARES]),
    ("Muito difícil", "Rival dois níveis acima, com uma Convicção",
     [(pc(n), inimigo(n + 2, conviccoes=1)) for n in IMPARES]),
    ("Muito difícil", "Um Prata do mesmo nível com uma Convicção, contra um Bronze",
     [(pc(n), inimigo(n, "prata", 1)) for n in (9, 11, 13, 15, 17, 19)]),
    ("Mortal", "Elite do mesmo nível, contra um Bronze ou um Prata",
     [(pc(n, p), inimigo(n, "ouro", 2)) for n in (15, 17, 20) for p in ("bronze", "prata")]),
    ("Mortal, mas possível", "Elite três níveis abaixo do personagem (a partir do nível 18)",
     [(pc(n, p), inimigo(n - 3, "ouro", 2)) for n in (18, 19, 20) for p in ("bronze", "prata")]),
]

# A fronteira que continua pesando é a do Posto (pedido do usuário, 0.7.0).
FRONTEIRAS = [
    ("Bronze de nível 8 contra Prata de nível 9, uma Convicção", pc(8), inimigo(9, "prata", 1)),
    ("Bronze de nível 9 contra Prata de nível 9, uma Convicção", pc(9), inimigo(9, "prata", 1)),
    ("Bronze de nível 14 contra elite de nível 15", pc(14), inimigo(15, "ouro", 2)),
    ("Prata de nível 14 contra elite de nível 15", pc(14, "prata"), inimigo(15, "ouro", 2)),
]


def medir_dificuldade(lutas: int = N) -> list[tuple[str, str, list[float]]]:
    saida = []
    for i, (nome, quem, pares) in enumerate(DIFICULDADE):
        v = [duelos(fa, fb, n=lutas, semente=100 * i + j)["a"] for j, (fa, fb) in enumerate(pares)]
        saida.append((nome, quem, v))
    return saida


def um_nivel_acima(lutas: int = N) -> list[float]:
    """Nomeado sem Convicção um nível acima do personagem, em todo nível."""
    return [duelos(pc(n - 1), inimigo(n), n=lutas, semente=500 + n)["a"] for n in range(2, 21)]


# ---------------------------------------------------------------------------
# Figurantes
# ---------------------------------------------------------------------------


def _d20(rng: random.Random, vantagem: bool) -> int:
    a = rng.randint(1, 20)
    return max(a, rng.randint(1, 20)) if vantagem else a


def bando(nivel: int, tamanho: int = 6, area: bool = False, lutas: int = 2000,
          semente: int = 1) -> dict:
    """Um personagem sozinho contra um bando da tabela de figurantes.

    Ele usa a técnica quando ela derruba mais que os golpes do turno (a de área
    derruba até seis; a de alvo único, três) e o golpe comum no resto. O bando ataca
    uma vez por rodada, com Vantagem enquanto houver mais de três de pé. O dano dele
    não se apara e o ataque não tem crítico (0.10.0): o bando só custa PV.
    Devolve as rodadas, a fração dos PV que ele perdeu e quantas vezes caiu."""
    rng = random.Random(semente)
    de, atk, dano = R.figurante(nivel)
    g = R.grau(nivel)
    if area:
        tec = Tecnica("área", "golpe", {"dano": 1, "area": 1}, grau=g)
        derruba_tec = min(tamanho, R.FIGURANTES_POR_AREA)
    else:
        tec = Tecnica("alvo único", "golpe", {"dano": 2}, grau=g)
        derruba_tec = R.FIGURANTES_POR_TECNICA
    rodadas = perda = caiu = 0
    for _ in range(lutas):
        x = montar("P", nivel)
        x.reiniciar()
        acerta = min(0.95, max(0.05, (21 - de + x.bonus_ataque("golpe")) / 20))
        golpes = R.ataques_por_golpe(nivel)
        vivos, r = tamanho, 0
        while vivos > 0 and r < 20:
            r += 1
            if r > 1:
                x.subir_cosmo(R.COSMO_RELOGIO)
            for vez in ((0, 1) if rng.random() < 0.5 else (1, 0)):
                if vivos <= 0:
                    break
                if vez == 0:
                    custo = tec.custo()
                    pode = x.cosmo >= custo or x.piso >= custo
                    if pode and derruba_tec > R.FIGURANTES_POR_GOLPE * golpes:
                        if x.piso < custo:
                            x.cosmo -= custo
                        if rng.random() < acerta:
                            vivos -= derruba_tec
                    else:
                        acertou = False
                        for _g in range(golpes):
                            if vivos > 0 and rng.random() < acerta:
                                vivos -= R.FIGURANTES_POR_GOLPE
                                acertou = True
                        if acertou:
                            x.subir_cosmo(R.COSMO_ACERTO)
                elif _d20(rng, vivos > 3) + atk >= x.defesa:
                    x.pv -= dano
        rodadas += r
        perda += min(1.0, (x.pv_max - x.pv) / x.pv_max)
        caiu += x.pv <= 0
    return {"rodadas": rodadas / lutas, "perda": perda / lutas, "caiu": caiu / lutas}


# ---------------------------------------------------------------------------
# Antes do Sexto Sentido: a prova da armadura
# ---------------------------------------------------------------------------


def prova(nivel_humano: int = R.NIVEL_DA_PROVA, lutas: int = 4000, semente: int = 1,
          despertar: bool = True) -> dict:
    """Dois aprendizes do mesmo nível humano na prova da armadura: FOR ou DES 12, CON 11,
    que viram 15 e 14 quando ele desperta.

    Cada um ataca uma vez por turno com o golpe de gente do nível dele. Quem cai a 0 PV
    gasta a Convicção e levanta com um quarto dos PV; com `despertar`, levanta desperto:
    os atributos de guerreiro, um quarto dos PV do nível 1 de guerreiro, o Cosmo no Teto e
    a técnica assinatura (a grande do Grau 1). Devolve as rodadas, quantas provas tiveram
    alguém despertando e em quantas os dois despertaram."""
    rng = random.Random(semente)
    golpe_h, con_h = (R.mod(v) for v in R.DISTRIBUICAO_HUMANA[:2])
    golpe_d, con_d = (R.mod(v) for v in R.DISTRIBUICAO[:2])
    pv_max = R.pv_humano(nivel_humano, con_h)
    dado = R.dado_golpe_humano(nivel_humano)
    rodadas = despertou = vence_desperto = 0
    for _ in range(lutas):
        pv = [pv_max, pv_max]
        acordado = [False, False]
        levantou = [False, False]
        r = 0
        vez = rng.randint(0, 1)
        while min(pv) > 0 and r < 30:
            r += 1
            for _t in range(2):
                a, b = vez, 1 - vez
                vez = b
                mod = golpe_d if acordado[a] else golpe_h
                de = R.HUMANO_DEF + (golpe_d if acordado[b] else golpe_h)
                if rng.randint(1, 20) + mod + R.prof(1) >= de:
                    if acordado[a]:
                        # desperto: o Cosmo no Teto e a técnica assinatura, a grande
                        pontos = R.TAMANHO_MAXIMO[1]
                        pv[b] -= sum(rng.randint(1, 8) for _p in range(pontos)) + mod
                    else:
                        pv[b] -= rng.randint(1, dado) + mod
                if pv[b] <= 0 and not levantou[b]:
                    levantou[b] = True
                    if despertar:
                        acordado[b] = True
                        pv[b] = max(1, (R.PV_BASE[1] + con_d) // 4)
                    else:
                        pv[b] = max(1, pv_max // 4)
                if pv[b] <= 0:
                    break
        rodadas += r
        despertou += any(acordado)
        vence_desperto += all(acordado)
    return {"rodadas": rodadas / lutas, "despertou": despertou / lutas,
            "os_dois_despertam": vence_desperto / lutas}


# ---------------------------------------------------------------------------
# A surpresa (0.10.0)
# ---------------------------------------------------------------------------

NIVEIS_SURPRESA = (1, 3, 5, 9, 13, 17, 20)


def surpresa(n: int, lutas: int = N) -> float:
    """Espelho de Bronzes em que o primeiro dá o golpe de abertura."""
    return duelos(lambda: montar("A", n, conviccoes=3), lambda: montar("B", n, conviccoes=3),
                  n=lutas, semente=650 + n, surpresa_a=True)["a"]


# ---------------------------------------------------------------------------
# O grupo contra um nomeado acima do nível dele (0.11.0)
# ---------------------------------------------------------------------------

NIVEIS_ACIMA = (1, 3, 5, 9, 13)


def grupo_contra_nomeado(n: int, k: int, acima: int, lutas: int = NG) -> dict:
    """k personagens do nível n contra um nomeado sem Convicção `acima` níveis acima.
    Sem Convicção, ele não usa Sozinho contra muitos."""
    return grupo_contra_um(grupo(n, k), inimigo(n + acima), n=lutas,
                           semente=1100 + 10 * n + acima + k, sozinho_contra_muitos=False)


# ---------------------------------------------------------------------------
# A armadura de Ouro emprestada (0.11.0)
# ---------------------------------------------------------------------------

NIVEIS_EMPRESTADA = (5, 9, 13, 17)


def emprestada(n: int, posto: str = "bronze", lutas: int = N) -> tuple[float, float]:
    """Um Bronze contra alguém do mesmo nível: com a armadura dele e com uma de Ouro
    emprestada (a linha do Ouro, três características, sem as formas da dele)."""
    conv = {"bronze": 3, "prata": 1, "ouro": 2}[posto]

    def com():
        return montar("P", n, conviccoes=3, armadura_posto="ouro")
    sem_ = duelos(pc(n), inimigo(n, posto, conv), n=lutas, semente=1200 + n)["a"]
    com_ = duelos(com, inimigo(n, posto, conv), n=lutas, semente=1200 + n)["a"]
    return sem_, com_


def emprestada_no_grupo(n: int, lutas: int = NG) -> tuple[float, float]:
    """Quatro Bronzes contra um Ouro do mesmo nível, e um deles de armadura emprestada."""
    def quatro():
        return [montar(f"P{i}", n, armadura_posto="ouro" if i == 0 else "") for i in range(4)]
    sem_ = grupo_contra_um(grupo(n, 4), inimigo(n, "ouro", 2), n=lutas, semente=1210 + n)["grupo"]
    com_ = grupo_contra_um(quatro, inimigo(n, "ouro", 2), n=lutas, semente=1210 + n)["grupo"]
    return sem_, com_


def emprestada_prata(n: int, lutas: int = N) -> tuple[float, float]:
    """Um Bronze contra um Bronze do mesmo nível, com uma armadura de Prata emprestada."""
    def com():
        return montar("P", n, conviccoes=3, armadura_posto="prata")
    sem_ = duelos(pc(n), inimigo(n, "bronze", 3), n=lutas, semente=1220 + n)["a"]
    com_ = duelos(com, inimigo(n, "bronze", 3), n=lutas, semente=1220 + n)["a"]
    return sem_, com_


# ---------------------------------------------------------------------------
# Os deuses (0.11.0)
# ---------------------------------------------------------------------------

SANGUE_DE_DEUS = {"bronze": ("guerreiro",) * 3 + ("elite", "deus"),
                  "ouro": ("guerreiro",) * 6 + ("deus",)}


def no_nono(posto: str = "bronze", nome: str = "H"):
    """Um personagem de nível 20 no Nono, com a armadura na forma Divina (a escada do sangue
    inteira, até o de deus)."""
    def f():
        x = montar(nome, 20, posto, conviccoes=3, formas=SANGUE_DE_DEUS[posto],
                   armadura_posto="divina")
        x.sentido_inicial = "nono"
        x.reiniciar()
        return x
    return f


def deus(tipo: str):
    """O deus do Capítulo Dez: a elite de nível 20, no Nono, com os PV e a defesa da
    tabela. Apara pelo tamanho do golpe, não pela fração dos PV dele."""
    t = R.DEUSES[tipo]

    def f():
        x = montar("Deus", 20, "ouro", conviccoes=0,
                   politica={"aparar_limiar": 0.20 / t["pv"]})
        x.pv_max = int(x.pv_max * t["pv"])
        x.defesa_extra = t["def"]
        x.sentido_inicial = "nono"
        x.deus = tipo
        x.reiniciar()
        return x
    return f


def no_setimo(oitavo: bool, nome: str):
    """Um Ouro de nível 20 no Sétimo, revivido seis vezes, com ou sem o Oitavo."""
    def f():
        x = montar(nome, 20, "ouro", conviccoes=3, formas=("guerreiro",) * 6)
        x.sentido_inicial = "setimo"
        x.oitavo = oitavo
        x.reiniciar()
        return x
    return f


def ouros_contra_deus(k: int, oitavo: bool, tipo: str = "menor", lutas: int = NG,
                      ao_lado: bool = False) -> dict:
    """k Ouros no Sétimo (com ou sem o Oitavo) contra um deus: fora do Nono, só uma fração
    do dano entra (R.DANO_CONTRA_DEUS) — a não ser que lutem ao lado do próprio deus."""
    def grupo_():
        g = [no_setimo(oitavo, f"O{i}")() for i in range(k)]
        for x in g:
            x.ao_lado_do_deus = ao_lado
        return g
    return grupo_contra_um(grupo_, deus(tipo),
                           n=lutas, semente=1600 + k + (50 if oitavo else 0),
                           sozinho_contra_muitos=False, pv_chefe=1.0, acoes_chefe=R.chefe_acoes(k))


def contra_deus(tipo: str, posto: str = "bronze", k: int = 1, lutas: int = NG) -> dict:
    """k personagens no Nono contra um deus, que responde a cada um como um chefe (Sozinho
    contra muitos). Sem a Guerra dos Mil Dias: um deus não morre junto."""
    return grupo_contra_um(lambda: [no_nono(posto, f"H{i}")() for i in range(k)], deus(tipo),
                           n=lutas, semente=1500 + k + (10 if posto == "ouro" else 0),
                           sozinho_contra_muitos=False, pv_chefe=1.0, acoes_chefe=R.chefe_acoes(k))


# ---------------------------------------------------------------------------
# O sangue doado (0.11.0)
# ---------------------------------------------------------------------------

NIVEIS_SANGUE = (1, 5, 9, 13, 17, 20)


def debilitado(n: int, tercos: int, lutas: int = N) -> float:
    """Um Bronze que doou `tercos` terços do sangue contra um Bronze inteiro do mesmo
    nível: os PV máximos caem um terço por terço doado, arredondado para cima."""
    def doador():
        x = montar("P", n, conviccoes=3)
        x.pv_max -= R.ceil_div(x.pv_max * tercos, 3)
        x.reiniciar()
        return x
    return duelos(doador, inimigo(n, conviccoes=3), n=lutas, semente=1300 + n)["a"]


# ---------------------------------------------------------------------------
# A armadura que se sacrifica (regra opcional, 0.11.0)
# ---------------------------------------------------------------------------


def sacrificio(n: int, resistencia: int | None = None, lutas: int = N) -> tuple[float, float]:
    """Sem e com a regra, contra um Bronze inteiro do mesmo nível. Com `resistencia`, o
    personagem começa a luta com a armadura gasta: lutas em sequência, sem descanso."""
    def quem(pol):
        def f():
            x = montar("P", n, conviccoes=3, politica=pol)
            x.resistencia_inicial = resistencia
            x.reiniciar()
            return x
        return f
    sem_ = duelos(quem({}), inimigo(n, conviccoes=3), n=lutas, semente=1400 + n)["a"]
    com_ = duelos(quem({"sacrificar": "cair"}), inimigo(n, conviccoes=3), n=lutas,
                  semente=1400 + n)["a"]
    return sem_, com_


# ---------------------------------------------------------------------------
# Os que Hades traz de volta (0.15.0)
# ---------------------------------------------------------------------------


def corrompido(n: int = 4, k: int = 3, convicoes: int = 0, lutas: int = NG) -> dict:
    """k personagens (ou companheiros) do nível n contra um Prata de nível 9. Sem Convicção
    ele é um corrompido: não levanta, não responde e não desperta."""
    return grupo_contra_um(grupo(n, k), inimigo(9, "prata", convicoes), n=lutas,
                           semente=1700 + 10 * n + k + convicoes)


# ---------------------------------------------------------------------------
# Os golpes famosos, montados com as peças novas do motor (0.18.0)
# ---------------------------------------------------------------------------


def golpes_famosos(grau: int = 4) -> dict:
    """Os exemplos do Capítulo Seis, como Golpe do Assento no Grau 4 (tamanho máximo 7)."""
    return {
        "Agulha Escarlate": Tecnica("Agulha Escarlate", "golpe", {"dano": 3}, alcance="curto",
                                    mais=("marca", "desfecho"), grau=grau, assento=True),
        "Caixão de Gelo": Tecnica("Caixão de Gelo", "cosmo", {"cond_forte": 1, "dano": 1},
                                  alcance="medio", limitacoes=1, grau=grau, assento=True,
                                  condicao="banido"),
        "Ondas do Inferno": Tecnica("Ondas do Inferno", "cosmo", {"cond_forte": 1},
                                    alcance="vista", limitacoes=1, grau=grau, assento=True,
                                    condicao="banido", limites=("puxa",)),
        "Muralha de Cristal": Tecnica("Muralha de Cristal", "cosmo", {"refletir": 1},
                                      ativacao="reacao", limitacoes=1, grau=grau, assento=True,
                                      limites=("uma_vez",)),
    }


def ouro_com(nome: str, golpe: str | None, n: int = 16, conviccoes: int = 3):
    """Um Ouro do nível n com um dos golpes famosos no lugar do Golpe do Assento comum."""
    def f():
        x = montar(nome, n, "ouro", conviccoes=conviccoes)
        if golpe:
            x.tecnicas = [t for t in x.tecnicas if t.nome != "assento"] + [golpes_famosos()[golpe]]
        x.reiniciar()
        return x
    return f


def golpe_famoso(golpe: str | None, lutas: int = N) -> tuple[float, float]:
    """Num duelo contra um Ouro de nível 16 com o Assento comum, e como chefe de nível 15
    contra quatro Bronzes do nível dele: quanto o dono do golpe vence, e quanto o grupo."""
    d = duelos(ouro_com("A", golpe), ouro_com("B", None), n=lutas, semente=1800)["a"]
    g = grupo_contra_um(grupo(15, 4), ouro_com("C", golpe, n=15, conviccoes=2), n=NG,
                        semente=1810)["grupo"]
    return d, g


# ---------------------------------------------------------------------------
# Vários contra vários (0.19.0)
# ---------------------------------------------------------------------------

# (nome, quantos inimigos a mais que personagens, Convicções de cada um, níveis acima)
MUITOS = [
    ("Nomeados, tantos quanto os personagens, do mesmo nível", 0, 0, 0),
    ("Nomeados, um a mais que os personagens, do mesmo nível", 1, 0, 0),
    ("Nomeados, tantos quanto, dois níveis acima", 0, 0, 2),
    ("Nomeados, tantos quanto, três níveis acima", 0, 0, 3),
    ("Rivais (uma Convicção), um a menos que os personagens", -1, 1, 0),
    ("Rivais, tantos quanto os personagens", 0, 1, 0),
    ("Rivais, tantos quanto, um nível acima", 0, 1, 1),
    ("Rivais, um a mais que os personagens", 1, 1, 0),
]


def muitos(n: int, k: int, a_mais: int, conviccoes: int, acima: int, lutas: int = 150) -> dict:
    """k personagens do nível n contra k + a_mais inimigos do nível n + acima."""
    pol = {"despertar": R.desperta_do_mestre("bronze", conviccoes)}

    def inimigos():
        return [montar(f"I{i}", n + acima, conviccoes=conviccoes, politica=pol)
                for i in range(k + a_mais)]
    return muitos_contra_muitos(grupo(n, k), inimigos, n=lutas,
                                semente=1900 + 11 * n + 3 * k + a_mais + acima)


def milagre(n: int, lutas: int = N) -> tuple[float, float]:
    """Um Bronze sozinho contra um Ouro do mesmo nível: sem e com a Centelha do deus na
    pior hora (o milagre)."""
    def bronze(m):
        def f():
            x = montar("P", n, conviccoes=3)
            x.centelha_do_deus = m
            x.reiniciar()
            return x
        return f
    sem = duelos(bronze(False), inimigo(n, "ouro", 3), n=lutas, semente=2000 + n)["a"]
    com = duelos(bronze(True), inimigo(n, "ouro", 3), n=lutas, semente=2000 + n)["a"]
    return sem, com


# ---------------------------------------------------------------------------
# O aliado de luta
# ---------------------------------------------------------------------------


def aliado_no_duelo(n: int, lutas: int = NG) -> tuple[float, float]:
    """Contra um rival do mesmo nível com uma Convicção: sozinho, e com o aliado."""
    so = duelos(pc(n), inimigo(n, conviccoes=1), n=N, semente=700 + n)["a"]
    com = grupo_contra_um(grupo(n, 1, True), inimigo(n, conviccoes=1), n=lutas,
                          semente=710 + n, pv_chefe=1.0, acoes_chefe=0)["grupo"]
    return so, com


def aliado_no_grupo(n: int, k: int, lutas: int = NG) -> tuple[float, float]:
    """k Bronzes contra um Ouro do mesmo nível: sem e com um aliado de luta."""
    sem = grupo_contra_um(grupo(n, k), inimigo(n, "ouro", 2), n=lutas, semente=720 + n + k)["grupo"]
    com = grupo_contra_um(grupo(n, k, True), inimigo(n, "ouro", 2), n=lutas,
                          semente=730 + n + k, **contra_muitos(k))["grupo"]
    return sem, com


# ---------------------------------------------------------------------------
# As fichas prontas contra o grupo
# ---------------------------------------------------------------------------

# (ficha, quem enfrenta, nível do personagem, quantos personagens)
FICHAS = [
    ("cavaleiro-negro", "Um Bronze de nível 1", 1, 1),
    ("espectro-novato", "Um Bronze de nível 1", 1, 1),
    ("espectro-novato", "Um Bronze de nível 2", 2, 1),
    ("espectro-novato", "Dois Bronzes de nível 1", 1, 2),
    ("espectro-novato", "Três Bronzes de nível 1", 1, 3),
    ("espectro-terrestre", "Um Bronze de nível 3", 3, 1),
    ("espectro-terrestre", "Um Bronze de nível 4", 4, 1),
    ("cavaleiro-de-prata", "Um Bronze de nível 8", 8, 1),
    ("cavaleiro-de-prata", "Um Bronze de nível 9", 9, 1),
    ("cavaleiro-de-prata", "Um Bronze de nível 13", 13, 1),
    ("cavaleiro-de-prata", "Dois Bronzes de nível 9", 9, 2),
    ("cavaleiro-de-prata", "Três Bronzes de nível 9", 9, 3),
    ("estrela-celeste", "Um Bronze de nível 11", 11, 1),
    ("estrela-celeste", "Um Bronze de nível 13", 13, 1),
    ("estrela-celeste", "Dois Bronzes de nível 11", 11, 2),
    ("estrela-celeste", "Três Bronzes de nível 9", 9, 3),
    ("estrela-celeste", "Três Bronzes de nível 11", 11, 3),
    ("comandante-de-hades", "Um Bronze de nível 5", 5, 1),
    ("comandante-de-hades", "Um Bronze de nível 9", 9, 1),
    ("comandante-de-hades", "Três Bronzes de nível 5", 5, 3),
    ("satelite-de-artemis", "Um Bronze de nível 6", 6, 1),
    ("satelite-de-artemis", "Dois Bronzes de nível 5", 5, 2),
    ("palasita", "Um Bronze de nível 7", 7, 1),
    ("palasita", "Um Bronze de nível 6", 6, 1),
    ("marciano", "Um Bronze de nível 10", 10, 1),
    ("marciano", "Três Bronzes de nível 9", 9, 3),
    ("cavaleiro-da-coroa", "Um Bronze de nível 13", 13, 1),
    ("cavaleiro-da-coroa", "Três Bronzes de nível 12", 12, 3),
    ("anjo-caido", "Um Bronze de nível 14", 14, 1),
    ("anjo-caido", "Três Bronzes de nível 13", 13, 3),
    ("cavaleiro-fantasma", "Um Bronze de nível 16", 16, 1),
    ("cavaleiro-fantasma", "Três Bronzes de nível 15", 15, 3),
    ("tita", "Quatro Bronzes de nível 17", 17, 4),
    ("tita", "Cinco Bronzes de nível 17", 17, 5),
    ("guerreiro-deus", "Quatro Bronzes de nível 12", 12, 4),
    ("guerreiro-deus", "Quatro Bronzes de nível 15", 15, 4),
    ("general-marina", "Quatro Bronzes de nível 15", 15, 4),
    ("cavaleiro-de-ouro", "Um Bronze de nível 16", 16, 1),
    ("cavaleiro-de-ouro", "Quatro Bronzes de nível 15", 15, 4),
    ("cavaleiro-de-ouro", "Cinco Bronzes de nível 15", 15, 5),
    ("juiz-do-inferno", "Quatro Bronzes de nível 17", 17, 4),
    ("juiz-do-inferno", "Quatro Bronzes de nível 18", 18, 4),
]


def varios_contra_um(chave: str, quantos: int, n: int, lutas: int = NG, semente: int = 1) -> float:
    """Quantos da ficha pronta juntos contra um Bronze do nível n: quanto o Bronze vence.
    Nomeados sem Convicção não usam Sozinho contra muitos, e o Bronze também não."""
    from inimigos import lutador
    r = grupo_contra_um(lambda: [lutador(chave) for _ in range(quantos)], pc(n), n=lutas,
                        semente=semente, sozinho_contra_muitos=False)
    return 1 - r["grupo"] - r["empate"]


def contra_ficha(chave: str, n: int, k: int, lutas: int = NG, semente: int = 1) -> dict:
    """Quanto k Bronzes do nível n vencem a ficha pronta, e quantos caem."""
    from inimigos import lutador
    if k == 1:
        r = duelos(pc(n), lambda: lutador(chave), n=lutas, semente=semente)
        return {"vence": r["a"], "caem": None}
    r = grupo_contra_um(grupo(n, k), lambda: lutador(chave), n=lutas, semente=semente)
    return {"vence": r["grupo"], "caem": r["caidos_media"]}


# ---------------------------------------------------------------------------
# O relatório
# ---------------------------------------------------------------------------


def main() -> None:
    linhas = ["# As ferramentas do Mestre, medidas", "",
              f"Gerado por `python sim/mestre.py`. {N} duelos por célula ({NG} nas lutas de "
              "grupo, 2000 nos bandos), sementes fixas. O personagem tem três Convicções e "
              "levanta no máximo uma vez por luta.", ""]

    print("dificuldade...")
    linhas += ["## Quanto pesa um inimigo", "",
               "| Dificuldade | Inimigo | O personagem vence |", "|---|---|---:|"]
    for nome, quem, v in medir_dificuldade():
        linhas.append(f"| {nome} | {quem} | {faixa(v)} |")
    um = um_nivel_acima()
    linhas += ["", "| Nomeado sem Convicção um nível acima do personagem | "
               + " | ".join(str(n) for n in range(2, 21)) + " |",
               "|---|" + "---:|" * 19,
               "| O inimigo vence | " + " | ".join(pct(1 - x) for x in um) + " |", ""]
    linhas += ["| A fronteira do Posto | O personagem vence |", "|---|---:|"]
    for i, (nome, fa, fb) in enumerate(FRONTEIRAS):
        linhas.append(f"| {nome} | {pct(duelos(fa, fb, n=N, semente=600 + i)['a'])} |")

    print("figurantes...")
    linhas += ["", "## Figurantes", "",
               "Um personagem sozinho contra um bando da tabela. O golpe comum que acerta "
               f"derruba {R.FIGURANTES_POR_GOLPE}; a técnica de alvo único, "
               f"{R.FIGURANTES_POR_TECNICA}; a de área, os que pegar, até "
               f"{R.FIGURANTES_POR_AREA}. O dano do bando não se apara e o ataque dele não "
               "tem crítico.", "",
               "| Nível | DEF · ataque · dano | Seis, sem área | Seis, com área | Dez, sem área "
               "| Doze, com área |",
               "|---:|---|---|---|---|---|"]
    for n in range(1, 21):
        de, atk, dano = R.figurante(n)
        cel = []
        for tam, area in ((6, False), (6, True), (10, False), (12, True)):
            b = bando(n, tam, area, semente=n)
            c = f"{b['rodadas']:.1f} rodadas, {pct(b['perda'])} dos PV"
            if b["caiu"] >= 0.005:
                c += f", cai {pct(b['caiu'])}"
            cel.append(c)
        linhas.append(f"| {n} | {de} · +{atk} · {dano} | " + " | ".join(cel) + " |")

    print("surpresa...")
    linhas += ["", "## A surpresa", "",
               "Dois Bronzes do mesmo nível; o primeiro pegou o outro sem ser percebido e dá o "
               "golpe de abertura: um golpe comum antes da Iniciativa, com Vantagem, e o outro "
               "sem reação até o primeiro turno dele.", "",
               "| Nível | " + " | ".join(str(n) for n in NIVEIS_SURPRESA) + " |",
               "|---|" + "---:|" * len(NIVEIS_SURPRESA),
               "| Quem surpreende vence | "
               + " | ".join(pct(surpresa(n)) for n in NIVEIS_SURPRESA) + " |"]

    print("grupo contra nomeado acima...")
    linhas += ["", "## O grupo contra um nomeado acima do nível dele", "",
               "Personagens do mesmo nível contra um nomeado sem Convicção alguns níveis "
               "acima. Sem Convicção, ele não usa Sozinho contra muitos. Cada célula: quanto "
               "o grupo vence / quantos personagens caem, em média.", "",
               "| Nível do grupo | 2 contra +2 | 2 contra +3 | 2 contra +4 | 3 contra +2 "
               "| 3 contra +3 | 3 contra +4 |", "|---:|---|---|---|---|---|---|"]
    for n in NIVEIS_ACIMA:
        cel = []
        for k in (2, 3):
            for acima in (2, 3, 4):
                r = grupo_contra_nomeado(n, k, acima)
                cel.append(f"{pct(r['grupo'])} / {r['caidos_media']:.1f}")
        linhas.append(f"| {n} | " + " | ".join(cel) + " |")

    print("armadura emprestada...")
    linhas += ["", "## A armadura de Ouro emprestada", "",
               "Um Bronze de armadura de Ouro emprestada: a linha do Ouro na tabela de Posto, "
               "três características, a Resistência da CON e da Vida, e nada das formas da "
               "armadura dele. A Hierarquia e o Sétimo continuam os do Bronze.", "",
               "| Nível | Contra um Bronze (3 Convicções) | Contra um Prata (1) | "
               "Contra um Ouro (2) |", "|---:|---|---|---|"]
    for n in NIVEIS_EMPRESTADA:
        cel = []
        for posto in ("bronze", "prata", "ouro"):
            if R.posto_existe(posto, n):
                sem_, com_ = emprestada(n, posto)
                cel.append(f"{pct(sem_)} → {pct(com_)}")
            else:
                cel.append("—")
        linhas.append(f"| {n} | " + " | ".join(cel) + " |")
    linhas += ["", "| Quatro Bronzes contra um Ouro do mesmo nível | Sem | Um de armadura "
               "emprestada |", "|---|---:|---:|"]
    for n in (15, 20):
        sem_, com_ = emprestada_no_grupo(n)
        linhas.append(f"| Nível {n} | {pct(sem_)} | {pct(com_)} |")

    linhas += ["", "| Armadura de Prata emprestada, contra um Bronze do mesmo nível | Sem | Com |",
               "|---|---:|---:|"]
    for n in NIVEIS_EMPRESTADA:
        sem_, com_ = emprestada_prata(n)
        linhas.append(f"| Nível {n} | {pct(sem_)} | {pct(com_)} |")

    print("deuses...")
    linhas += ["", "## Os deuses", "",
               "Personagens de nível 20 no Nono, com a armadura na forma Divina, contra um deus: "
               "a elite de nível 20 no Nono, com os PV multiplicados e a DEF somada "
               f"(menor: × {R.DEUSES['menor']['pv']:g} e +{R.DEUSES['menor']['def']}; maior: "
               f"× {R.DEUSES['maior']['pv']:g} e +{R.DEUSES['maior']['def']}). Só o combate: os "
               "efeitos de destino ficam de fora. Cada célula: quanto vencem / rodadas / quantos "
               "caem.", "",
               "| Contra | Um Bronze | Um Ouro | Dois Bronzes | Três Bronzes |",
               "|---|---|---|---|---|"]
    for tipo in ("menor", "maior"):
        cel = []
        for posto, k in (("bronze", 1), ("ouro", 1), ("bronze", 2), ("bronze", 3)):
            r = contra_deus(tipo, posto, k)
            cel.append(f"{pct(r['grupo'])} / {r['rodadas_media']:.0f} / {r['caidos_media']:.1f}")
        linhas.append(f"| Deus {tipo} | " + " | ".join(cel) + " |")
    menor = R.DANO_CONTRA_DEUS["menor"]
    linhas += ["", "Fora do Nono, só uma fração do dano entra na divindade menor "
               f"({menor['setimo']:.0%} no Sétimo, {menor['oitavo']:.0%} com o Oitavo); no deus "
               "maior, nada. Ouros de nível 20 no Sétimo, revividos seis vezes:", "",
               "| Contra a divindade menor | Um | Três | Cinco |", "|---|---|---|---|"]
    for oit in (False, True):
        cel = []
        for k in (1, 3, 5):
            r = ouros_contra_deus(k, oit)
            cel.append(f"{pct(r['grupo'])} / {r['caidos_media']:.1f} caem")
        linhas.append(f"| {'Com o Oitavo' if oit else 'Só o Sétimo'} | " + " | ".join(cel) + " |")
    linhas += ["", "Ao lado do próprio deus, quem está no Sétimo fere um deus normalmente. Ouros de "
               "nível 20 no Sétimo, ferindo por inteiro:", "",
               "| Ao lado do próprio deus | Um | Três | Cinco |", "|---|---|---|---|"]
    for tipo in ("menor", "maior"):
        cel = []
        for k in (1, 3, 5):
            r = ouros_contra_deus(k, False, tipo, ao_lado=True)
            cel.append(f"{pct(r['grupo'])} / {r['caidos_media']:.1f} caem")
        linhas.append(f"| Contra o deus {tipo} | " + " | ".join(cel) + " |")

    print("sangue...")
    linhas += ["", "## O sangue doado", "",
               "Um Bronze que doou sangue contra um Bronze inteiro do mesmo nível, os dois com "
               "três Convicções. Cada terço doado tira um terço dos PV máximos.", "",
               "| Terços doados | " + " | ".join(str(n) for n in NIVEIS_SANGUE) + " |",
               "|---|" + "---:|" * len(NIVEIS_SANGUE)]
    for tercos in (0, 1, 2):
        linhas.append(f"| {tercos} | " + " | ".join(pct(debilitado(n, tercos))
                                                   for n in NIVEIS_SANGUE) + " |")

    print("sacrifício...")
    linhas += ["", "## A armadura que se sacrifica (regra opcional)", "",
               "No último ponto de Resistência, quando a metade do dano ainda derrubaria, a "
               "armadura segura o golpe inteiro e morre. Sem e com a regra, contra um Bronze "
               "inteiro do mesmo nível.", "",
               "| Começa a luta com | " + " | ".join(str(n) for n in NIVEIS_SANGUE) + " |",
               "|---|" + "---:|" * len(NIVEIS_SANGUE)]
    for res in (None, 2, 1):
        nome = "a Resistência cheia" if res is None else f"Resistência {res}"
        cel = []
        for n in NIVEIS_SANGUE:
            sem_, com_ = sacrificio(n, res)
            cel.append(f"{pct(sem_)} → {pct(com_)}")
        linhas.append(f"| {nome} | " + " | ".join(cel) + " |")

    print("corrompidos...")
    linhas += ["", "## Os que Hades traz de volta", "",
               "Três Bronzes (personagens ou companheiros) contra um Prata de nível 9: vivo, com "
               "uma Convicção, e corrompido, sem nenhuma. Cada célula: quanto vencem / quantos "
               "caem.", "",
               "| Nível dos três | Contra o Prata vivo | Contra o corrompido |", "|---:|---|---|"]
    for n in (4, 5, 7, 9):
        cel = []
        for c in (1, 0):
            r = corrompido(n, 3, c)
            cel.append(f"{pct(r['grupo'])} / {r['caidos_media']:.1f}")
        linhas.append(f"| {n} | " + " | ".join(cel) + " |")

    print("golpes famosos...")
    linhas += ["", "## Os golpes famosos", "",
               "Montados com as peças novas do motor como Golpe do Assento, no lugar do comum. "
               "Duelo: um Ouro de nível 16 com o golpe contra outro com o Assento comum. Chefe: "
               "quanto quatro Bronzes de nível 15 vencem o Ouro com o golpe.", "",
               "| Golpe | Tamanho · custo | Duelo | Quatro Bronzes vencem |", "|---|---|---:|---:|"]
    for nome in [None] + list(golpes_famosos()):
        d, g = golpe_famoso(nome)
        t = golpes_famosos().get(nome)
        tc = f"{t.tamanho()} · {t.custo()}" if t else "7 · 7"
        linhas.append(f"| {nome or 'Golpe do Assento comum'} | {tc} | {pct(d)} | {pct(g)} |")

    print("vários contra vários...")
    linhas += ["", "## Vários contra vários", "",
               "O grupo concentra os golpes no inimigo mais ferido; cada inimigo bate no "
               "personagem mais ferido. Sem a resposta de Sozinho contra muitos. Cada célula: "
               "quanto o grupo vence, para 2, 3 e 4 personagens.", "",
               "| Inimigos | Nível 3 | Nível 9 | Nível 15 |", "|---|---|---|---|"]
    for nome, a_mais, conv, acima in MUITOS:
        cel = []
        for n in (3, 9, 15):
            v = []
            for k in (2, 3, 4):
                if k + a_mais < 1 or n + acima > 20:
                    continue
                v.append(pct(muitos(n, k, a_mais, conv, acima)["grupo"]))
            cel.append(" · ".join(v))
        linhas.append(f"| {nome} | " + " | ".join(cel) + " |")

    print("milagre...")
    linhas += ["", "## O milagre", "",
               "Um Bronze sozinho contra um Ouro do mesmo nível, os dois com três Convicções: "
               "sem e com a Centelha do deus quando ele levanta.", "",
               "| Nível | Sem | Com o milagre |", "|---:|---:|---:|"]
    for n in (15, 17, 20):
        sem_, com_ = milagre(n)
        linhas.append(f"| {n} | {pct(sem_)} | {pct(com_)} |")

    print("aliado...")
    linhas += ["", "## O aliado de luta", "",
               "Metade do nível do grupo, metade dos PV, sem Convicção; não conta para Sozinho "
               "contra muitos.", "",
               "| Contra um rival do mesmo nível, com uma Convicção | Sozinho | Com o aliado |",
               "|---|---:|---:|"]
    for n in (3, 7, 11, 15, 19):
        so, com = aliado_no_duelo(n)
        linhas.append(f"| Nível {n} | {pct(so)} | {pct(com)} |")
    linhas += ["", "| Bronzes contra um Ouro do mesmo nível | Sem aliado | Com um aliado |",
               "|---|---:|---:|"]
    for n in (15, 20):
        for k in (3, 4):
            sem, com = aliado_no_grupo(n, k)
            linhas.append(f"| {k} Bronzes, nível {n} | {pct(sem)} | {pct(com)} |")
    linhas += ["", "| Quatro Bronzes contra um Ouro do mesmo nível | Vence | Caem | Rodadas |",
               "|---|---:|---:|---:|"]
    for n in (15, 17, 20):
        r = grupo_contra_um(grupo(n, 4), inimigo(n, "ouro", 2), n=NG, semente=740 + n)
        linhas.append(f"| Nível {n} | {pct(r['grupo'])} | {r['caidos_media']:.1f} | "
                      f"{r['rodadas_media']:.1f} |")

    print("fichas...")
    linhas += ["", "## As fichas prontas", "",
               "| Ficha | Quem enfrenta | Vence | Caem |", "|---|---|---:|---:|"]
    from inimigos import INIMIGOS
    for i, (chave, quem, n, k) in enumerate(FICHAS):
        r = contra_ficha(chave, n, k, lutas=N if k == 1 else NG, semente=800 + i)
        caem = "—" if r["caem"] is None else f"{r['caem']:.1f}"
        linhas.append(f"| {INIMIGOS[chave]['nome']} | {quem} | {pct(r['vence'])} | {caem} |")

    linhas += ["", "| Espectros juntos contra um Bronze | O Bronze vence |", "|---|---:|"]
    for i, (q, n) in enumerate(((2, 3), (2, 4), (3, 4), (3, 5))):
        linhas.append(f"| {q} Espectros contra um Bronze de nível {n} | "
                      f"{pct(varios_contra_um('espectro-terrestre', q, n, semente=900 + i))} |")
    for i, (q, n) in enumerate(((2, 2), (2, 3), (2, 4))):
        linhas.append(f"| {q} Espectros Novatos contra um Bronze de nível {n} | "
                      f"{pct(varios_contra_um('espectro-novato', q, n, semente=910 + i))} |")

    print("prova...")
    linhas += ["", "## Antes do Sexto Sentido: a prova da armadura", "",
               "Dois aprendizes do mesmo nível humano (FOR ou DES 12 e CON 11, que viram 15 e "
               "14 ao despertar) num duelo. Quem cai gasta a Convicção e levanta — humano, ou "
               "desperto.", "",
               "| Nível humano | PV | Golpe | Rodadas, sem despertar | Rodadas, despertando | "
               "Alguém desperta | Os dois despertam |", "|---:|---:|---|---:|---:|---:|---:|"]
    golpe_h, con_h = (R.mod(v) for v in R.DISTRIBUICAO_HUMANA[:2])
    for nh in R.NIVEIS_HUMANOS[R.NIVEL_DA_PROVA - 1:]:
        sem, com = prova(nh, despertar=False), prova(nh, despertar=True)
        linhas.append(f"| {nh} | {R.pv_humano(nh, con_h)} | 1d{R.dado_golpe_humano(nh)} + {golpe_h} | "
                      f"{sem['rodadas']:.1f} | {com['rodadas']:.1f} | {pct(com['despertou'])} | "
                      f"{pct(com['os_dois_despertam'])} |")
    linhas += ["", "Diante de um desperto, o humano é figurante: a linha do nível 1 da tabela de "
               "figurantes, na seção acima."]

    saida = pathlib.Path(__file__).parent / "MESTRE.md"
    saida.write_text("\n".join(linhas) + "\n", encoding="utf-8")
    print("\n".join(linhas))


if __name__ == "__main__":
    main()
