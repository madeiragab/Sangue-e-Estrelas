"""Toda a conferência do sistema, sem dependências externas.

    python test.py            tudo (leva uns dois minutos)
    python test.py motor      só as contas das técnicas
    python test.py livro      só o build e a coerência do livro
    python test.py equilibrio só as metas de equilíbrio

Três blocos:

  motor       as técnicas impressas no livro têm o tamanho e o custo que o
              motor do Capítulo Seis calcula;
  livro       o build roda, todo link interno tem destino, e as tabelas
              geradas a partir de sim/regras.py estão no livro;
  equilibrio  as metas de equilíbrio, medidas em duelos com semente fixa.

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
    for posto, (bonus, caixas) in R.POSTO.items():
        nome = {"bronze": "Bronze", "prata": "Prata", "ouro": "Ouro", "divina": "Forma Divina"}[posto]
        linha = f'<tr><td>{nome}</td><td class="num">+{bonus}</td><td class="num">{caixas}</td></tr>'
        confere(linha in html, f"tabela de Posto: {nome} +{bonus} DEF, {caixas} caixas")
    for n in (1, 5, 9, 13, 17, 20):
        trecho = f'<td class="num">{n}</td><td class="num">+{R.prof(n)}</td><td class="num">{R.grau(n)}</td><td class="num">{R.teto_base(n)}</td>'
        confere(trecho in html, f"tabela de níveis: nível {n}")
    confere(f"nível {R.NIVEL_ATAQUE_EXTRA}" in html.lower() or f"nível {R.NIVEL_ATAQUE_EXTRA}" in html,
            f"o Ataque Extra está no nível {R.NIVEL_ATAQUE_EXTRA}")


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


def testar_equilibrio() -> None:
    print(f"equilíbrio ({N} duelos por linha):")
    for n in (1, 5, 9, 13, 17):
        r = taxa(lambda k: montar("A", k), lambda k: montar("B", k), n, 11 + n)
        confere(0.40 <= r["a"] <= 0.60, f"nível {n}: espelho Bronze×Bronze perto de 50% ({r['a']:.0%})")
        s = taxa(lambda k: montar("A", k, conviccoes=0), lambda k: montar("B", k, conviccoes=0), n, 21 + n)
        confere(3.0 <= s["rodadas_media"] <= 8.5,
                f"nível {n}: luta sem Convicções dura 3 a 8,5 rodadas ({s['rodadas_media']:.1f})")
        confere(4.5 <= r["rodadas_media"] <= 11.0,
                f"nível {n}: luta com Convicções dura 4,5 a 11 rodadas ({r['rodadas_media']:.1f})")
        t = taxa(lambda k: montar("A", k, politica={"tecnicas": False}), lambda k: montar("B", k), n, 31 + n)
        confere(t["a"] <= 0.40, f"nível {n}: técnica vale mais que só golpe comum ({t['a']:.0%} sem técnica)")
        ap = taxa(lambda k: montar("A", k, politica={"aparar": False}), lambda k: montar("B", k), n, 41 + n)
        confere(ap["a"] <= 0.50, f"nível {n}: apanhar sem aparar não compensa ({ap['a']:.0%})")
        q = taxa(lambda k: montar("A", k, politica={"queimar": False}), lambda k: montar("B", k), n, 51 + n)
        confere(0.30 <= q["a"] <= 0.60, f"nível {n}: queimar ajuda sem dominar ({q['a']:.0%} de quem nunca queima)")
        p = taxa(lambda k: montar("A", k, "prata"), lambda k: montar("B", k), n, 61 + n)
        confere(0.52 <= p["a"] <= 0.72, f"nível {n}: Prata vence Bronze na maioria ({p['a']:.0%})")
        o = taxa(lambda k: montar("A", k), lambda k: montar("B", k, "ouro"), n, 71 + n)
        confere(o["a"] <= 0.07, f"nível {n}: Bronze sozinho quase nunca vence um Ouro ({o['a']:.0%})")
        oc = taxa(lambda k: montar("A", k), lambda k: montar("B", k, "ouro"), n, 81 + n, centelhas_a=1)
        confere(o["a"] - 0.02 <= oc["a"] <= 0.18,
                f"nível {n}: Centelhas dão ao Bronze uma chance pequena ({o['a']:.0%} → {oc['a']:.0%})")
        po = taxa(lambda k: montar("A", k, "prata"), lambda k: montar("B", k, "ouro"), n, 86 + n)
        confere(po["a"] <= 0.12, f"nível {n}: Prata sozinho quase nunca vence um Ouro ({po['a']:.0%})")
        lev = vitorias_levantando(n, 88 + n)
        confere(lev >= 0.70, f"nível {n}: quando o Bronze vence o Ouro, quase sempre levantou do chão ({lev:.0%})")
        mil = taxa(lambda k: montar("A", k, "ouro"), lambda k: montar("B", k, "ouro"), n, 91 + n)
        confere(0.03 <= mil["mil_dias"] <= 0.30,
                f"nível {n}: Guerra dos Mil Dias é rara mas acontece entre Ouros ({mil['mil_dias']:.0%})")


# ---------------------------------------------------------------------------


def main() -> None:
    alvo = sys.argv[1] if len(sys.argv) > 1 else "tudo"
    if alvo in ("tudo", "motor"):
        testar_motor()
    if alvo in ("tudo", "livro"):
        testar_livro()
    if alvo in ("tudo", "equilibrio"):
        testar_equilibrio()
    print()
    if falhas:
        print(f"{len(falhas)} falha(s).")
        sys.exit(1)
    print("tudo certo.")


if __name__ == "__main__":
    main()
