"""Os experimentos que decidiram os números da versão atual.

Roda tudo e escreve sim/RESULTADOS.md — as tabelas que o README mostra.

    python sim/cenarios.py            (leva alguns minutos)
    python sim/cenarios.py --rapido   (menos lutas por linha, para conferir)

Cada linha é um duelo repetido muitas vezes com sementes fixas: o mesmo
comando dá sempre o mesmo resultado.
"""

from __future__ import annotations

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))

import regras as R  # noqa: E402
from luta import duelos, montar  # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

RAPIDO = "--rapido" in sys.argv
N = 400 if RAPIDO else 1500
NIVEIS = (1, 4, 5, 8, 9, 12, 13, 16, 17, 20)
NIVEIS_CURTOS = (1, 5, 9, 13, 15, 17, 20)


def pct(x: float) -> str:
    return f"{x:.0%}"


def varredura_de_niveis() -> list[str]:
    linhas = [
        "| Nível | PV | Rodadas, com Convicções | Rodadas, sem | Dano vindo de técnicas | Quem não usa técnica vence |",
        "|---:|---:|---:|---:|---:|---:|",
    ]
    for n in NIVEIS:
        com = duelos(lambda: montar("A", n), lambda: montar("B", n), n=N, semente=n)
        sem = duelos(lambda: montar("A", n, conviccoes=0), lambda: montar("B", n, conviccoes=0),
                     n=N, semente=100 + n)
        st = duelos(lambda: montar("A", n, politica={"tecnicas": False}), lambda: montar("B", n),
                    n=N, semente=200 + n)
        pv = montar("X", n).pv_max
        linhas.append(f"| {n} | {pv} | {com['rodadas_media']:.1f} | {sem['rodadas_media']:.1f} "
                      f"| {pct(com['parte_tecnica'])} | {pct(st['a'])} |")
    return linhas


GUERREIRO = ("guerreiro",) * 3

CONFRONTOS = [
    ("Espelho: Bronze contra Bronze", lambda n: montar("A", n), lambda n: montar("B", n), {}),
    ("Quem não apara a armadura", lambda n: montar("A", n, politica={"aparar": False}),
     lambda n: montar("B", n), {}),
    ("Quem nunca queima", lambda n: montar("A", n, politica={"queimar": False}),
     lambda n: montar("B", n), {}),
    ("Quem nunca levanta", lambda n: montar("A", n, politica={"levantar": False}),
     lambda n: montar("B", n), {}),
    ("Prata contra Bronze", lambda n: montar("A", n, "prata"), lambda n: montar("B", n), {}),
    ("Bronze contra Prata", lambda n: montar("A", n), lambda n: montar("B", n, "prata"), {}),
    ("Prata contra Ouro", lambda n: montar("A", n, "prata"), lambda n: montar("B", n, "ouro"), {}),
    ("Um nível acima", lambda n: montar("A", n + 1), lambda n: montar("B", n), {}),
    ("Dois níveis acima", lambda n: montar("A", n + 2), lambda n: montar("B", n), {}),
    ("Bronze sozinho contra Ouro", lambda n: montar("A", n), lambda n: montar("B", n, "ouro"), {}),
    ("Bronze com uma Centelha por rodada contra Ouro", lambda n: montar("A", n),
     lambda n: montar("B", n, "ouro"), {"centelhas_a": 1}),
    ("Bronze que se cega contra Ouro", lambda n: montar("A", n, politica={"cegar_se": True}),
     lambda n: montar("B", n, "ouro"), {}),
    ("Armadura revivida três vezes (V4) contra a original",
     lambda n: montar("A", n, formas=GUERREIRO), lambda n: montar("B", n), {}),
    ("V4 com a forma de elite contra a original",
     lambda n: montar("A", n, formas=GUERREIRO + ("elite",)), lambda n: montar("B", n), {}),
    ("Bronze V4 com a forma de elite contra Ouro",
     lambda n: montar("A", n, formas=GUERREIRO + ("elite",)), lambda n: montar("B", n, "ouro"), {}),
    ("Bronze com as cinco formas, até a de deus, contra Ouro",
     lambda n: montar("A", n, formas=GUERREIRO + ("elite", "deus")), lambda n: montar("B", n, "ouro"), {}),
    ("Prata revivida seis vezes contra a original",
     lambda n: montar("A", n, "prata", formas=GUERREIRO * 2), lambda n: montar("B", n, "prata"), {}),
    ("Prata com a escada inteira (seis, elite, deus) contra Ouro",
     lambda n: montar("A", n, "prata", formas=GUERREIRO * 2 + ("elite", "deus")),
     lambda n: montar("B", n, "ouro"), {}),
    ("Ouro revivido nove vezes contra o original",
     lambda n: montar("A", n, "ouro", formas=GUERREIRO * 3), lambda n: montar("B", n, "ouro"), {}),
    ("Garras contra nenhum acessório", lambda n: montar("A", n, acessorio="garras"),
     lambda n: montar("B", n), {}),
    ("Escudo contra nenhum acessório", lambda n: montar("A", n, acessorio="escudo"),
     lambda n: montar("B", n), {}),
]


