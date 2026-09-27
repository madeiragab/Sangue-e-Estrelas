"""Toda a conferência do sistema, sem dependências externas.

    python test.py            tudo (leva uns segundos)
    python test.py motor      só as contas das técnicas
    python test.py livro      só o build e a coerência do livro
    python test.py equilibrio só as metas de equilíbrio
    python test.py extremos   só as metas dos testes de estresse

Quatro blocos:

  motor       as técnicas impressas no livro têm o tamanho e o custo que o
              motor do Capítulo Seis calcula;
  livro       o build roda, todo link interno tem destino, e as tabelas
              geradas a partir de sim/regras.py estão no livro;
  equilibrio  as metas de equilíbrio, medidas em duelos com semente fixa;
  extremos    o que o teste de estresse (sim/extremos.py) achou e o livro
              corrigiu: grupo contra chefe, build de Cosmo, atordoar,
              limitações.

Uma meta que falha não é um teste quebrado: é o simulador avisando que uma
mudança de regra mexeu no jogo. Ou a regra volta, ou a meta muda — e a mudança
vai para o CHANGELOG.
"""

from __future__ import annotations

import pathlib
import subprocess
import sys

RAIZ = pathlib.Path(__file__).parent
sys.path.insert(0, str(RAIZ / "sim"))

import regras as R  # noqa: E402
from luta import duelos, montar  # noqa: E402
from tecnica import Tecnica  # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

falhas: list[str] = []


def confere(cond: bool, texto: str) -> None:
    print(("  OK   " if cond else "  FALHA ") + texto)
    if not cond:
        falhas.append(texto)


# ---------------------------------------------------------------------------
# Motor
# ---------------------------------------------------------------------------

# (técnica, tamanho impresso, custo impresso)
IMPRESSAS = [
    (Tecnica("Punho de Meteoros", "golpe", {"dano": 2}), 2, 2),
    (Tecnica("Poeira de Gelo", "cosmo", {"area": 2, "cond_fraca": 1}, alcance="curto"), 3, 3),
    (Tecnica("Corrente Circular", "cosmo", {"defesa": 1}, ativacao="reacao", alcance="curto"), 2, 2),
    (Tecnica("Asas Flamejantes", "cosmo", {"dano": 3}, alcance="medio", mais=("quebra",)), 5, 5),
    (Tecnica("Dragão Ascendente", "golpe", {"dano": 2, "cond_fraca": 1}, limitacoes=1), 3, 2),
    (Tecnica("Golpe Fantasma", "cosmo", {"cond_media": 1}), 2, 2),
    (Tecnica("Muralha de Cosmo", "cosmo", {"pv_temp": 2}, duracao="cena", alcance="pessoal"), 5, 5),
    (Tecnica("Passo de Luz", "golpe", {"movimento": 1}, ativacao="bonus", alcance="pessoal"), 2, 2),
    (Tecnica("Excalibur", "golpe", {"dano": 4}, alcance="medio", mais=("atravessa",),
             grau=3, assento=True), 7, 7),
    (Tecnica("Cólera dos Cem Dragões", "cosmo", {"area": 4}, alcance="medio",
             area_dobrada=True, grau=3, assento=True), 7, 7),
    (Tecnica("Trovão Atômico", "golpe", {"dano": 3}, alcance="longo", mais=("ignora_cobertura",),
             grau=3, assento=True), 7, 7),
    (Tecnica("Garra que Rasga o Céu", "golpe", {"dano": 2}, mais=("quebra",)), 3, 3),
    (Tecnica("Olhos do Lince", "cosmo", {"vantagem": 1}, ativacao="reacao", alcance="curto"), 2, 2),
]


def testar_motor() -> None:
    print("motor de técnicas:")
    for t, tam, custo in IMPRESSAS:
        confere(t.tamanho() == tam and t.custo() == custo and t.valida(),
                f"{t.nome}: tamanho {t.tamanho()} (livro {tam}), custo {t.custo()} (livro {custo})")
    # o piso das limitações: nunca abaixo da metade do tamanho
    t = Tecnica("teste", "golpe", {"dano": 5}, limitacoes=5)
    confere(t.custo() == 3, "limitações param na metade do tamanho, arredondada para cima")


# ---------------------------------------------------------------------------
# Livro
# ---------------------------------------------------------------------------


