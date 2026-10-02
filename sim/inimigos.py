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

# O mesmo número da regra (R.DOMINIO_OURO), nos ataques e nas Rolagens de Efeito.
SETIMO_DOMINADO = (f"<strong>Sétimo dominado.</strong> Entra no Sétimo quando quer. Diante de "
                   f"um Sétimo recém-despertado, soma +{R.DOMINIO_OURO} nos ataques e nas "
                   f"Rolagens de Efeito, e o outro soma −{R.DOMINIO_OURO} nos dele.")

INIMIGOS = {
    "cavaleiro-negro": dict(
        nome="Cavaleiro Negro", nivel=2, posto="bronze", acessorio="garras", conviccoes=0,
        caracteristicas=("cortante",),
        exercito="Renegado", armadura="Armadura Negra, cópia de uma de Bronze",
        tecnicas=("Punho das Sombras", "Chama Negra", None),
        tracos=["<strong>Armadura falsa.</strong> A Armadura Negra não se regenera: a "
                "Resistência gasta fica gasta até alguém consertá-la."],
        quando="O primeiro inimigo nomeado de uma campanha. Um Bronze de nível 1 vence "
               "um desses sozinho pouco mais da metade das vezes: no começo, levantar "
               "ainda não dá o Sétimo."),
    "espectro-novato": dict(
        nome="Espectro Novato", nivel=3, posto="bronze", acessorio="garras", conviccoes=0,
        caracteristicas=("leve",), exercito="Hades", armadura="Súplice",
        tecnicas=("Garra do Estige", "Lamento do Aqueronte", None),
        tracos=["<strong>Estrela Maligna.</strong> Se morrer, volta em "
                "<span class=\"dado\">1d4</span> semanas, enquanto Hades existir."],
        quando="O primeiro Espectro de uma campanha contra Hades: a Súplice acabou de "
               "escolhê-lo. Um Bronze de nível 1 vence um destes sozinho quase metade das "
               "vezes; dois Bronzes de nível 1 vencem quase sempre, e um deles cai uma luta "
               "em três. Dois Novatos juntos ainda derrubam um Bronze sozinho de nível 4 duas "
               "vezes em três."),
    "espectro-terrestre": dict(
        nome="Espectro de Estrela Terrestre", nivel=4, posto="bronze", acessorio="asas",
        caracteristicas=("leve",),
        conviccoes=0, exercito="Hades", armadura="Súplice",
        tecnicas=("Asa do Mundo Inferior", "Garra do Cão do Inferno", "Grito Maligno"),
        tracos=["<strong>Estrela Maligna.</strong> Se morrer, volta em "
                "<span class=\"dado\">1d4</span> semanas, enquanto Hades existir."],
        quando="Vem em grupos de dois ou três. Sozinho, perde duas vezes em três para um "
               "Bronze de nível 3. Dois juntos derrubam quase sempre um Bronze de nível 3 ou 4; "
               "três ainda derrubam um de nível 5 quatro vezes em cinco. Para um Bronze "
               "sozinho antes do Sétimo, dois já são demais: é luta para o grupo."),
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
    "estrela-celeste": dict(
        nome="Espectro de Estrela Celeste", nivel=11, posto="prata", acessorio="asas",
        caracteristicas=("couraca", "leve"),
        conviccoes=1, exercito="Hades", armadura="Súplice",
        tecnicas=("Voo do Abismo", "Pena Negra", "Eclipse do Tártaro"),
        tracos=["<strong>Estrela Maligna.</strong> Volta em <span class=\"dado\">1d4</span> "
                "semanas enquanto Hades existir.",
                "<strong>Uma Convicção.</strong> Ele levanta uma vez, e levanta desperto."],
        quando="Um dos 36 de Hades, acima das Estrelas Terrestres: o Prata do exército. "
               "Um Bronze do mesmo nível vence um destes uma vez em sete, e só um de nível 13 "
               "vence mais da metade das vezes. Dois Bronzes de nível 11 vencem sete vezes em "
               "dez, e um deles cai; três de nível 9 também vencem sete em dez, mas quase dois "
               "caem. É a luta da sessão para um grupo pequeno."),
    "comandante-de-hades": dict(
        nome="Comandante sem armadura", nivel=9, posto="bronze", acessorio="nenhum",
        caracteristicas=(), conviccoes=1, sem_armadura=True, desperta=False,
        posto_nome="Sem Posto", exercito="Hades — a voz do deus na terra",
        armadura="nenhuma", tecnicas=("Lança do Mundo Inferior", "Sombra que Prende",
                                       "Ordem de Hades"),
        tracos=["<strong>Sem armadura.</strong> O poder dela vem do deus e de uma relíquia, "
                "não do metal: não apara, não bloqueia e não tem Elmo.",
                "<strong>Recua em vez de cair</strong> (<a href=\"#cap11\">Capítulo Onze</a>). "
                "A 0 PV, ela some numa fenda negra; a luta conta como vencida.",
                "<strong>Uma Convicção, e nenhum Sétimo.</strong> Ela levanta, mas não "
                "desperta: o Cosmo dela é emprestado.",
                "<strong>Nunca vem sozinha.</strong> Chega com um bando ou um Espectro "
                "nomeado — é a autoridade dela, não o punho, que pesa."],
        quando="Quem manda num exército sem lutar nele: a sacerdotisa, a voz do deus, o "
               "comandante que nunca vestiu armadura. Perigoso pela autoridade e pela fuga, "
               "não pelo punho. Um Bronze de nível 5 vence uma luta com ele uma vez em três; "
               "de nível 7, seis em dez; do nível dele, quase nove em dez. Três Bronzes de "
               "nível 5 vencem quase sempre, e um deles costuma cair. O nível é um ponto de "
               "partida: o seu comandante pode ser bem mais forte, ou mais fraco — monte-o "
               "pela tabela rápida no nível que a sua história pedir."),
    "satelite-de-artemis": dict(
        nome="Satélite de Ártemis", nivel=6, posto="bronze", acessorio="asas", conviccoes=1,
        caracteristicas=("leve",), exercito="Ártemis", armadura="Veste sagrada",
        tecnicas=("Flecha de Prata da Lua", "Luz Pálida", "Arco da Caçadora"),
        tracos=["<strong>A luz da lua.</strong> Sob a lua, +1 no Teto de Cosmo (não somado "
                "aqui).",
                "<strong>Uma Convicção.</strong> Levanta uma vez, pela deusa."],
        quando="A caçadora da lua, quase sempre em par. Um Bronze do mesmo nível "
               "vence metade das vezes; um de nível 5, uma vez em quatro. Dois Bronzes de "
               "nível 5 vencem quase oito em dez; de nível 6, quase sempre."),
    "palasita": dict(
        nome="Palasita de Terceira Classe", nivel=7, posto="bronze", acessorio="garras",
        conviccoes=1, caracteristicas=("cortante",), exercito="Palas", armadura="Cronotector",
        tecnicas=("Corte da Grande Espada", "Golpe do Punho", "Lâmina do Instante"),
        tracos=["<strong>A Grande Espada.</strong> O acessório é a espada (conta como "
                "garras): quem a perde, perde o corte.",
                "<strong>Uma Convicção.</strong> Pela irmã de Atena, que ele ama."],
        quando="O soldado da espada, que chega em grupo. Um Bronze do mesmo nível "
               "vence metade das vezes; um de nível 6, uma em três. Dois Bronzes de nível 6 "
               "vencem quase sempre."),
    "marciano": dict(
        nome="Marciano", nivel=10, posto="prata", acessorio="escudo", conviccoes=1,
        caracteristicas=("pesada", "espinhos"), exercito="Marte", armadura="Veste de Marte",
        tecnicas=("Lança da Guerra", "Grito de Batalha", "Marcha Vermelha"),
        tracos=["<strong>Fúria da guerra.</strong> Quando um aliado cai perto dele, +1 de "
                "Cosmo, uma vez por turno.",
                "<strong>Não há paz.</strong> Ele nunca dá Glória a quem o convence: com ele, "
                "só a luta resolve."],
        quando="O soldado de elite de um deus que só conhece a guerra. Um Bronze do "
               "mesmo nível vence pouco mais de uma vez em dez; um de nível 12, quatro em "
               "dez. Três Bronzes de nível 9 vencem sete em dez, e um ou dois caem."),
    "cavaleiro-da-coroa": dict(
        nome="Cavaleiro da Coroa", nivel=13, posto="prata", acessorio="nenhum", conviccoes=1,
        caracteristicas=("ofuscante", "estrelada"), exercito="Apolo",
        armadura="Armadura da Coroa",
        tecnicas=("Raio da Coroa", "Calor do Meio-Dia", "Disco Solar"),
        tracos=["<strong>Ainda sem a coroa.</strong> A coroa do sol é dos três da elite "
                "(<a href=\"#outros-exercitos\">Capítulo Nove</a>); este ainda luta no "
                "Sexto e desperta como um rival.",
                "<strong>Uma Convicção.</strong> Pelo deus do sol — ou, às vezes, uma que ele "
                "esconde."],
        quando="O cavaleiro do sol, antes da coroa. Um Bronze do mesmo nível vence uma "
               "vez em dez; um de nível 15, duas em três. Três Bronzes de nível 12 vencem oito "
               "em dez."),
    "anjo-caido": dict(
        nome="Anjo Caído", nivel=14, posto="prata", acessorio="asas", conviccoes=2,
        caracteristicas=("couraca", "coracao"), exercito="Lúcifer", armadura="Glória",
        tecnicas=("Queda do Céu", "Pena de Cinza", "Juízo da Asa Negra"),
        tracos=["<strong>Asas da queda.</strong> Toda Glória tem asas.",
                "<strong>Orgulho.</strong> Nunca se rende, nunca recua.",
                "<strong>Duas Convicções.</strong> Levanta, e levanta de novo."],
        quando="O anjo que caiu com o mestre dele, e não se arrepende. Um Bronze do "
               "mesmo nível vence uma vez em nove. Três de nível 13 vencem oito em dez, e um "
               "ou dois caem."),
    "cavaleiro-fantasma": dict(
        nome="Cavaleiro Fantasma", nivel=16, posto="ouro", acessorio="nenhum", conviccoes=0,
        caracteristicas=("ressonante", "pesada", "espelhada"), exercito="Éris",
        armadura="Veste fantasma, a sombra de uma armadura de Ouro",
        tecnicas=("Golpe do Rancor", "Mão Fria", "Lamento de Ouro"),
        assento="o Golpe do Assento que ele tinha em vida",
        tracos=["<strong>Trazido pela força.</strong> Era um Ouro; Éris o arrancou da morte. "
                "Sem Convicção: não levanta e não usa Sozinho contra muitos. A 0 PV, vira "
                "cinza (<a href=\"#corrompidos\">Capítulo Nove</a>).",
                SETIMO_DOMINADO],
        quando="Era um Ouro, e luta como um: um Bronze sozinho quase nunca vence. Mas "
               "sem Convicção ele não responde a um grupo nem levanta, e três Bronzes de nível "
               "15 o derrubam quase sempre. É o Ouro da sessão em que o grupo ainda não está "
               "pronto para um de verdade."),
    "tita": dict(
        nome="Titã meio desperto", nivel=18, posto="ouro", acessorio="nenhum", conviccoes=2,
        caracteristicas=("couraca", "pesada", "ressonante"), exercito="Cronos",
        armadura="Soma", resistencia_extra=1,
        tecnicas=("Peso do Céu", "Mão do Tártaro", "Era de Ouro"),
        assento="o golpe do deus que ainda dorme nele",
        tracos=["<strong>Meio desperto.</strong> O deus ainda não acordou inteiro no corpo: "
                "por isso um Ouro o enfrenta. Desperto de vez, é uma divindade menor "
                "(<a href=\"#deuses\">Capítulo Dez</a>).",
                "<strong>Soma.</strong> +1 de Resistência (já somada).",
                SETIMO_DOMINADO],
        quando="Mais duro que um Juiz do Inferno: quatro Bronzes de nível 17 vencem "
               "uma vez em quatro, e uns três caem; cinco, seis em dez. É o "
               "fim de uma campanha — ou o começo de outra, contra o deus inteiro."),
    "guerreiro-deus": dict(
        nome="Guerreiro Deus", nivel=15, posto="ouro", acessorio="nenhum", conviccoes=2,
        caracteristicas=("couraca", "ressonante", "estrelada"),
        exercito="Asgard", armadura="Veste Divina", teto_extra=1,
        tecnicas=("Presas do Lobo do Norte", "Ventania Gelada", "Tempestade de Cristal"),
        assento="Golpe da Estrela da Ursa Maior",
        tracos=["<strong>Safira de Odin.</strong> +1 no Teto de Cosmo enquanto a safira "
                "estiver na Veste (já somado).",
                SETIMO_DOMINADO],
        quando="Um dos sete. Quatro Bronzes do nível dele vencem duas vezes em três, e uns dois "
               "caem; três níveis abaixo, uma vez em sete. Sozinho, um personagem não vence."),
    "general-marina": dict(
        nome="General Marina", nivel=15, posto="ouro", acessorio="escudo", conviccoes=2,
        caracteristicas=("pesada", "espelhada", "couraca"),
        exercito="Poseidon", armadura="Escama", resistencia_extra=1,
        tecnicas=("Maré Devastadora", "Redemoinho", "Garra do Kraken"),
        assento="Triângulo das Ondas",
        tracos=["<strong>Escama de oricalco.</strong> +1 de Resistência (já somada).",
                SETIMO_DOMINADO],
        quando="O guardião de um dos sete pilares. Luta melhor debaixo d'água que qualquer "
               "Cavaleiro. Quatro Bronzes do nível dele vencem duas vezes em três, e uns dois "
               "caem."),
    "cavaleiro-de-ouro": dict(
        nome="Cavaleiro de Ouro", nivel=16, posto="ouro", acessorio="nenhum", conviccoes=3,
        caracteristicas=("ressonante", "ofuscante", "pesada"),
        exercito="Atena", armadura="Armadura de Ouro",
        tecnicas=("Impacto do Zodíaco", "Chama Dourada", "Muralha de Luz"),
        assento="o Golpe do Assento da vaga",
        tracos=[SETIMO_DOMINADO,
                "<strong>Três Convicções.</strong> Derrubar um Ouro uma vez não basta."],
        quando="Uma das doze casas. Um Bronze sozinho vence um destes menos de uma vez em "
               "cem, mesmo no nível dele. Quatro Bronzes de nível 15 vencem metade das "
               "vezes, e uns três caem; cinco, três vezes em quatro."),
    "juiz-do-inferno": dict(
        nome="Juiz do Inferno", nivel=18, posto="ouro", acessorio="asas", conviccoes=3,
        caracteristicas=("leve", "cortante", "coracao"),
        exercito="Hades", armadura="Súplice", teto_extra=1,
        tecnicas=("Garras do Grifo", "Marionete Cósmica", "Grande Cautela"),
        assento="Golpe do Juízo",
        tracos=["<strong>Estrela Maligna.</strong> Volta em <span class=\"dado\">1d4</span> "
                "semanas enquanto Hades existir.",
                "<strong>Juiz.</strong> +1 no Teto de Cosmo (já somado).",
                SETIMO_DOMINADO],
        quando="Um dos três juízes. Quatro Bronzes de nível 17 vencem metade das vezes, e "
               "uns três caem; de nível 18, duas vezes em três. É a luta de um arco inteiro."),
}

