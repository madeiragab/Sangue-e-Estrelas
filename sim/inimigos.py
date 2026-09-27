"""Os inimigos prontos do livro, montados com as mesmas regras dos personagens.

O build.py chama este arquivo para escrever as fichas e as tabelas do livro. Ou
seja: o número impresso é o mesmo que o simulador usa nos duelos, e o test.py
mede esses mesmos lutadores.
"""

from __future__ import annotations

import html

import regras as R
from luta import Lutador, montar

# ---------------------------------------------------------------------------
# Os inimigos prontos
# ---------------------------------------------------------------------------

INIMIGOS = {
    "cavaleiro-negro": dict(
        nome="Cavaleiro Negro", nivel=2, posto="bronze", acessorio="garras", conviccoes=0,
        exercito="Renegado", armadura="Armadura Negra, cópia de uma de Bronze",
        tecnicas=("Punho das Sombras", "Chama Negra", None),
        tracos=["<strong>Armadura falsa.</strong> A Armadura Negra não se regenera: as "
                "caixas marcadas ficam marcadas até alguém consertá-la."],
        quando="O primeiro inimigo nomeado de uma campanha. Um Bronze de nível 1 vence "
               "um desses sozinho na maioria das vezes."),
    "espectro-terrestre": dict(
        nome="Espectro de Estrela Terrestre", nivel=4, posto="bronze", acessorio="asas",
        conviccoes=0, exercito="Hades", armadura="Súplice",
        tecnicas=("Asa do Mundo Inferior", "Garra do Cão do Inferno", "Grito Maligno"),
        tracos=["<strong>Estrela Maligna.</strong> Se morrer, volta em "
                "<span class=\"dado\">1d4</span> semanas, enquanto Hades existir."],
        quando="Vem em grupos de dois ou três. Um só é uma luta difícil para um Bronze de "
               "nível 3."),
    "cavaleiro-de-prata": dict(
        nome="Cavaleiro de Prata", nivel=6, posto="prata", acessorio="correntes",
        conviccoes=1, exercito="Atena", armadura="Armadura de Prata",
        tecnicas=("Correntes do Cão Infernal", "Laço de Aço", "Chicote de Cosmo"),
        tracos=["<strong>Correntes.</strong> Golpes comuns e Agarrar alcançam 6 metros.",
                "<strong>Uma Convicção.</strong> Ele levanta uma vez, e levanta desperto."],
        quando="O caçador que o Santuário manda atrás de quem desobedeceu. Um grupo de três "
               "Bronzes de nível 5 dá conta; um só, raramente."),
    "guerreiro-deus": dict(
        nome="Guerreiro Deus", nivel=15, posto="ouro", acessorio="nenhum", conviccoes=2,
        exercito="Asgard", armadura="Veste Divina", teto_extra=1,
        tecnicas=("Presas do Lobo do Norte", "Ventania Gelada", "Tempestade de Cristal"),
        assento="Golpe da Estrela da Ursa Maior",
        tracos=["<strong>Safira de Odin.</strong> +1 no Teto de Cosmo enquanto a safira "
                "estiver na Veste (já somado).",
                "<strong>Sétimo dominado.</strong> Entra no Sétimo quando quer e, diante de um "
                "Sétimo recém-despertado, soma +2 no ataque e na DEF."],
        quando="Um dos sete. É luta para um grupo inteiro de nível 12 ou mais, com Centelhas; "
               "um personagem sozinho, mesmo do nível dele, perde quase sempre."),
    "general-marina": dict(
        nome="General Marina", nivel=15, posto="ouro", acessorio="escudo", conviccoes=2,
        exercito="Poseidon", armadura="Escama", caixa_extra=1,
        tecnicas=("Maré Devastadora", "Redemoinho", "Garra do Kraken"),
        assento="Triângulo das Ondas",
        tracos=["<strong>Escama de oricalco.</strong> Uma caixa a mais em cada peça (já "
                "somada).",
                "<strong>Sétimo dominado.</strong> Como todo guerreiro de elite."],
        quando="O guardião de um dos sete pilares. Luta melhor debaixo d'água que qualquer "
               "Cavaleiro."),
    "cavaleiro-de-ouro": dict(
        nome="Cavaleiro de Ouro", nivel=16, posto="ouro", acessorio="nenhum", conviccoes=3,
        exercito="Atena", armadura="Armadura de Ouro",
        tecnicas=("Impacto do Zodíaco", "Chama Dourada", "Muralha de Luz"),
        assento="o Golpe do Assento da vaga",
        tracos=["<strong>Sétimo dominado.</strong> Entra no Sétimo no primeiro turno e, "
                "diante de um Sétimo recém-despertado, soma +2 no ataque e na DEF.",
                "<strong>Três Convicções.</strong> Derrubar um Ouro uma vez não basta."],
        quando="Uma das doze casas. Um Bronze sozinho vence um destes menos de uma vez em "
               "vinte, mesmo no nível dele; com o grupo mandando Centelhas, um pouco mais."),
    "juiz-do-inferno": dict(
        nome="Juiz do Inferno", nivel=18, posto="ouro", acessorio="asas", conviccoes=3,
        exercito="Hades", armadura="Súplice", teto_extra=1,
        tecnicas=("Garras do Grifo", "Marionete Cósmica", "Grande Chifre do Wyvern"),
        assento="Golpe do Juízo",
        tracos=["<strong>Estrela Maligna.</strong> Volta em <span class=\"dado\">1d4</span> "
                "semanas enquanto Hades existir.",
                "<strong>Juiz.</strong> +1 no Teto de Cosmo (já somado).",
                "<strong>Sétimo dominado.</strong>"],
        quando="Um dos três juízes. É a luta de um arco inteiro."),
}