def testar_livro() -> None:
    print("livro:")
    r = subprocess.run([sys.executable, str(RAIZ / "build.py")], capture_output=True,
                       text=True, encoding="utf-8")
    confere(r.returncode == 0, "build.py roda sem erro (marcadores e links internos)")
    if r.returncode != 0:
        print(r.stdout, r.stderr)
        return
    html = (RAIZ / "livro.html").read_text(encoding="utf-8")
    for posto, (bonus, res) in R.POSTO.items():
        nome = {"bronze": "Bronze", "prata": "Prata", "ouro": "Ouro", "divina": "Forma Divina"}[posto]
        linha = f'<tr><td>{nome}</td><td class="num">+{bonus}</td><td class="num">{res}</td></tr>'
        confere(linha in html, f"tabela de Posto: {nome} +{bonus} DEF, Resistência {res}")
    for sangue in R.FORMA:
        vezes = "".join(f'<td class="num">{R.REVIVIDAS_MAX[sangue][p] or "—"}</td>'
                        for p in ("bronze", "prata", "ouro"))
        confere(vezes in html, f"escada do sangue: {sangue} revive "
                f"{'/'.join(str(R.REVIVIDAS_MAX[sangue][p]) for p in ('bronze', 'prata', 'ouro'))} vezes")
    g = ("guerreiro",)
    confere(R.formas_validas("prata", g * 4 + ("elite", "deus"))
            and R.formas_validas("ouro", g * 6 + ("deus",))
            and not R.formas_validas("prata", g * 5)
            and not R.formas_validas("ouro", g * 7)
            and not R.formas_validas("bronze", g * 4)
            and not R.formas_validas("ouro", g + ("elite",))
            and not R.formas_validas("bronze", ("elite", "guerreiro")),
            "escada do sangue: limites por Posto, sem degrau de elite no Ouro, sempre subindo")
    from inimigos import descricao_forma
    for sangue in R.FORMA:
        confere(descricao_forma(sangue) in html, f"escada do sangue: o bônus de {sangue} está no livro")
    # o exemplo do Capítulo Sete: três formas de guerreiro e uma de elite
    b = R.bonus_das_formas(g * 3 + ("elite",))
    confere(b == {"def": 1, "res": 1, "acerto": 2}
            and "DEF +3</strong>" in html and "Resistência 4</strong>" in html
            and "+2 no acerto</strong>" in html,
            f"exemplo da armadura do Téo bate com a regra ({b})")
    for n in (1, 5, 9, 13, 17, 20):
        trecho = f'<td class="num">{n}</td><td class="num">+{R.prof(n)}</td><td class="num">{R.grau(n)}</td><td class="num">{R.teto_base(n)}</td>'
        confere(trecho in html, f"tabela de níveis: nível {n}")
    confere(f"nível {R.NIVEL_ATAQUE_EXTRA}" in html.lower() or f"nível {R.NIVEL_ATAQUE_EXTRA}" in html,
            f"o Ataque Extra está no nível {R.NIVEL_ATAQUE_EXTRA}")
    confere(f"<strong>Prata:</strong> a partir do nível {R.NIVEL_PRATA}." in html
            and f"<strong>Elite:</strong> a partir do nível {R.NIVEL_ELITE}," in html,
            f"o livro dá o requisito de Posto: Prata no {R.NIVEL_PRATA}, elite no {R.NIVEL_ELITE}")
    from inimigos import INIMIGOS
    for slug, ficha in INIMIGOS.items():
        confere(R.posto_existe(ficha["posto"], ficha["nivel"]),
                f"ficha pronta {slug}: nível {ficha['nivel']} cabe no Posto {ficha['posto']}")


# ---------------------------------------------------------------------------
# Equilíbrio
# ---------------------------------------------------------------------------

N = 500


def taxa(fa, fb, n_nivel: int, semente: int, **kw) -> dict:
    return duelos(lambda: fa(n_nivel), lambda: fb(n_nivel), n=N, semente=semente, **kw)


def vitorias_levantando(nivel: int, semente: int) -> float:
    """Das vitórias do Bronze (com Centelhas) sobre o Ouro, quantas vieram depois de levantar."""
    import random
    from luta import Luta
    rng = random.Random(semente)
    a, b = montar("Bronze", nivel), montar("Ouro", nivel, "ouro")
    vit = lev = 0
    for _ in range(N * 2):
        r = Luta(a, b, rng, centelhas_a=1).lutar()
        if r.vencedor == "Bronze":
            vit += 1
            lev += r.detalhes["Bronze"]["levantou"] > 0
    return lev / vit if vit else 1.0


# A luta é curta e decisiva no começo e longa e destrutiva no fim (0.6.0).
FAIXA_SEM = {1: (2.0, 4.0), 5: (3.5, 6.5), 9: (4.0, 7.5), 13: (3.5, 7.0), 15: (3.5, 7.5),
             17: (4.5, 8.5), 20: (5.5, 9.5)}
