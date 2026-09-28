"""O sistema em condições extremas.

Onde `cenarios.py` mede o jogo como ele costuma ser jogado, este arquivo tenta
quebrá-lo: builds tortas, técnicas de condição, limitações baratas, políticas
exageradas, recursos no máximo e no zero, diferenças grandes de nível e de
Posto, escadas de sangue inteiras e lutas de grupo contra um só.

    python sim/extremos.py            (alguns minutos; escreve sim/EXTREMOS.md)
    python sim/extremos.py --rapido   (menos lutas por célula)
"""

from __future__ import annotations

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))

import regras as R  # noqa: E402
from luta import POLITICA_PADRAO, Lutador, duelos, grupo_contra_um, montar  # noqa: E402
from tecnica import Tecnica, tecnica_de_dano  # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

RAPIDO = "--rapido" in sys.argv
N = 300 if RAPIDO else 800
NG = 200 if RAPIDO else 500          # lutas de grupo são mais lentas
NIVEIS = (1, 5, 9, 13, 17)
SEMENTE = [1]


def semente() -> int:
    SEMENTE[0] += 1
    return SEMENTE[0]


def pct(x: float) -> str:
    return f"{x:.0%}"


def taxa(fa, fb, **kw) -> float:
    return duelos(fa, fb, n=N, semente=semente(), **kw)["a"]


def linha_por_nivel(nome: str, fa, fb, niveis=NIVEIS, **kw) -> str:
    cel = []
    for n in niveis:
        try:
            cel.append(pct(taxa(lambda: fa(n), lambda: fb(n), **kw)))
        except ValueError:
            cel.append("—")
    return f"| {nome} | " + " | ".join(cel) + " |"


def cabecalho(titulo: str, niveis=NIVEIS) -> list[str]:
    return [f"| {titulo} | " + " | ".join(f"Nível {n}" for n in niveis) + " |",
            "|---|" + "---:|" * len(niveis)]


# ---------------------------------------------------------------------------
# Builds
# ---------------------------------------------------------------------------

DISTRIBUICOES = {
    # nome: (atributo principal, segundo, terceiro, e o resto), natureza das técnicas
    "golpe": ("des", "con", "sab", "golpe"),
    "forca": ("for", "con", "sab", "golpe"),
    "cosmo": ("sab", "con", "des", "cosmo"),
    "tanque": ("con", "des", "sab", "golpe"),
    "vidro": ("des", "sab", "for", "golpe"),       # CON no 8
}


def montar_build(nome: str, nivel: int, build: str = "golpe", posto: str = "bronze",
                 kit: str = "padrao", **kw) -> Lutador:
    p1, p2, p3, natureza = DISTRIBUICOES[build]
    esc = kw.pop("escolhas", None) or R.escolhas_padrao(nivel)
    a1, a2 = R.atributos_das_escolhas(esc)
    valores = {p1: a1, p2: a2, p3: 13}
    resto = [a for a in ("for", "des", "con", "int", "sab", "car") if a not in valores]
    for a, v in zip(resto, (12, 10, 8)):
        valores[a] = v
    if build == "vidro":
        valores.update({"con": 8, "int": 10, "car": 12})
    g = R.grau(nivel)
    tam = R.TAMANHO_MAXIMO[g]
    tecs = kit_de_tecnicas(kit, tam, g, natureza, nivel)
    if posto == "ouro":
        tecs.append(Tecnica("assento", "golpe", {"dano": tam}, mais=("atravessa",), grau=g,
                            assento=True))
    pol = dict(POLITICA_PADRAO)
    pol.update(kw.pop("politica", {}))
    # a build de Cosmo dá o golpe comum com o Atributo do Cosmo
    atr_golpe = {"cosmo": "sab", "forca": "for"}.get(build, "des")
    return Lutador(nome, nivel, posto, valores, tecs, atr_golpe=atr_golpe,
                   atr_cosmo="sab", politica=pol, vigor=esc["vida_cosmo"].count("v"),
                   cosmo_escolhas=esc["vida_cosmo"].count("c"),
                   defesas_extra=esc["pericia_defesa"].count("d"), **kw)


