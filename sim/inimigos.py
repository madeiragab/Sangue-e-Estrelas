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
        caracteristicas=("cortante",),
        exercito="Renegado", armadura="Armadura Negra, cópia de uma de Bronze",
        tecnicas=("Punho das Sombras", "Chama Negra", None),
        tracos=["<strong>Armadura falsa.</strong> A Armadura Negra não se regenera: a "
                "Resistência gasta fica gasta até alguém consertá-la."],
        quando="O primeiro inimigo nomeado de uma campanha. Um Bronze de nível 1 vence "
               "um desses sozinho na maioria das vezes."),
    "espectro-terrestre": dict(
        nome="Espectro de Estrela Terrestre", nivel=4, posto="bronze", acessorio="asas",
        caracteristicas=("leve",),
        conviccoes=0, exercito="Hades", armadura="Súplice",
        tecnicas=("Asa do Mundo Inferior", "Garra do Cão do Inferno", "Grito Maligno"),
        tracos=["<strong>Estrela Maligna.</strong> Se morrer, volta em "
                "<span class=\"dado\">1d4</span> semanas, enquanto Hades existir."],
        quando="Vem em grupos de dois ou três. Sozinho, perde quase sempre para um Bronze de "
               "nível 3; dois juntos já são uma luta difícil para ele (o Bronze vence uma vez "
               "em quatro), e três derrubam até um Bronze de nível 4."),
    "cavaleiro-de-prata": dict(
        nome="Cavaleiro de Prata", nivel=9, posto="prata", acessorio="correntes",
        caracteristicas=("ressonante", "ofuscante"),
        conviccoes=1, exercito="Atena", armadura="Armadura de Prata",
        tecnicas=("Correntes do Cão Infernal", "Laço de Aço", "Chicote de Cosmo"),
        tracos=["<strong>Correntes.</strong> Golpes comuns e Agarrar alcançam 6 metros.",
                "<strong>Uma Convicção.</strong> Ele levanta uma vez, e levanta desperto."],
        quando="O caçador que o Santuário manda atrás de quem desobedeceu. Um Bronze do "
               "mesmo nível vence uma vez em nove; um de nível 8, quase nunca; só um Bronze de "
               "nível 13 vence com folga. É luta para dois Bronzes juntos (vencem seis vezes em "
               "dez) ou para outro Prata; contra três, ele cai depressa."),
    "guerreiro-deus": dict(
        nome="Guerreiro Deus", nivel=15, posto="ouro", acessorio="nenhum", conviccoes=2,
        caracteristicas=("couraca", "ressonante", "estrelada"),
        exercito="Asgard", armadura="Veste Divina", teto_extra=1,
        tecnicas=("Presas do Lobo do Norte", "Ventania Gelada", "Tempestade de Cristal"),
        assento="Golpe da Estrela da Ursa Maior",
        tracos=["<strong>Safira de Odin.</strong> +1 no Teto de Cosmo enquanto a safira "
                "estiver na Veste (já somado).",
                "<strong>Sétimo dominado.</strong> Entra no Sétimo quando quer e, diante de um "
                "Sétimo recém-despertado, soma +2 no ataque e na DEF."],
        quando="Um dos sete. Quatro Bronzes do nível dele vencem duas vezes em três, e uns dois "
               "caem; três níveis abaixo, uma vez em sete. Sozinho, um personagem não vence."),
    "general-marina": dict(
        nome="General Marina", nivel=15, posto="ouro", acessorio="escudo", conviccoes=2,
        caracteristicas=("pesada", "espelhada", "couraca"),
        exercito="Poseidon", armadura="Escama", resistencia_extra=1,
        tecnicas=("Maré Devastadora", "Redemoinho", "Garra do Kraken"),
        assento="Triângulo das Ondas",
        tracos=["<strong>Escama de oricalco.</strong> +1 de Resistência (já somada).",
                "<strong>Sétimo dominado.</strong> Como todo guerreiro de elite."],
        quando="O guardião de um dos sete pilares. Luta melhor debaixo d'água que qualquer "
               "Cavaleiro. Quatro Bronzes do nível dele vencem duas vezes em três, e uns dois "
               "caem."),
    "cavaleiro-de-ouro": dict(
        nome="Cavaleiro de Ouro", nivel=16, posto="ouro", acessorio="nenhum", conviccoes=3,
        caracteristicas=("ressonante", "ofuscante", "pesada"),
        exercito="Atena", armadura="Armadura de Ouro",
        tecnicas=("Impacto do Zodíaco", "Chama Dourada", "Muralha de Luz"),
        assento="o Golpe do Assento da vaga",
        tracos=["<strong>Sétimo dominado.</strong> Entra no Sétimo no primeiro turno e, "
                "diante de um Sétimo recém-despertado, soma +2 no ataque e na DEF.",
                "<strong>Três Convicções.</strong> Derrubar um Ouro uma vez não basta."],
        quando="Uma das doze casas. Um Bronze sozinho vence um destes menos de uma vez em "
               "cem, mesmo no nível dele. Quatro Bronzes de nível 15 vencem metade das "
               "vezes, e uns três caem; cinco, três vezes em quatro."),
    "juiz-do-inferno": dict(
        nome="Juiz do Inferno", nivel=18, posto="ouro", acessorio="asas", conviccoes=3,
        caracteristicas=("leve", "cortante", "coracao"),
        exercito="Hades", armadura="Súplice", teto_extra=1,
        tecnicas=("Garras do Grifo", "Marionete Cósmica", "Grande Chifre do Wyvern"),
        assento="Golpe do Juízo",
        tracos=["<strong>Estrela Maligna.</strong> Volta em <span class=\"dado\">1d4</span> "
                "semanas enquanto Hades existir.",
                "<strong>Juiz.</strong> +1 no Teto de Cosmo (já somado).",
                "<strong>Sétimo dominado.</strong>"],
        quando="Um dos três juízes. Quatro Bronzes de nível 17 vencem metade das vezes, e "
               "uns três caem; de nível 18, duas vezes em três. É a luta de um arco inteiro."),
}