def existe(nome: str, n: int) -> bool:
    """Um confronto só é medido nos níveis em que os Postos dele existem."""
    if nome in ("Um nível acima", "Dois níveis acima"):
        return n + (1 if nome.startswith("Um") else 2) <= 20
    if "Ouro" in nome:
        return R.posto_existe("ouro", n)
    if "Prata" in nome:
        return R.posto_existe("prata", n)
    return True


def confrontos() -> list[str]:
    cab = "| Confronto | " + " | ".join(f"Nível {n}" for n in NIVEIS_CURTOS) + " |"
    sep = "|---|" + "---:|" * len(NIVEIS_CURTOS)
    linhas = [cab, sep]
    for i, (nome, fa, fb, kw) in enumerate(CONFRONTOS):
        celulas = []
        for n in NIVEIS_CURTOS:
            if not existe(nome, n):
                celulas.append("—")
                continue
            r = duelos(lambda: fa(n), lambda: fb(n), n=N, semente=1000 * (i + 1) + n, **kw)
            cel = pct(r["a"])
            if r["empate"] >= 0.05:
                cel += f" ({pct(r['empate'])} emp.)"
            celulas.append(cel)
        linhas.append(f"| {nome} | " + " | ".join(celulas) + " |")
    return linhas


def mil_dias() -> list[str]:
    linhas = ["| Confronto | " + " | ".join(f"Nível {n}" for n in NIVEIS_CURTOS) + " |",
              "|---|" + "---:|" * len(NIVEIS_CURTOS)]
    for nome, fa, fb in (
        ("Ouro contra Ouro", lambda n: montar("A", n, "ouro"), lambda n: montar("B", n, "ouro")),
        ("Bronze contra Bronze", lambda n: montar("A", n), lambda n: montar("B", n)),
    ):
        cel = []
        for n in NIVEIS_CURTOS:
            if not existe(nome, n):
                cel.append("—")
                continue
            r = duelos(lambda: fa(n), lambda: fb(n), n=N, semente=7000 + n)
            cel.append(pct(r["mil_dias"]))
        linhas.append(f"| {nome} | " + " | ".join(cel) + " |")
    return linhas


def main() -> None:
    partes = [
        "# Resultados do simulador",
        "",
        "Gerado por `python sim/cenarios.py`. Cada célula é a média de "
        f"{N} duelos com sementes fixas. Os lutadores são montados pelo livro: "
        "15/14/13/12/10/8 com DES e CON na frente, duas técnicas de dano (a grande, "
        "no tamanho máximo, e uma pequena) e a política de jogo escrita em `sim/luta.py`.",
        "",
        "## A luta ao longo dos níveis",
        "",
        "Espelho de Bronze contra Bronze. *Rodadas* é a duração média da luta; "
        "*com Convicções* quer dizer que os dois podem levantar uma vez.",
        "",
        *varredura_de_niveis(),
        "",
        "## Regra por regra",
        "",
        "Porcentagem de vitórias do primeiro lutador. O espelho deve ficar perto de 50%; "
        "o resto mostra quanto cada escolha vale. O traço é um Posto que não existe "
        f"naquele nível: Prata só a partir do {R.NIVEL_PRATA}, elite só a partir do {R.NIVEL_ELITE}.",
        "",
        *confrontos(),
        "",
        "## Guerra dos Mil Dias",
        "",
        "Em quantas lutas os Cosmos travam num choque de técnicas.",
        "",
        *mil_dias(),
        "",
    ]
    texto = "\n".join(partes)
    destino = pathlib.Path(__file__).parent / "RESULTADOS.md"
    destino.write_text(texto, encoding="utf-8")
    print(texto)


if __name__ == "__main__":
    main()