def kit_de_tecnicas(kit: str, tam: int, g: int, natureza: str, nivel: int) -> list:
    grande = Tecnica("grande", natureza, {"dano": tam}, grau=g)
    pequena = Tecnica("pequena", natureza, {"dano": 2}, grau=g)
    media = Tecnica("media", natureza, {"dano": max(3, tam - 2)}, grau=g)
    base = [grande, pequena] + ([media] if R.tecnicas_conhecidas(nivel) >= 3 else [])
    if kit == "padrao":
        return base
    if kit == "so_grande":
        return [grande]
    if kit == "so_pequenas":
        return [pequena, Tecnica("pequena2", natureza, {"dano": 2}, grau=g),
                Tecnica("tres", natureza, {"dano": 3}, grau=g)]
    # Limitações: a grande fica com duas, e custa menos
    lim = {
        "lim_so_fere": ("fere",),
        "lim_so_desprevenido": ("desprevenido",),
        "lim_so_carregar": ("carregar",),
        "lim_so_uma_vez": ("uma_vez",),
        "lim_fere": ("fere", "desprevenido"),
        "lim_uma_vez": ("uma_vez", "fere"),
        "lim_carregar": ("carregar", "fere"),
        "lim_teto": ("teto", "fere"),
    }
    if kit in lim:
        barata = Tecnica("grande", natureza, {"dano": tam}, grau=g, limitacoes=len(lim[kit]),
                         limites=lim[kit])
        return [barata] + base[1:]
    # Condições: o kit padrão mais uma técnica de condição
    cond = {
        "atordoar": Tecnica("atordoar", natureza, {"cond_forte": 1}, grau=g, condicao="atordoado"),
        "paralisar": Tecnica("paralisar", natureza, {"cond_forte": 1}, grau=g, condicao="paralisado"),
        "cegar": Tecnica("cegar", natureza, {"cond_media": 1}, grau=g, condicao="cego"),
        "queimar": Tecnica("queimar", natureza, {"cond_media": 1}, grau=g, condicao="queimando"),
        "amedrontar": Tecnica("amedrontar", natureza, {"cond_media": 1}, grau=g, condicao="amedrontado"),
        "dano_atordoar": Tecnica("dano e atordoar", natureza, {"dano": 1, "cond_forte": 1}, grau=g,
                                 condicao="atordoado"),
    }
    uma_vez = kit.endswith("_uma_vez")
    if uma_vez:
        kit = kit[: -len("_uma_vez")]
    if kit in cond:
        t = cond[kit]
        if uma_vez:
            t.limites = ("uma_vez",)    # política, não limitação comprada: o custo não muda
        assert t.valida(), (kit, t.tamanho(), t.tamanho_maximo())
        return base + [t]
    raise ValueError(kit)


# ---------------------------------------------------------------------------
# Seções
# ---------------------------------------------------------------------------


def curva_de_nivel() -> list[str]:
    niveis = tuple(range(2, 21))
    cel1, cel2 = [], []
    for n in niveis:
        cel1.append(pct(taxa(lambda: montar("A", n), lambda: montar("B", n - 1))))
        cel2.append(pct(taxa(lambda: montar("A", n), lambda: montar("B", n - 2))) if n > 2 else "—")
    cab = "| | " + " | ".join(str(n) for n in niveis) + " |"
    return [cab, "|---|" + "---:|" * len(niveis),
            "| Um nível acima | " + " | ".join(cel1) + " |",
            "| Dois níveis acima | " + " | ".join(cel2) + " |"]


def builds() -> list[str]:
    out = cabecalho("Build contra o padrão (DES, CON, SAB; técnicas de Golpe)")
    for b, rot in (("cosmo", "Cosmo na frente, técnicas de Cosmo"), ("forca", "FOR na frente"),
                   ("tanque", "CON na frente"), ("vidro", "Canhão de vidro, CON 8")):
        out.append(linha_por_nivel(rot, lambda n, b=b: montar_build("A", n, b),
                                   lambda n: montar_build("B", n)))
    for k, rot in (("so_grande", "Só a técnica grande"), ("so_pequenas", "Só técnicas pequenas")):
        out.append(linha_por_nivel(rot, lambda n, k=k: montar_build("A", n, kit=k),
                                   lambda n: montar_build("B", n)))
    for ac in ("garras", "escudo", "asas"):
        out.append(linha_por_nivel(f"Acessório: {ac}", lambda n, ac=ac: montar("A", n, acessorio=ac),
                                   lambda n: montar("B", n)))
    out.append(linha_por_nivel("Só Vida contra só Cosmo, nas escolhas de nível",
                               lambda n: montar("A", n, escolhas=so_vida_ou_cosmo(n, "v")),
                               lambda n: montar("B", n, escolhas=so_vida_ou_cosmo(n, "c"))))
    return out