# ---------------------------------------------------------------------------
# Montar
# ---------------------------------------------------------------------------


def lutador(chave: str) -> Lutador:
    e = INIMIGOS[chave]
    x = montar(e["nome"], e["nivel"], e["posto"], acessorio=e["acessorio"],
               conviccoes=e["conviccoes"], caracteristicas=e["caracteristicas"])
    x.teto_fixo = e.get("teto_extra", 0)
    x.resistencia_extra = e.get("resistencia_extra", 0)
    x.reiniciar()
    return x


def _defesas(x: Lutador) -> tuple[int, int, int]:
    d_ = x.defesas_passivas()
    return d_["con"], d_["des"], d_["sab"]


def _caracteristicas(x: Lutador) -> str:
    return " · ".join(CARACTERISTICAS[c][0] for c in x.caracteristicas)


def _acessorio(x: Lutador) -> str:
    return {"nenhum": "sem acessório", "garras": "garras", "escudo": "escudo",
            "correntes": "correntes", "asas": "asas"}[x.acessorio]


def _golpe(x: Lutador) -> str:
    lados = 10 if x.acessorio == "garras" else 8
    atk = R.ataques_por_golpe(x.nivel)
    vezes = " (dois golpes)" if atk == 2 else ""
    return (f"+{x.bonus_ataque('golpe')} contra a DEF, "
            f"<span class=\"dado\">1d{lados} + {x.mods[x.atr_golpe]}</span>{vezes}")