# ---------------------------------------------------------------------------
# Montar
# ---------------------------------------------------------------------------


def lutador(chave: str) -> Lutador:
    e = INIMIGOS[chave]
    x = montar(e["nome"], e["nivel"], e["posto"], acessorio=e["acessorio"],
               conviccoes=e["conviccoes"])
    x.teto_fixo = e.get("teto_extra", 0)
    x.caixa_extra = e.get("caixa_extra", 0)
    x.reiniciar()
    return x


def _defesas(x: Lutador) -> tuple[int, int, int]:
    treinadas = {"des", "sab"} | ({"con"} if x.nivel >= 10 else set())
    def d_(atr):
        return 14 + x.mods[atr] + (x.prof if atr in treinadas else 0)
    return d_("con"), d_("des"), d_("sab")


def _caixas(x: Lutador, extra: int) -> str:
    x.reiniciar()
    partes = []
    nomes = {"elmo": "Elmo", "peitoral": "Peitoral", "bracos": "Braços", "pernas": "Pernas",
             "acessorio": "acessório"}
    for p in ("elmo", "peitoral", "bracos", "pernas", "acessorio"):
        if p == "acessorio" and x.acessorio == "nenhum":
            continue
        partes.append(f"{nomes[p]} {x.caixas[p]}")
    return " · ".join(partes)


def _golpe(x: Lutador) -> str:
    lados = 10 if x.acessorio == "garras" else 8
    atk = R.ataques_por_golpe(x.nivel)
    vezes = " (dois golpes)" if atk == 2 else ""
    return (f"+{x.bonus_ataque('golpe')} contra a DEF, "
            f"<span class=\"dado\">1d{lados} + {x.mods[x.atr_golpe]}</span>{vezes}")


def _tecnica(x: Lutador, t, nome: str) -> str:
    mod = x.mods[x.atr_golpe]
    extra = " Atravessa a armadura." if t.atravessa else ""
    return (f"<strong>{html.escape(nome)}</strong> · {t.custo()} de Cosmo · "
            f"+{x.bonus_ataque('golpe')} contra a DEF · "
            f"<span class=\"dado\">{t.dados_de_dano}d{t.lado} + {mod}</span>.{extra}")


def bloco(chave: str) -> str:
    e = INIMIGOS[chave]
    x = lutador(chave)
    x.reiniciar()
    fort, refl, vont = _defesas(x)
    teto = x.teto
    ini = x.mods["des"]
    sentido = "Sétimo quando quiser" if x.posto == "ouro" else "Sexto; desperta como um personagem"
    nomes_tec = list(e["tecnicas"])
    tecs = {t.nome: t for t in x.tecnicas}
    itens = []
    if x.posto == "ouro" and "assento" in tecs:
        itens.append(_tecnica(x, tecs["assento"], e.get("assento", "Golpe do Assento")))
    itens.append(_tecnica(x, tecs["grande"], nomes_tec[0]))
    if "media" in tecs and nomes_tec[2]:
        itens.append(_tecnica(x, tecs["media"], nomes_tec[2]))
    itens.append(_tecnica(x, tecs["pequena"], nomes_tec[1]))
    status = (
        f"<b>PV</b> {x.pv_max} <span class=\"sep\">·</span> <b>DEF</b> {x.defesa} "
        f"<span class=\"sep\">·</span> <b>Iniciativa</b> +{ini}<br>"
        f"<b>Fortitude</b> {fort} <span class=\"sep\">·</span> <b>Reflexos</b> {refl} "
        f"<span class=\"sep\">·</span> <b>Vontade</b> {vont}<br>"
        f"<b>Cosmo</b> começa em {x.cosmo}, Teto {teto} <span class=\"sep\">·</span> "
        f"<b>Sentido</b> {sentido}<br>"
        f"<b>Armadura</b> {html.escape(e['armadura'])}, DEF +{R.POSTO[x.posto][0]} · "
        f"{_caixas(x, e.get('caixa_extra', 0))}<br>"
        f"<b>Convicções</b> {e['conviccoes']}"
    )
    posto_nome = {"bronze": "Bronze", "prata": "Prata", "ouro": "Elite"}[x.posto]
    partes = [
        '<div class="criatura">',
        f'<h3>{html.escape(e["nome"])}<span class="kleos">Nível {x.nivel} · {posto_nome}</span></h3>',
        f'<p class="tipo">{html.escape(e["exercito"])}</p>',
        f'<div class="status">{status}</div>',
        '<p class="rotulo-bloco">Golpe comum</p>',
        f'<p>{_golpe(x)}. Acertou: +1 de Cosmo.</p>',
        '<p class="rotulo-bloco">Técnicas</p>',
        "<ul>" + "".join(f"<li>{i}</li>" for i in itens) + "</ul>",
        '<p class="rotulo-bloco">Traços</p>',
        "<ul>" + "".join(f"<li>{t}</li>" for t in e["tracos"]) + "</ul>",
        f'<p class="morte"><span class="rotulo-bloco">Quando usar</span>{e["quando"]}</p>',
        "</div>",
    ]
    return "\n".join(partes)