def so_vida_ou_cosmo(nivel: int, qual: str) -> dict:
    """As escolhas do padrão, mas com Vida (ou Cosmo) em todo nível."""
    esc = R.escolhas_padrao(nivel)
    esc["vida_cosmo"] = qual * (nivel - 1)
    return esc


def limitacoes() -> list[str]:
    out = cabecalho("A técnica grande com limitações (cada uma custa 1 a menos)")
    for k, rot in (("lim_so_fere", "Fere 1d6 por Grau"), ("lim_so_desprevenido", "Desprevenido"),
                   ("lim_so_uma_vez", "Uma vez por luta"), ("lim_so_carregar", "Exige carregar"),
                   ("lim_fere", "Fere e Desprevenido"), ("lim_uma_vez", "Uma vez por luta e fere"),
                   ("lim_carregar", "Exige carregar e fere"), ("lim_teto", "Só com o Cosmo no Teto e fere")):
        out.append(linha_por_nivel(rot, lambda n, k=k: montar_build("A", n, kit=k),
                                   lambda n: montar_build("B", n)))
    return out


def condicoes() -> list[str]:
    out = cabecalho("O kit padrão mais uma técnica de condição")
    for k, rot in (("atordoar", "Atordoar (forte, 4)"), ("paralisar", "Paralisar (forte, 4)"),
                   ("cegar", "Cegar (média, 2)"), ("queimar", "Queimando (média, 2)"),
                   ("amedrontar", "Amedrontar (média, 2)"), ("dano_atordoar", "Dano e atordoar (5)")):
        out.append(linha_por_nivel(rot, lambda n, k=k: montar_build("A", n, kit=k),
                                   lambda n: montar_build("B", n)))
    return out


def politicas() -> list[str]:
    out = cabecalho("Política extrema contra a padrão")
    for pol, rot in (({"aparar_limiar": 0.0}, "Apara tudo o que puder"),
                     ({"bloquear": False}, "Nunca bloqueia"),
                     ({"concentrar": False}, "Nunca concentra"),
                     ({"cegar_se": True}, "Se cega para despertar"),
                     ({"despertar": False}, "Nunca desperta o Sétimo")):
        out.append(linha_por_nivel(rot, lambda n, pol=pol: montar("A", n, politica=pol),
                                   lambda n: montar("B", n)))
    return out


def recursos() -> list[str]:
    out = cabecalho("Recursos no extremo")
    out.append(linha_por_nivel("Zero Convicções contra três", lambda n: montar("A", n, conviccoes=0),
                               lambda n: montar("B", n)))
    out.append(linha_por_nivel("Quatro Convicções contra três", lambda n: montar("A", n, conviccoes=4),
                               lambda n: montar("B", n, conviccoes=3)))
    for c in (1, 2, 3):
        out.append(linha_por_nivel(f"{c} Centelha(s) por rodada, espelho", lambda n: montar("A", n),
                                   lambda n: montar("B", n), centelhas_a=c))
    for c in (1, 3):
        out.append(linha_por_nivel(f"Bronze com {c} Centelha(s) por rodada contra Prata",
                                   lambda n: montar("A", n), lambda n: montar("B", n, "prata"),
                                   niveis=(9, 13, 17), centelhas_a=c))
    return out