FAIXA_COM = {1: (3.0, 5.5), 5: (4.5, 8.0), 9: (5.5, 9.5), 13: (5.0, 9.0), 15: (5.0, 9.5),
             17: (7.0, 11.5), 20: (8.0, 13.0)}


def testar_equilibrio() -> None:
    print(f"equilíbrio ({N} duelos por linha):")
    for n in (1, 5, 9, 13, 15, 17, 20):
        r = taxa(lambda k: montar("A", k), lambda k: montar("B", k), n, 11 + n)
        confere(0.40 <= r["a"] <= 0.60, f"nível {n}: espelho Bronze×Bronze perto de 50% ({r['a']:.0%})")
        s = taxa(lambda k: montar("A", k, conviccoes=0), lambda k: montar("B", k, conviccoes=0), n, 21 + n)
        lo, hi = FAIXA_SEM[n]
        confere(lo <= s["rodadas_media"] <= hi,
                f"nível {n}: luta sem Convicções dura {lo:g} a {hi:g} rodadas ({s['rodadas_media']:.1f})")
        lo, hi = FAIXA_COM[n]
        confere(lo <= r["rodadas_media"] <= hi,
                f"nível {n}: luta com Convicções dura {lo:g} a {hi:g} rodadas ({r['rodadas_media']:.1f})")
        t = taxa(lambda k: montar("A", k, politica={"tecnicas": False}), lambda k: montar("B", k), n, 31 + n)
        confere(t["a"] <= 0.45, f"nível {n}: técnica vale mais que só golpe comum ({t['a']:.0%} sem técnica)")
        ap = taxa(lambda k: montar("A", k, politica={"aparar": False}), lambda k: montar("B", k), n, 41 + n)
        # no nível 1, com a luta curta, bloquear em vez de aparar rende um pouco: até 58%
        confere(ap["a"] <= 0.58, f"nível {n}: apanhar sem aparar não compensa ({ap['a']:.0%})")
        q = taxa(lambda k: montar("A", k, politica={"queimar": False}), lambda k: montar("B", k), n, 51 + n)
        confere(0.30 <= q["a"] <= 0.60, f"nível {n}: queimar ajuda sem dominar ({q['a']:.0%} de quem nunca queima)")
        # Prata e Ouro só são medidos onde existem: o Posto tem requisito de nível
        if R.posto_existe("prata", n):
            p = taxa(lambda k: montar("A", k, "prata"), lambda k: montar("B", k), n, 61 + n)
            confere(0.70 <= p["a"] <= 0.92,
                    f"nível {n}: o Bronze normalmente perde para o Prata ({p['a']:.0%} do Prata)")
            g = ("guerreiro",) * 3
            f4 = taxa(lambda k: montar("A", k, formas=g), lambda k: montar("B", k), n, 66 + n)
            fe = taxa(lambda k: montar("A", k, formas=g + ("elite",)), lambda k: montar("B", k), n, 67 + n)
            confere(0.50 <= f4["a"] <= 0.75 and fe["a"] >= f4["a"] - 0.02,
                    f"nível {n}: cada forma nova ajuda (V4 {f4['a']:.0%}, com sangue de elite {fe['a']:.0%})")
        if not R.posto_existe("ouro", n):
            continue
        o = taxa(lambda k: montar("A", k), lambda k: montar("B", k, "ouro"), n, 71 + n)
        confere(o["a"] <= 0.07, f"nível {n}: Bronze sozinho quase nunca vence um Ouro ({o['a']:.0%})")
        confere(p["b"] >= o["a"] + 0.05,
                f"nível {n}: o Bronze perde mais para o Ouro que para o Prata ({o['a']:.0%} × {p['b']:.0%})")
        tudo = ("guerreiro",) * 3 + ("elite", "deus")
        fd = taxa(lambda k: montar("A", k, formas=tudo), lambda k: montar("B", k, "ouro"), n, 87 + n)
        confere(fd["a"] <= 0.25,
                f"nível {n}: nem com sangue de deus a armadura de Bronze iguala o Ouro ({fd['a']:.0%})")
        pd = taxa(lambda k: montar("A", k, "prata", formas=("guerreiro",) * 4 + ("elite", "deus")),
                  lambda k: montar("B", k, "ouro"), n, 85 + n)
        confere(pd["a"] <= 0.40,
                f"nível {n}: nem a Prata com a escada inteira iguala o Ouro ({pd['a']:.0%})")
        o6 = taxa(lambda k: montar("A", k, "ouro", formas=("guerreiro",) * 6),
                  lambda k: montar("B", k, "ouro"), n, 84 + n)
        confere(0.55 <= o6["a"] <= 0.80,
                f"nível {n}: o Ouro revivido seis vezes é forte, não imbatível ({o6['a']:.0%})")
        oc = taxa(lambda k: montar("A", k), lambda k: montar("B", k, "ouro"), n, 81 + n, centelhas_a=1)
        # do 15 em diante a Centelha vale cerca de 1 ponto: a margem cobre o acaso de 500 duelos
        confere(o["a"] - 0.03 <= oc["a"] <= 0.18,
                f"nível {n}: Centelhas não tiram o Ouro do lugar ({o['a']:.0%} → {oc['a']:.0%})")
        po = taxa(lambda k: montar("A", k, "prata"), lambda k: montar("B", k, "ouro"), n, 86 + n)
        confere(po["a"] <= 0.12, f"nível {n}: Prata sozinho quase nunca vence um Ouro ({po['a']:.0%})")
        lev = vitorias_levantando(n, 88 + n)
        confere(lev >= 0.70, f"nível {n}: quando o Bronze vence o Ouro, quase sempre levantou do chão ({lev:.0%})")
        mil = taxa(lambda k: montar("A", k, "ouro"), lambda k: montar("B", k, "ouro"), n, 91 + n)
        confere(0.03 <= mil["mil_dias"] <= 0.30,
                f"nível {n}: Guerra dos Mil Dias é rara mas acontece entre Ouros ({mil['mil_dias']:.0%})")


