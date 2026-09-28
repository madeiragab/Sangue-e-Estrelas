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
from luta import duelos, grupo_contra_um, montar  # noqa: E402
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
    return lambda: montar("I", n, posto, conviccoes=conviccoes)


def aliado(n: int):
    """O aliado de luta: um inimigo da tabela rápida na metade do nível do grupo, com
    metade dos PV e sem Convicção."""
    a = montar("Aliado", R.nivel_do_aliado(n), conviccoes=0)
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
    derruba o bando inteiro; a de alvo único, três) e o golpe comum no resto. O
    bando ataca uma vez por rodada, com Vantagem enquanto houver mais de três de pé.
    Devolve as rodadas, a fração dos PV que ele perdeu e quantas vezes caiu."""
    rng = random.Random(semente)
    de, atk, dano = R.figurante(nivel)
    g = R.grau(nivel)
    if area:
        tec = Tecnica("área", "golpe", {"dano": 1, "area": 1}, grau=g)
        derruba_tec = tamanho
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
    """Dois aprendizes do mesmo nível humano na prova da armadura: FOR ou DES 15, CON 14.

    Cada um ataca uma vez por turno com o golpe de gente do nível dele. Quem cai a 0 PV
    gasta a Convicção e levanta com um quarto dos PV; com `despertar`, levanta desperto:
    um quarto dos PV do nível 1 de guerreiro, o Cosmo no Teto e a técnica assinatura (a
    grande do Grau 1). Devolve as rodadas, quantas provas tiveram alguém despertando e
    em quantas os dois despertaram."""
    rng = random.Random(semente)
    mod = 2
    pv_max = R.pv_humano(nivel_humano, mod)
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
                de = R.HUMANO_DEF + mod
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
                        pv[b] = max(1, (R.PV_BASE[1] + mod) // 4)
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
    ("espectro-terrestre", "Um Bronze de nível 3", 3, 1),
    ("espectro-terrestre", "Um Bronze de nível 4", 4, 1),
    ("cavaleiro-de-prata", "Um Bronze de nível 8", 8, 1),
    ("cavaleiro-de-prata", "Um Bronze de nível 9", 9, 1),
    ("cavaleiro-de-prata", "Um Bronze de nível 13", 13, 1),
    ("cavaleiro-de-prata", "Dois Bronzes de nível 9", 9, 2),
    ("cavaleiro-de-prata", "Três Bronzes de nível 9", 9, 3),
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
               f"{R.FIGURANTES_POR_TECNICA}; a de área, o bando inteiro.", "",
               "| Nível | DEF · ataque · dano | Seis, sem área | Seis, com área | Dez, sem área |",
               "|---:|---|---|---|---|"]
    for n in range(1, 21):
        de, atk, dano = R.figurante(n)
        cel = []
        for tam, area in ((6, False), (6, True), (10, False)):
            b = bando(n, tam, area, semente=n)
            c = f"{b['rodadas']:.1f} rodadas, {pct(b['perda'])} dos PV"
            if b["caiu"] >= 0.005:
                c += f", cai {pct(b['caiu'])}"
            cel.append(c)
        linhas.append(f"| {n} | {de} · +{atk} · {dano} | " + " | ".join(cel) + " |")

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

    print("prova...")
    linhas += ["", "## Antes do Sexto Sentido: a prova da armadura", "",
               "Dois aprendizes do mesmo nível humano (FOR ou DES 15 e CON 14) num duelo. Quem "
               "cai gasta a Convicção e levanta — humano, ou desperto.", "",
               "| Nível humano | PV | Golpe | Rodadas, sem despertar | Rodadas, despertando | "
               "Alguém desperta | Os dois despertam |", "|---:|---:|---|---:|---:|---:|---:|"]
    for nh in R.NIVEIS_HUMANOS[R.NIVEL_DA_PROVA - 1:]:
        sem, com = prova(nh, despertar=False), prova(nh, despertar=True)
        linhas.append(f"| {nh} | {R.pv_humano(nh, 2)} | 1d{R.dado_golpe_humano(nh)} + 2 | "
                      f"{sem['rodadas']:.1f} | {com['rodadas']:.1f} | {pct(com['despertou'])} | "
                      f"{pct(com['os_dois_despertam'])} |")
    linhas += ["", "Diante de um desperto, o humano é figurante: a linha do nível 1 da tabela de "
               "figurantes, na seção acima."]

    saida = pathlib.Path(__file__).parent / "MESTRE.md"
    saida.write_text("\n".join(linhas) + "\n", encoding="utf-8")
    print("\n".join(linhas))


if __name__ == "__main__":
    main()