def posto() -> list[str]:
    ks = (0, 1, 2, 3, 4, 5)
    out = ["| Quantos níveis acima | " + " | ".join(f"+{k}" for k in ks) + " |",
           "|---|" + "---:|" * len(ks)]
    for rot, fa, fb, base in (
        ("Bronze contra Prata do nível 9", lambda n: montar("A", n), lambda n: montar("B", n, "prata"), 9),
        ("Bronze contra Prata do nível 13", lambda n: montar("A", n), lambda n: montar("B", n, "prata"), 13),
        ("Bronze contra Ouro do nível 15", lambda n: montar("A", n), lambda n: montar("B", n, "ouro"), 15),
        ("Prata contra Ouro do nível 15", lambda n: montar("A", n, "prata"), lambda n: montar("B", n, "ouro"), 15),
    ):
        cel = []
        for k in ks:
            if base + k > 20:
                cel.append("—")
                continue
            cel.append(pct(taxa(lambda: fa(base + k), lambda: fb(base))))
        out.append(f"| {rot} | " + " | ".join(cel) + " |")
    return out


def grupos() -> list[str]:
    out = ["| Grupo contra um chefe do mesmo nível | 2 | 3 | 4 | 5 |", "|---|---:|---:|---:|---:|"]
    casos = [
        ("Bronzes contra um Bronze, nível 5", 5, "bronze", "bronze"),
        ("Bronzes contra um Prata, nível 9", 9, "bronze", "prata"),
        ("Bronzes contra um Prata, nível 13", 13, "bronze", "prata"),
        ("Bronzes contra um Ouro, nível 15", 15, "bronze", "ouro"),
        ("Bronzes contra um Ouro, nível 20", 20, "bronze", "ouro"),
        ("Pratas contra um Ouro, nível 17", 17, "prata", "ouro"),
    ]
    for rot, n, pg, pc in casos:
        for regra in (False, True):
            cel = []
            for k in (2, 3, 4, 5):
                r = grupo_contra_um(lambda: [montar(f"P{i}", n, pg) for i in range(k)],
                                    lambda: montar("C", n, pc), n=NG, semente=semente(),
                                    sozinho_contra_muitos=regra)
                cel.append(f"{pct(r['grupo'])} ({r['caidos_media']:.1f} caem)")
            marca = "com Sozinho contra muitos" if regra else "sem a regra"
            out.append(f"| {rot}, {marca} | " + " | ".join(cel) + " |")
    # um atordoador no grupo
    out += ["", "| Quatro Bronzes, um deles com Atordoar, contra um Ouro | Nível 15 | Nível 20 |",
            "|---|---:|---:|"]
    cel = []
    for n in (15, 20):
        r = grupo_contra_um(lambda: [montar_build("P0", n, kit="atordoar")]
                            + [montar(f"P{i}", n) for i in range(1, 4)],
                            lambda: montar("C", n, "ouro"), n=NG, semente=semente())
        cel.append(pct(r["grupo"]))
    out.append("| Com a regra | " + " | ".join(cel) + " |")
    # as fichas prontas contra um grupo de quatro
    import inimigos as I
    out += ["", "| Ficha pronta contra quatro Bronzes | Nível do grupo | O grupo vence | Caem |",
            "|---|---:|---:|---:|"]
    for chave, n in (("cavaleiro-de-prata", 9), ("guerreiro-deus", 12), ("guerreiro-deus", 15),
                     ("cavaleiro-de-ouro", 15), ("juiz-do-inferno", 17)):
        r = grupo_contra_um(lambda: [montar(f"P{i}", n) for i in range(4)],
                            lambda: I.lutador(chave), n=NG, semente=semente())
        out.append(f"| {I.INIMIGOS[chave]['nome']} | {n} | {pct(r['grupo'])} | {r['caidos_media']:.1f} |")
    return out


def duracao() -> list[str]:
    out = ["| Confronto | Rodadas (média) | Empates por tempo |", "|---|---:|---:|"]
    g6 = ("guerreiro",) * 6
    for rot, fa, fb in (
        ("Tanque contra tanque, nível 17", lambda: montar_build("A", 17, "tanque"),
         lambda: montar_build("B", 17, "tanque")),
        ("Ouro revivido seis vezes e com sangue de deus, espelho, nível 20",
         lambda: montar("A", 20, "ouro", formas=g6 + ("deus",)),
         lambda: montar("B", 20, "ouro", formas=g6 + ("deus",))),
        ("Apara tudo, espelho, nível 13", lambda: montar("A", 13, politica={"aparar_limiar": 0.0}),
         lambda: montar("B", 13, politica={"aparar_limiar": 0.0})),
    ):
        r = duelos(fa, fb, n=N, semente=semente())
        out.append(f"| {rot} | {r['rodadas_media']:.1f} | {pct(max(0.0, r['empate'] - r['mil_dias']))} |")
    return out