def testar_extremos() -> None:
    """O que o sim/extremos.py achou e o livro corrigiu não pode voltar."""
    import inimigos as I
    from extremos import montar_build
    from luta import grupo_contra_um
    print(f"extremos ({N} duelos por linha):")
    confere(set(I.CARACTERISTICAS) >= set(R.CARACTERISTICAS_PADRAO),
            "as características dos lutadores de referência estão na tabela do livro")
    for n in (15, 20):
        g4 = grupo_contra_um(lambda: [montar(f"P{i}", n) for i in range(4)],
                             lambda: montar("C", n, "ouro"), n=300, semente=200 + n)
        g2 = grupo_contra_um(lambda: [montar(f"P{i}", n) for i in range(2)],
                             lambda: montar("C", n, "ouro"), n=300, semente=210 + n)
        confere(0.30 <= g4["grupo"] <= 0.65 and g2["grupo"] <= 0.30,
                f"nível {n}: Sozinho contra muitos segura o Ouro diante do grupo "
                f"(4 Bronzes {g4['grupo']:.0%}, 2 Bronzes {g2['grupo']:.0%})")
    for n in (9, 13, 17):
        c = taxa(lambda k: montar_build("A", k, "cosmo"), lambda k: montar_build("B", k), n, 220 + n)
        confere(0.35 <= c["a"] <= 0.65, f"nível {n}: quem luta pelo Cosmo empata com quem luta pela DES ({c['a']:.0%})")
    from extremos import so_vida_ou_cosmo
    for n in (5, 13, 17, 20):
        v = taxa(lambda k: montar("A", k, escolhas=so_vida_ou_cosmo(k, "v")),
                 lambda k: montar("B", k, escolhas=so_vida_ou_cosmo(k, "c")), n, 225 + n)
        confere(0.25 <= v["a"] <= 0.78,
                f"nível {n}: nem só Vida nem só Cosmo domina ({v['a']:.0%} da Vida)")
    for n in (5, 9, 13):
        a = taxa(lambda k: montar_build("A", k, kit="atordoar"), lambda k: montar_build("B", k), n, 230 + n)
        confere(a["a"] <= 0.65, f"nível {n}: atordoar não decide a luta sozinho ({a['a']:.0%})")
    for c, (nome, _) in I.CARACTERISTICAS.items():
        if c == "elmo_fechado":
            continue
        v = [taxa(lambda k: montar("A", k, caracteristicas=(c,)),
                  lambda k: montar("B", k, caracteristicas=()), n, 250 + n)["a"] for n in (5, 13)]
        confere(all(0.42 <= x <= 0.64 for x in v),
                f"característica {nome}: um empurrão, nunca a luta ({v[0]:.0%} e {v[1]:.0%})")
    for kit in ("lim_so_fere", "lim_so_desprevenido", "lim_so_uma_vez", "lim_so_carregar"):
        r = taxa(lambda k: montar_build("A", k, kit=kit), lambda k: montar_build("B", k), 13, 240)
        confere(r["a"] <= 0.60, f"nível 13: a limitação {kit[7:]} custa de verdade ({r['a']:.0%})")