def dano_texto(x: Lutador, t) -> str:
    """O dano de uma técnica como o livro escreve: 3d8 + 50 (cada ponto rola 1d8 +
    nível − 1, e o atributo soma uma vez)."""
    dados, fixo = R.dano_do_ponto(x.nivel, t.grau)
    p = t.pontos_de_dano
    mod = x.mods[x.atr_golpe if t.natureza == "golpe" else x.atr_cosmo]
    return f"{p * dados}d{t.lado} + {p * fixo + mod}"


def _tecnica(x: Lutador, t, nome: str) -> str:
    extra = " Atravessa a armadura." if t.atravessa else ""
    return (f"<strong>{html.escape(nome)}</strong> · {t.custo()} de Cosmo · "
            f"+{x.bonus_ataque(t.natureza)} contra a DEF · "
            f"<span class=\"dado\">{dano_texto(x, t)}</span>.{extra}")


def bloco(chave: str) -> str:
    e = INIMIGOS[chave]
    x = lutador(chave)
    x.reiniciar()
    fort, refl, vont = _defesas(x)
    teto = x.teto
    ini = (x.mods["des"] + (2 if "leve" in x.caracteristicas else 0)
           - (2 if "pesada" in x.caracteristicas else 0))
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
        f"<b>Cosmo</b> começa em {x.cosmo}, piso {x.piso}, Teto {teto} "
        f"<span class=\"sep\">·</span> "
        f"<b>Sentido</b> {sentido}<br>"
        f"<b>Armadura</b> {html.escape(e['armadura'])}, DEF +{x.armadura_def} · "
        f"<b>Resistência</b> {x.resistencia_max} · {_acessorio(x)}<br>"
        f"<b>Características</b> {_caracteristicas(x)}<br>"
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
    6: "Segunda Lição",
    9: "Ataque Extra",
    11: "Golpe Certeiro",
    14: "Quarta Convicção",
    18: "Segunda técnica assinatura",
    20: "Lenda",
}


def escolhas_do_nivel(n: int) -> str:
    """O que o jogador escolhe ao chegar neste nível."""
    if n == 1:
        return "—"
    partes = ["Vida ou Cosmo"]
    if n in R.NIVEIS_TECNICA_OU_ATRIBUTO:
        partes.append("técnica nova ou atributo")
    if n in R.NIVEIS_PERICIA_OU_DEFESA:
        partes.append("perícia ou defesa")
    return " · ".join(partes)


def tabela_niveis() -> str:
    """Duas tabelas: os números de cada nível, e o que se ganha, o que se escolhe e a
    Glória para sair dele. Seis colunas no máximo em cada, para caber no celular."""
    linhas = ['<div class="rolagem"><table class="compacta">',
              '<thead><tr><th class="num">Nível</th><th class="num">Prof.</th>'
              '<th class="num">Grau</th><th class="num">Teto</th><th class="num">PV</th>'
              '<th class="num">Ponto</th></tr></thead><tbody>']
    for n in range(1, 21):
        linhas.append(
            f'<tr><td class="num">{n}</td><td class="num">+{R.prof(n)}</td>'
            f'<td class="num">{R.grau(n)}</td><td class="num">{R.teto_base(n)}</td>'
            f'<td class="num">{R.pv_maximo(n, 0)}</td>'
            f'<td class="num">+{R.bonus_do_ponto(n)}</td></tr>')
    linhas += ["</tbody></table></div>", '<div class="rolagem"><table>',
               '<thead><tr><th class="num">Nível</th><th>O que você ganha</th>'
               '<th>O que você escolhe</th><th class="num">Glória</th></tr></thead><tbody>']
    for n in range(1, 21):
        gloria = "—" if n == 20 else str(R.gloria_para_subir(n))
        linhas.append(f'<tr><td class="num">{n}</td><td>{GANHOS.get(n, "—")}</td>'
                      f'<td>{escolhas_do_nivel(n)}</td><td class="num">{gloria}</td></tr>')
    linhas.append("</tbody></table></div>")
    return "\n".join(linhas)