def condicoes_uma_vez() -> list[str]:
    out = cabecalho("A condição média usada uma vez, na hora certa")
    for k, rot in (("cegar", "Cegar"), ("queimar", "Queimando"), ("amedrontar", "Amedrontar")):
        out.append(linha_por_nivel(rot, lambda n, k=k: montar_build("A", n, kit=k + "_uma_vez"),
                                   lambda n: montar_build("B", n)))
    return out


def fronteiras_de_grau() -> list[str]:
    """O personagem (3 Convicções) contra um inimigo que já cruzou o Grau."""
    out = ["| Personagem contra inimigo dois níveis acima | Dentro da faixa | Cruzando o Grau |",
           "|---|---:|---:|"]
    for rot, conv in (("Nomeado sem Convicção", 0), ("Rival com uma Convicção", 1)):
        dentro = [taxa(lambda: montar("A", a, conviccoes=3), lambda: montar("B", a + 2, conviccoes=conv))
                  for a in (1, 5, 9, 13, 17)]
        cruza = [taxa(lambda: montar("A", a, conviccoes=3), lambda: montar("B", a + 2, conviccoes=conv))
                 for a in (3, 7, 11, 15)]
        out.append(f"| {rot} | {pct(min(dentro))} a {pct(max(dentro))} "
                   f"| {pct(min(cruza))} a {pct(max(cruza))} |")
    return out


def caracteristicas() -> list[str]:
    import inimigos as I
    out = cabecalho("Com a característica, contra a mesma armadura sem nenhuma")
    for c, (nome, _) in I.CARACTERISTICAS.items():
        if c == "elmo_fechado":
            continue                    # o simulador não arranca sentidos
        out.append(linha_por_nivel(nome, lambda n, c=c: montar("A", n, caracteristicas=(c,)),
                                   lambda n: montar("B", n, caracteristicas=())))
    return out


def main() -> None:
    partes = [
        "# O sistema em condições extremas",
        "",
        f"Gerado por `python sim/extremos.py`. {N} duelos por célula ({NG} nas lutas de grupo), "
        "sementes fixas. Porcentagem de vitórias de quem está na linha, contra o padrão do "
        "livro montado no mesmo nível (DES 15, CON 14, SAB 13; técnica grande, pequena e média).",
        "",
        "## Um nível faz quanta diferença", "", *curva_de_nivel(), "",
        "## Builds", "", *builds(), "",
        "## Limitações", "", *limitacoes(), "",
        "## Técnicas de condição", "", *condicoes(), "",
        "## Políticas extremas", "", *politicas(), "",
        "## Recursos", "", *recursos(), "",
        "## Posto e nível", "", *posto(), "",
        "## Grupo contra um", "",
        "O grupo inteiro bate no inimigo; o inimigo bate sempre no mais ferido de pé.", "",
        *grupos(), "",
        "## Duração", "", *duracao(), "",
        "## Condições médias, usadas uma vez", "",
        "A mesma técnica da seção de condições, mas usada uma vez só por luta.", "",
        *condicoes_uma_vez(), "",
        "## Fronteiras de Grau", "",
        "Desde a 0.7.0 o dano de cada ponto e os PV sobem nível a nível, sem saltar quando o "
        "Grau muda. Esta tabela confere: o inimigo que já cruzou o Grau não pesa mais que o "
        "que ainda não cruzou. Dentro da faixa: personagem de nível 1, 5, 9, 13, 17. "
        "Cruzando: 3, 7, 11, 15 (o inimigo já está no Grau seguinte).", "",
        *fronteiras_de_grau(), "",
        "## Características da armadura", "", *caracteristicas(), "",
    ]
    texto = "\n".join(partes)
    (pathlib.Path(__file__).parent / "EXTREMOS.md").write_text(texto, encoding="utf-8")
    print(texto)


if __name__ == "__main__":
    main()