# ---------------------------------------------------------------------------
# Tabelas geradas para o livro
# ---------------------------------------------------------------------------

GANHOS = {
    1: "Tudo da criação · duas técnicas · técnica assinatura",
    2: "Leitura de Combate",
    3: "Cosmo Desperto",
    4: "Terceira técnica · +2 pontos de atributo",
    5: "+1 caixa numa peça da armadura",
    6: "Segunda Lição",
    7: "+1 caixa numa peça da armadura",
    8: "Quarta técnica · +2 pontos de atributo",
    9: "Ataque Extra",
    10: "Terceira defesa treinada",
    11: "Golpe Certeiro",
    12: "Quinta técnica · +2 pontos de atributo",
    13: "+1 caixa numa peça da armadura",
    14: "Quarta Convicção",
    15: "Cosmo Sereno",
    16: "Sexta técnica · +2 pontos de atributo",
    17: "+1 caixa numa peça da armadura",
    18: "Segunda técnica assinatura",
    19: "+2 pontos de atributo",
    20: "Sétima técnica · Lenda",
}


def tabela_niveis() -> str:
    linhas = ['<div class="rolagem"><table>',
              '<thead><tr><th class="num">Nível</th><th class="num">Prof.</th>'
              '<th class="num">Grau</th><th class="num">Teto</th><th class="num">PV</th>'
              '<th class="num">Glória</th><th>O que você ganha</th></tr></thead><tbody>']
    for n in range(1, 21):
        gloria = "—" if n == 20 else str(R.gloria_para_subir(n))
        linhas.append(
            f'<tr><td class="num">{n}</td><td class="num">+{R.prof(n)}</td>'
            f'<td class="num">{R.grau(n)}</td><td class="num">{R.teto_base(n)}</td>'
            f'<td class="num">{R.pv_maximo(n, 0)}</td><td class="num">{gloria}</td>'
            f'<td>{GANHOS[n]}</td></tr>')
    linhas.append("</tbody></table></div>")
    return "\n".join(linhas)


def tabela_posto() -> str:
    nomes = {"bronze": "Bronze", "prata": "Prata", "ouro": "Ouro", "divina": "Forma Divina"}
    linhas = ['<div class="rolagem"><table>',
              '<thead><tr><th>Posto</th><th class="num">DEF</th><th class="num">Caixas por peça</th>'
              '</tr></thead><tbody>']
    for p, (bonus, caixas) in R.POSTO.items():
        linhas.append(f'<tr><td>{nomes[p]}</td><td class="num">+{bonus}</td><td class="num">{caixas}</td></tr>')
    linhas.append("</tbody></table></div>")
    return "\n".join(linhas)


def tabela_rapida() -> str:
    """Um inimigo nomeado genérico de cada nível, pelo mesmo construtor."""
    linhas = ['<div class="rolagem"><table class="compacta">',
              '<thead><tr><th class="num">Nív.</th><th class="num">PV</th>'
              '<th class="num">DEF B/P/E</th><th class="num">Atq.</th>'
              '<th>Golpe</th><th>Técnica (custo)</th>'
              '<th class="num">Defesas</th></tr></thead><tbody>']
    for n in (1, 2, 3, 4, 5, 6, 8, 10, 12, 14, 16, 18, 20):
        b, p, o = (montar("x", n, posto) for posto in ("bronze", "prata", "ouro"))
        for z in (b, p, o):
            z.reiniciar()
        grande = next(t for t in b.tecnicas if t.nome == "grande")
        mod = b.mods["des"]
        fort, refl, vont = _defesas(b)
        golpes = "2×" if R.ataques_por_golpe(n) == 2 else ""
        linhas.append(
            f'<tr><td class="num">{n}</td><td class="num">{b.pv_max}</td>'
            f'<td class="num">{b.defesa}/{p.defesa}/{o.defesa}</td>'
            f'<td class="num">+{b.bonus_ataque("golpe")}</td>'
            f'<td>{golpes}1d8+{mod}</td>'
            f'<td>{grande.dados_de_dano}d8+{mod} ({grande.custo()})</td>'
            f'<td class="num">{min(fort, refl, vont)}/{max(fort, refl, vont)}</td></tr>')
    linhas.append("</tbody></table></div>")
    return "\n".join(linhas)