def tabela_posto() -> str:
    nomes = {"bronze": "Bronze", "prata": "Prata", "ouro": "Ouro", "divina": "Forma Divina"}
    linhas = ['<div class="rolagem"><table>',
              '<thead><tr><th>Posto</th><th class="num">DEF</th><th class="num">Resistência</th>'
              '</tr></thead><tbody>']
    for p, (bonus, res) in R.POSTO.items():
        linhas.append(f'<tr><td>{nomes[p]}</td><td class="num">+{bonus}</td><td class="num">{res}</td></tr>')
    linhas.append("</tbody></table></div>")
    return "\n".join(linhas)


CARACTERISTICAS = {
    # chave no simulador: (nome, o que faz). A ordem é a da tabela do livro.
    "couraca": ("Couraça grossa", "Todo golpe comum que te acerta causa o seu Grau a menos de dano."),
    "espinhos": ("Espinhos", "Uma vez por turno, quem te acerta com um golpe comum sofre "
                 "1d4 + o seu Grau de dano."),
    "espelhada": ("Espelhada", "Uma vez por luta, quando você apara uma técnica, quem a usou "
                  "sofre 1d6 por Grau."),
    "pesada": ("Pesada", "+1 na DEF, −2 na Iniciativa e −3 metros de movimento."),
    "leve": ("Leve", "+2 na Iniciativa e +3 metros de movimento."),
    "ressonante": ("Ressonante", "Você começa toda luta com +1 de Cosmo."),
    "estrelada": ("Constelação viva", "Enquanto você estiver no Sétimo, +1 no acerto: a sua "
                  "constelação acende atrás de você."),
    "coracao": ("Coração de estrela", "Quando você levanta com uma Convicção, o seu próximo "
                "ataque tem Vantagem."),
    "cortante": ("Cortante", "Os seus golpes comuns não podem ser aparados."),
    "ofuscante": ("Ofuscante", "Uma vez por luta, a primeira técnica usada contra você rola com "
                  "Desvantagem: a armadura brilha na hora do golpe."),
    "elmo_fechado": ("Elmo fechado", "Enquanto o Elmo estiver no lugar, nenhuma técnica arranca a "
                     "sua visão ou a sua audição."),
}


def tabela_caracteristicas() -> str:
    linhas = ['<div class="rolagem"><table>',
              '<thead><tr><th>Característica</th><th>O que faz</th></tr></thead><tbody>']
    for nome, efeito in CARACTERISTICAS.values():
        efeito = html.escape(efeito).replace("1d4", '<span class="dado">1d4</span>') \
            .replace("1d6", '<span class="dado">1d6</span>').replace("1d8", '<span class="dado">1d8</span>')
        linhas.append(f"<tr><td>{nome}</td><td>{efeito}</td></tr>")
    linhas.append("</tbody></table></div>")
    return "\n".join(linhas)


ESCADA = {
    # sangue: (nome, de quem)
    "guerreiro": ("De guerreiro", "o dono ou um companheiro do mesmo exército"),
    "elite": ("De elite", "um Ouro, General, Juiz ou Guerreiro Deus"),
    "deus": ("De deus", "o deus patrono do exército"),
}


def descricao_forma(sangue: str) -> str:
    """O bônus de cada forma nova, em texto, tirado de sim/regras.py."""
    if sangue == "guerreiro":
        return ("<strong>+1 no acerto</strong> na 1ª, 3ª, 5ª… · "
                "<strong>+1 de Resistência</strong> na 2ª, 4ª, 6ª…")
    nomes = {"def": "DEF", "acerto": "no acerto", "res": "de Resistência"}
    return " e ".join(f"<strong>+{v} {nomes[k]}</strong>" for k, v in R.FORMA[sangue].items())