def testar_mestre() -> None:
    """As promessas dos Capítulos Dez e Onze: nível sem salto, figurantes, aliado de
    luta e as fichas prontas (sim/mestre.py)."""
    import mestre as M
    print(f"mestre ({N} duelos por linha, 200 nas lutas de grupo):")
    # um nível acima pesa parecido em toda a campanha, até na troca de Grau
    for n in (5, 9, 13, 14, 17):
        u = taxa(lambda k: montar("A", k), lambda k: montar("B", k - 1), n, 300 + n)
        confere(0.52 <= u["a"] <= 0.90, f"nível {n}: um nível acima pesa sem saltar ({u['a']:.0%})")
    for n in (1, 4, 8, 9, 14, 20):
        b = M.bando(n, 6, lutas=1000, semente=n)
        a = M.bando(n, 6, area=True, lutas=1000, semente=n)
        confere(0.12 <= b["perda"] <= 0.35 and b["caiu"] <= 0.03 and 1.8 <= b["rodadas"] <= 4.5
                and a["rodadas"] <= 2.5,
                f"nível {n}: um bando de seis custa PV e tempo sem derrubar "
                f"({b['perda']:.0%} dos PV, {b['rodadas']:.1f} rodadas; com área {a['rodadas']:.1f})")
    for n in (3, 11, 19):
        so, com = M.aliado_no_duelo(n, lutas=200)
        confere(0.60 <= com <= 0.82 and com >= so + 0.08,
                f"nível {n}: o aliado de luta ajuda sem decidir ({so:.0%} → {com:.0%})")
    sem, com = M.aliado_no_grupo(15, 4, lutas=200)
    confere(sem - 0.03 <= com <= sem + 0.25,
            f"nível 15: o aliado não piora o grupo nem vence o Ouro por ele ({sem:.0%} → {com:.0%})")
    fichas = [
        ("cavaleiro-negro", 1, 1, 0.70, 1.00, "vence na maioria das vezes"),
        ("cavaleiro-de-prata", 8, 1, 0.00, 0.10, "quase nunca"),
        ("cavaleiro-de-prata", 9, 1, 0.05, 0.20, "uma vez em nove"),
        ("cavaleiro-de-prata", 13, 1, 0.75, 1.00, "vence com folga"),
        ("cavaleiro-de-prata", 9, 3, 0.75, 1.00, "é luta para três Bronzes"),
        ("guerreiro-deus", 12, 4, 0.00, 0.10, "três níveis abaixo, quase nunca"),
        ("guerreiro-deus", 15, 4, 0.50, 0.78, "duas vezes em três"),
        ("general-marina", 15, 4, 0.35, 0.65, "metade das vezes"),
        ("cavaleiro-de-ouro", 16, 1, 0.00, 0.02, "menos de uma vez em cem"),
        ("cavaleiro-de-ouro", 15, 4, 0.22, 0.45, "um terço das vezes"),
        ("cavaleiro-de-ouro", 15, 5, 0.45, 0.75, "cinco, pouco mais da metade"),
        ("juiz-do-inferno", 17, 4, 0.35, 0.60, "quase metade das vezes"),
        ("juiz-do-inferno", 18, 4, 0.52, 0.80, "de nível 18, duas vezes em três"),
    ]
    for i, (chave, n, k, lo, hi, texto) in enumerate(fichas):
        r = M.contra_ficha(chave, n, k, lutas=N if k == 1 else 200, semente=900 + i)
        confere(lo <= r["vence"] <= hi,
                f"{chave}: {k} Bronze(s) de nível {n} — {texto} ({r['vence']:.0%})")
    e2 = M.varios_contra_um("espectro-terrestre", 2, 3, lutas=200, semente=950)
    e3 = M.varios_contra_um("espectro-terrestre", 3, 4, lutas=200, semente=951)
    confere(0.15 <= e2 <= 0.40 and e3 <= 0.20,
            f"espectro-terrestre: dois são luta difícil para um nível 3 ({e2:.0%}), "
            f"três derrubam um nível 4 ({e3:.0%})")


# ---------------------------------------------------------------------------


def main() -> None:
    alvo = sys.argv[1] if len(sys.argv) > 1 else "tudo"
    if alvo in ("tudo", "motor"):
        testar_motor()
    if alvo in ("tudo", "livro"):
        testar_livro()
    if alvo in ("tudo", "equilibrio"):
        testar_equilibrio()
    if alvo in ("tudo", "extremos"):
        testar_extremos()
    if alvo in ("tudo", "mestre"):
        testar_mestre()
    print()
    if falhas:
        print(f"{len(falhas)} falha(s).")
        sys.exit(1)
    print("tudo certo.")


if __name__ == "__main__":
    main()