# ---------------------------------------------------------------------------
# Montar
# ---------------------------------------------------------------------------


def lutador(chave: str) -> Lutador:
    e = INIMIGOS[chave]
    desperta = e.get("desperta", R.desperta_do_mestre(e["posto"], e["conviccoes"]))
    x = montar(e["nome"], e["nivel"], e["posto"], acessorio=e["acessorio"],
               conviccoes=e["conviccoes"], caracteristicas=e["caracteristicas"],
               politica={"despertar": desperta})
    if e.get("sem_armadura"):
        x.armadura = "nenhuma"
    if e.get("sentido_inicial"):
        x.sentido_inicial = e["sentido_inicial"]
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


def _resposta(x: Lutador, t, nome: str, conviccoes: int) -> list:
    """A Resposta de Sozinho contra muitos, escrita na ficha: a técnica mais barata,
    só o dano. Nomeados sem Convicção não têm."""
    if not conviccoes:
        return []
    return ['<p class="rotulo-bloco">Resposta</p>',
            f'<p>Contra dois ou mais personagens, depois do turno de cada um: '
            f'<strong>{html.escape(nome)}</strong> contra quem acabou de agir, sem gastar '
            f'Cosmo · +{x.bonus_ataque(t.natureza)} contra a DEF · '
            f'<span class="dado">{dano_texto(x, t)}</span>. Só o dano.</p>']