def tabela_formas() -> str:
    """A escada do sangue em duas tabelas: quantas vezes revive e o bônus de cada
    forma nova (de sim/regras.py)."""
    linhas = ['<div class="rolagem"><table>',
              '<thead><tr><th>Quantas vezes revive</th><th class="num">Bronze</th>'
              '<th class="num">Prata</th><th class="num">Elite</th></tr></thead><tbody>']
    for s in R.FORMA:
        vezes = "".join(f'<td class="num">{R.REVIVIDAS_MAX[s][p] or "—"}</td>'
                        for p in ("bronze", "prata", "ouro"))
        linhas.append(f'<tr><td>Sangue {ESCADA[s][0].lower()}</td>{vezes}</tr>')
    linhas += ["</tbody></table></div>", '<div class="rolagem"><table>',
               '<thead><tr><th>Sangue</th><th>Cada forma nova dá</th></tr></thead><tbody>']
    for s in R.FORMA:
        nome, quem = ESCADA[s]
        linhas.append(f'<tr><td><strong>{nome}</strong>: {quem}</td>'
                      f'<td>{descricao_forma(s)}</td></tr>')
    linhas.append("</tbody></table></div>")
    return "\n".join(linhas)


def tabela_rapida() -> str:
    """Um inimigo nomeado genérico de cada nível, pelo mesmo construtor, sem
    características (o Mestre soma as que escolher). Em duas tabelas, para caber no
    celular: o que ele aguenta e o que ele bate."""
    defesa = ['<div class="rolagem"><table class="compacta">',
              '<thead><tr><th class="num">Nív.</th><th class="num">PV</th>'
              '<th class="num">DEF B/P/E</th><th class="num">Cosmo</th>'
              '<th class="num">Defesas</th></tr></thead><tbody>']
    ataque = ['<div class="rolagem"><table class="compacta">',
              '<thead><tr><th class="num">Nív.</th><th class="num">Atq.</th>'
              '<th>Golpe</th><th>Técnica (custo)</th></tr></thead><tbody>']
    for n in range(1, 21):
        b, p, o = (montar("x", n, posto, caracteristicas=()) for posto in ("bronze", "prata", "ouro"))
        for z in (b, p, o):
            z.reiniciar()
        grande = next(t for t in b.tecnicas if t.nome == "grande")
        mod = b.mods["des"]
        fort, refl, vont = _defesas(b)
        golpes = "2×" if R.ataques_por_golpe(n) == 2 else ""
        # o traço é um Posto que ainda não existe nesse nível
        def_p = p.defesa if R.posto_existe("prata", n) else "—"
        def_o = o.defesa if R.posto_existe("ouro", n) else "—"
        defesa.append(
            f'<tr><td class="num">{n}</td><td class="num">{b.pv_max}</td>'
            f'<td class="num">{b.defesa}/{def_p}/{def_o}</td>'
            f'<td class="num">{b.cosmo}/{b.piso}/{b.teto}</td>'
            f'<td class="num">{min(fort, refl, vont)}/{max(fort, refl, vont)}</td></tr>')
        ataque.append(
            f'<tr><td class="num">{n}</td><td class="num">+{b.bonus_ataque("golpe")}</td>'
            f'<td>{golpes}1d8+{mod}</td>'
            f'<td>{dano_texto(b, grande)} ({grande.custo()})</td></tr>')
    defesa.append("</tbody></table></div>")
    ataque.append("</tbody></table></div>")
    return "\n".join(defesa + ataque)


def tabela_figurantes() -> str:
    """O bando de cada nível (sim/regras.py: figurante)."""
    linhas = ['<div class="rolagem"><table class="compacta">',
              '<thead><tr><th class="num">Nível</th><th class="num">DEF</th>'
              '<th class="num">Ataque</th><th class="num">Dano</th>'
              '</tr></thead><tbody>']
    for n in range(1, 21):
        de, atk, dano = R.figurante(n)
        linhas.append(f'<tr><td class="num">{n}</td><td class="num">{de}</td>'
                      f'<td class="num">+{atk}</td><td class="num">{dano}</td></tr>')
    linhas.append("</tbody></table></div>")
    return "\n".join(linhas)