def bloco(chave: str) -> str:
    e = INIMIGOS[chave]
    x = lutador(chave)
    x.reiniciar()
    fort, refl, vont = _defesas(x)
    teto = x.teto
    ini = (x.mods["des"] + (2 if "leve" in x.caracteristicas else 0)
           - (2 if "pesada" in x.caracteristicas else 0))
    if e.get("sentido_texto"):
        sentido = e["sentido_texto"]
    elif x.posto == "ouro":
        sentido = "Sétimo quando quiser"
    elif e.get("desperta", R.desperta_do_mestre(x.posto, e["conviccoes"])):
        sentido = "Sexto; desperta como um personagem"
    else:
        sentido = "Sexto; não desperta"
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
        + (f"<b>Armadura</b> nenhuma<br>" if e.get("sem_armadura") else
           f"<b>Armadura</b> {html.escape(e['armadura'])}, DEF +{x.armadura_def} · "
           f"<b>Resistência</b> {x.resistencia_max} · {_acessorio(x)}<br>"
           f"<b>Características</b> {_caracteristicas(x)}<br>") +
        f"<b>Convicções</b> {e['conviccoes']}"
    )
    posto_nome = e.get("posto_nome") or {"bronze": "Bronze", "prata": "Prata", "ouro": "Elite"}[x.posto]
    partes = [
        '<div class="criatura">',
        f'<h3>{html.escape(e["nome"])}<span class="kleos">Nível {x.nivel} · {posto_nome}</span></h3>',
        f'<p class="tipo">{html.escape(e["exercito"])}</p>',
        f'<div class="status">{status}</div>',
        '<p class="rotulo-bloco">Golpe comum</p>',
        f'<p>{_golpe(x)}. Acertou: +1 de Cosmo.</p>',
        '<p class="rotulo-bloco">Técnicas</p>',
        "<ul>" + "".join(f"<li>{i}</li>" for i in itens) + "</ul>",
        *_resposta(x, tecs["pequena"], nomes_tec[1], e["conviccoes"]),
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


# ---------------------------------------------------------------------------
# O aprendiz rival (0.10.0): um humano, fora do motor dos guerreiros
# ---------------------------------------------------------------------------

APRENDIZ_NIVEL = R.NIVEL_DA_PROVA
# DES 12, SAB 11, CON 11, FOR 10, INT 9, CAR 8: a distribuição humana, lutando pela DES
APRENDIZ = {"des": 12, "sab": 11, "con": 11, "for": 10, "int": 9, "car": 8}


def bloco_aprendiz() -> str:
    """A ficha do aprendiz que disputa a armadura: os números saem de sim/regras.py, os
    mesmos da prova medida em sim/mestre.py."""
    m = {k: R.mod(v) for k, v in APRENDIZ.items()}
    n = APRENDIZ_NIVEL
    p = R.prof(1)
    pv = R.pv_humano(n, m["con"])
    defe = R.HUMANO_DEF + m["des"]
    fort = R.HUMANO_DEFESA_PASSIVA + m["con"]
    refl = R.HUMANO_DEFESA_PASSIVA + m["des"] + p
    vont = R.HUMANO_DEFESA_PASSIVA + m["sab"] + p
    status = (f"<b>PV</b> {pv} <span class=\"sep\">·</span> <b>DEF</b> {defe} "
              f"<span class=\"sep\">·</span> <b>Iniciativa</b> +{m['des']}<br>"
              f"<b>Fortitude</b> {fort} <span class=\"sep\">·</span> <b>Reflexos</b> {refl} "
              f"<span class=\"sep\">·</span> <b>Vontade</b> {vont}<br>"
              f"<b>Cosmo</b> nenhum, ainda <span class=\"sep\">·</span> <b>Armadura</b> nenhuma<br>"
              f"<b>Perícias</b> Acrobacia +{m['des'] + p}, Atletismo +{m['for'] + p}<br>"
              f"<b>Convicções</b> {R.conviccoes_humanas(n)}")
    partes = [
        '<div class="criatura">',
        f'<h3>Aprendiz rival<span class="kleos">Nível humano {n}</span></h3>',
        '<p class="tipo">Qualquer exército, antes da armadura</p>',
        f'<div class="status">{status}</div>',
        '<p class="rotulo-bloco">Golpe comum</p>',
        f'<p>+{m["des"] + p} contra a DEF · <span class="dado">1d{R.dado_golpe_humano(n)} + '
        f'{m["des"]}</span>.</p>',
        '<p class="rotulo-bloco">Traços</p>',
        '<ul><li><strong>Uma Convicção.</strong> Na prova da armadura, ele levanta desperto '
        '(<a href="#antes-do-sexto">Capítulo Três</a>): com um quarto dos PV do nível 1 de '
        'guerreiro, o Cosmo no Teto e a técnica assinatura nascendo ali.</li>'
        '<li><strong>Diante de um desperto, é figurante.</strong> Fora da prova, contra quem '
        'já despertou, ele entra no bando.</li></ul>',
        '<p class="morte"><span class="rotulo-bloco">Quando usar</span>Na prova e no torneio '
        'da armadura, e no treino antes dela. Dois aprendizes assim levam umas quatro rodadas '
        'para um cair, e quase sempre os dois despertam. Anote os PV: com '
        f'{pv}, ele não aguenta mais que dois ou três golpes.</p>',
        "</div>",
    ]
    return "\n".join(partes)
