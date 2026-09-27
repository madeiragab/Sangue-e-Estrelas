"""A luta inteira, rodada a rodada, com as regras do livro.

Um duelo aqui tem tudo o que a mesa tem: o Cosmo subindo pelo relógio e pelo
golpe que acerta, a técnica que descarrega, queimar, a armadura aparando e
quebrando, o Elmo segurando o primeiro crítico, o Sétimo Sentido (à vontade
para o Ouro, no limite para o Bronze), a marca de Lida, cair e levantar com uma
Convicção, as Centelhas dos aliados e a Guerra dos Mil Dias.

As decisões de cada lutador saem de uma política simples e escrita — o que
um jogador razoável faria. Trocar a política é o jeito de medir se uma jogada
é boa: rodar o mesmo duelo com e sem ela.
"""

from __future__ import annotations

import random
from dataclasses import dataclass, field

import regras as R
from tecnica import Tecnica, tecnica_de_dano

# ---------------------------------------------------------------------------
# Dados
# ---------------------------------------------------------------------------


def d(rng: random.Random, lados: int) -> int:
    return rng.randint(1, lados)


def rolar(rng: random.Random, n: int, lados: int) -> int:
    return sum(rng.randint(1, lados) for _ in range(n))


def d20(rng: random.Random, vantagem: int) -> int:
    """vantagem > 0: dois dados, o maior; < 0: dois dados, o menor."""
    a = rng.randint(1, 20)
    if vantagem == 0:
        return a
    b = rng.randint(1, 20)
    return max(a, b) if vantagem > 0 else min(a, b)


# ---------------------------------------------------------------------------
# Políticas
# ---------------------------------------------------------------------------

POLITICA_PADRAO = {
    "aparar": True,          # gasta a Resistência da armadura
    "aparar_limiar": 0.20,   # apara golpes de pelo menos 20% dos PV máximos
    "bloquear": True,
    "concentrar": True,      # Concentra quando isso fecha o custo da técnica grande
    "queimar": True,         # queima para fechar uma técnica ou garantir a derrubada
    "despertar": True,       # Bronze/Prata: desperta o Sétimo quando pode
    "cegar_se": False,       # Bronze/Prata: se cega para despertar (mutilação)
    "levantar": True,        # gasta Convicção para levantar
    "tecnicas": True,        # usa técnicas
}


# ---------------------------------------------------------------------------
# O lutador
# ---------------------------------------------------------------------------


@dataclass
class Lutador:
    nome: str
    nivel: int
    posto: str
    atributos: dict
    tecnicas: list
    atr_golpe: str = "des"
    atr_cosmo: str = "sab"
    acessorio: str = "nenhum"          # nenhum · garras · escudo
    conviccoes: int | None = None      # None = o número da tabela
    politica: dict = field(default_factory=lambda: dict(POLITICA_PADRAO))
    treino_extra_pv: int = 0
    teto_fixo: int = 0                 # Safira de Odin, Juiz do Inferno
    resistencia_extra: int = 0         # Escama de oricalco: +1
    vigor: int = 0                     # escolhas de Vida
    cosmo_escolhas: int = 0            # escolhas de Cosmo: +1 Teto e +1 Cosmo inicial cada
    defesas_extra: int = 0             # defesas treinadas escolhidas
    formas: tuple = ()                 # o sangue de cada revivida, em ordem
    caracteristicas: tuple = ()        # as características da armadura (Capítulo Sete)

    def __post_init__(self):
        self.mods = {k: R.mod(v) for k, v in self.atributos.items()}
        self.prof = R.prof(self.nivel)
        self.pv_max = R.pv_maximo(self.nivel, self.mods["con"], self.vigor, self.treino_extra_pv)
        if self.conviccoes is None:
            self.conviccoes = R.conviccoes(self.nivel)
        self.conviccoes_max = self.conviccoes
        self.reiniciar()

    # ------------------------------------------------------------------
    def reiniciar(self):
        """O estado de começo de luta. Cada duelo simulado é uma luta avulsa,
        então as Convicções voltam cheias."""
        self.conviccoes = self.conviccoes_max
        self.pv = self.pv_max
        self.caido = False
        self.fora = False
        self.teto_extra = 0
        self.cosmo = R.cosmo_inicial(self.mods[self.atr_cosmo], self.cosmo_escolhas, self.teto)
        self.sentido = "sexto"
        self.teto_extra = 0            # Sétimo, Nono, sentidos, Centelhas
        self.centelhas_recebidas = 0
        self.sentidos_perdidos = []
        self.levantou = 0
        self.reacao = True
        self.condicoes: dict = {}      # condição -> {"de": quem impôs, "tec": a técnica}
        self.usadas: set = set()       # técnicas "uma vez por luta" já usadas
        self.carregado = ""            # técnica "exige carregar" já preparada
        self.desprevenido = False
        self.imune: set = set()        # técnicas cuja condição forte já acabou
        self.lido_por: set = set()     # nomes das minhas técnicas que o oponente já leu
        self.vantagem_proxima = False  # Centelha: Vantagem no próximo ataque
        bonus, res = R.POSTO[self.posto]
        if not R.formas_validas(self.posto, self.formas):
            raise ValueError(f"{self.nome}: a armadura de {self.posto} não aceita {self.formas}")
        forma = R.bonus_das_formas(self.formas)
        self.armadura_def = bonus + forma["def"]
        self.acerto_forma = forma["acerto"]
        car = self.caracteristicas
        self.resistencia_max = (res + forma["res"] + self.resistencia_extra
                                + (1 if self.acessorio == "nenhum" else 0)
                                + R.resistencia_por_nivel(self.nivel)
                                )
        if "ressonante" in car:
            self.cosmo += 1
        self.espelho_usado = False
        self.ofuscar_usado = False
        self.espinhos_turno = 0
        self.resistencia = self.resistencia_max
        self.elmo = True
        self.armadura_morta = False
        # estatística
        self.dano_golpe = 0
        self.dano_tecnica = 0
        self.tecnicas_usadas = 0
        self.queimas = 0
        self.despertou = False

    # ------------------------------------------------------------------
    @property
    def teto(self) -> int:
        return R.teto_base(self.nivel) + self.teto_extra + self.teto_fixo + self.cosmo_escolhas

    @property
    def armada(self) -> bool:
        """A armadura ainda está no corpo: nem morta, nem em pedaços."""
        return not self.armadura_morta and self.resistencia > 0

    @property
    def defesa(self) -> int:
        d_ = 10 + max(self.mods["des"], self.mods[self.atr_cosmo])
        if self.armada:
            d_ += self.armadura_def + (1 if "pesada" in self.caracteristicas else 0)
        if "visao" in self.sentidos_perdidos:
            d_ -= 2                    # não vê o golpe vindo
        return d_

    @property
    def degrau(self) -> int:
        return R.DEGRAU[self.sentido]

    def bonus_ataque(self, natureza: str) -> int:
        atr = self.atr_golpe if natureza == "golpe" else self.atr_cosmo
        # o acerto das formas só vale com a armadura no corpo; a Constelação viva, no Sétimo
        return (self.mods[atr] + self.prof + (self.acerto_forma if self.armada else 0)
                + (1 if "estrelada" in self.caracteristicas and self.degrau >= 1 else 0))

    def dano_golpe_comum(self, rng, critico: bool) -> int:
        lados = 10 if self.acessorio == "garras" and self.armada else 8
        n = 2 if critico else 1
        return rolar(rng, n, lados) + self.mods[self.atr_golpe]

    @property
    def piso(self) -> int:
        return min(self.teto, R.piso_cosmo(self.mods[self.atr_cosmo])
                   + int(self.cosmo_escolhas * R.PISO_POR_COSMO))

    def queima_maxima(self) -> int:
        return self.prof + (2 if self.degrau >= 1 else 0)

    def custo(self, t: Tecnica) -> int:
        return t.custo()

    # ------------------------------------------------------------------
    def subir_cosmo(self, n: int):
        self.cosmo = min(self.teto, self.cosmo + n)

    def entrar_no_setimo(self, rng=None):
        if self.sentido == "sexto":
            self.sentido = "setimo"
            self.teto_extra += R.TETO_SETIMO
            self.despertou = True

            self.lido_por.clear()      # o golpe conhecido volta na velocidade da luz

    def iniciativa(self, rng) -> int:
        car = self.caracteristicas
        return rng.randint(1, 20) + self.mods["des"] + (2 if "leve" in car else 0) - (2 if "pesada" in car else 0)

    def pode_usar(self, t: Tecnica) -> bool:
        """As limitações que proíbem: uma vez por luta, só com o Cosmo no Teto."""
        if "uma_vez" in t.limites and t.nome in self.usadas:
            return False
        if "teto" in t.limites and self.cosmo < self.teto:
            return False
        return True

    def defesas_passivas(self) -> dict:
        """14 + atributo, + proficiência nas treinadas (DES e SAB; CON a partir do 10)."""
        treinadas = {"des", "sab"} | ({"con"} if self.defesas_extra else set())
        return {a: 14 + self.mods[a] + (self.prof if a in treinadas else 0)
                for a in ("con", "des", "sab")}

    def perder_sentido(self, qual: str):
        self.sentidos_perdidos.append(qual)
        self.teto_extra += 1
        self.subir_cosmo(1)


# ---------------------------------------------------------------------------
# Montar um lutador pelo livro
# ---------------------------------------------------------------------------


def montar(nome: str, nivel: int, posto: str = "bronze", *, acessorio: str = "nenhum",
           conviccoes: int | None = None, politica: dict | None = None,
           kit: str = "padrao", formas: tuple = (), caracteristicas: tuple | None = None,
           escolhas: dict | None = None) -> Lutador:
    """Um lutador de Golpe (DES) com o Cosmo em SAB, construído pelo livro.

    Distribuição 15/14/13/12/10/8: DES 15, CON 14, SAB 13, FOR 12, INT 10,
    CAR 8. Os aumentos de atributo vão para a DES até 20 e depois para a CON.
    `escolhas` são as escolhas de nível (R.escolhas_padrao, se não vier nada).
    """
    esc = escolhas or R.escolhas_padrao(nivel)
    des, con = R.atributos_das_escolhas(esc)
    atr = {"des": des, "con": con, "sab": 13, "for": 12, "int": 10, "car": 8}
    g = R.grau(nivel)
    tam = R.TAMANHO_MAXIMO[g]
    # O kit padrão: a técnica grande (todo o tamanho em dano) e uma pequena, de
    # 2 pontos, para usar quando o Cosmo não fecha a grande.
    tecs = [tecnica_de_dano(tam, g, nome="grande"), tecnica_de_dano(2, g, nome="pequena")]
    if kit == "tres" or 2 + esc["tecnica_atributo"].count("t") >= 3:
        tecs.append(tecnica_de_dano(max(3, tam - 2), g, nome="media"))
    if posto == "ouro":
        # Golpe do Assento: tamanho máximo + 1, com atravessa
        assento = Tecnica("assento", "golpe", {"dano": tam}, mais=("atravessa",),
                          grau=g, assento=True)
        tecs.append(assento)
    pol = dict(POLITICA_PADRAO)
    if politica:
        pol.update(politica)
    if caracteristicas is None:     # as típicas do Posto: 1 no Bronze, 2 na Prata, 3 na elite
        caracteristicas = R.CARACTERISTICAS_PADRAO[:R.CARACTERISTICAS_POR_POSTO[posto]]
    return Lutador(nome, nivel, posto, atr, tecs, acessorio=acessorio,
                   conviccoes=conviccoes, politica=pol, formas=tuple(formas),
                   caracteristicas=tuple(caracteristicas),
                   vigor=esc["vida_cosmo"].count("v"), cosmo_escolhas=esc["vida_cosmo"].count("c"),
                   defesas_extra=esc["pericia_defesa"].count("d"))


# ---------------------------------------------------------------------------
# Condições (Capítulo Cinco)
# ---------------------------------------------------------------------------

PERDE_O_TURNO = ("atordoado", "paralisado")
CONTRA_COM_VANTAGEM = ("cego", "preso")
ATACA_COM_DESVANTAGEM = ("cego", "amedrontado")


# ---------------------------------------------------------------------------
# A luta
# ---------------------------------------------------------------------------


@dataclass
class Resultado:
    vencedor: str | None          # nome, ou None para empate
    rodadas: int
    mil_dias: bool = False
    detalhes: dict = field(default_factory=dict)


class Luta:
    def __init__(self, a: Lutador, b: Lutador, rng: random.Random,
                 centelhas_a: int = 0, centelhas_b: int = 0, max_rodadas: int = 40):
        self.a, self.b, self.rng = a, b, rng
        # Centelhas por lado: quantas cada lado recebe por rodada, até o limite
        self.centelhas = {a.nome: centelhas_a, b.nome: centelhas_b}
        self.max_rodadas = max_rodadas
        self.contagem_mil_dias = 0
        self.mil_dias_travou = False
        self.travado = False
        self.ultimo_natural_tecnica = {}   # nome -> (rodada, natural)
        self.rodada = 0

    # ------------------------------------------------------------------
    def oponente(self, x: Lutador) -> Lutador:
        return self.b if x is self.a else self.a

    def vantagem(self, atacante: Lutador, alvo: Lutador) -> int:
        dif = atacante.degrau - alvo.degrau
        tem = (dif >= 1 or alvo.desprevenido
               or any(c in alvo.condicoes for c in CONTRA_COM_VANTAGEM))
        sofre = dif <= -1 or any(c in atacante.condicoes for c in ATACA_COM_DESVANTAGEM)
        if tem and sofre:
            return 0
        return 1 if tem else (-1 if sofre else 0)

    def travados(self) -> bool:
        return self.travado

    def choque(self, x: Lutador, y: Lutador, natural: int):
        """Choque de Cosmos: no mesmo Sentido (Sétimo ou acima), se as técnicas
        dos dois na mesma rodada tiram o mesmo número natural, os Cosmos travam."""
        anterior = self.ultimo_natural_tecnica.get(y.nome)
        self.ultimo_natural_tecnica[x.nome] = (self.rodada, natural)
        if (not self.travado and x.degrau >= 1 and x.degrau == y.degrau
                and anterior is not None and anterior[0] == self.rodada
                and anterior[1] == natural and natural >= R.CHOQUE_MINIMO):
            self.travado = True
            self.mil_dias_travou = True

    def destravar(self):
        self.travado = False
        self.contagem_mil_dias = 0

    # ------------------------------------------------------------------
    def aplicar_dano(self, alvo: Lutador, dano: int, *, atravessa: bool, fonte: str,
                     atacante: Lutador, quebra: bool):
        if dano <= 0:
            return
        if self.travados():
            return                      # Guerra dos Mil Dias: ninguém fere ninguém
        if quebra and alvo.armada:
            alvo.resistencia -= 1
        if fonte == "golpe" and "cortante" in atacante.caracteristicas and atacante.armada:
            atravessa = True            # a lâmina da armadura: o golpe comum não se apara
        if (fonte == "golpe" and "espinhos" in alvo.caracteristicas and alvo.armada
                and atacante.espinhos_turno != self.rodada):
            atacante.espinhos_turno = self.rodada   # uma vez por turno de quem bate
            atacante.pv = max(0, atacante.pv - d(self.rng, 4) - R.grau(alvo.nivel))
            if atacante.pv == 0:
                atacante.caido = True
        if fonte == "golpe" and "couraca" in alvo.caracteristicas and alvo.armada:
            dano = max(0, dano - R.grau(alvo.nivel))   # o golpe comum bate na couraça
        antes = dano
        pol = alvo.politica
        reacao_ok = alvo.reacao or not R.APARAR_USA_REACAO
        if (not atravessa and pol["aparar"] and reacao_ok
                and (dano >= pol["aparar_limiar"] * alvo.pv_max or dano >= alvo.pv)):
            if alvo.armada:
                alvo.resistencia -= 1
                dano //= 2
                if R.APARAR_USA_REACAO:
                    alvo.reacao = False
                if (fonte == "tecnica" and "espelhada" in alvo.caracteristicas
                        and not alvo.espelho_usado):
                    alvo.espelho_usado = True   # o espelho devolve o que não entrou
                    atacante.pv = max(0, atacante.pv - rolar(self.rng, R.grau(alvo.nivel), 6))
                    if atacante.pv == 0:
                        atacante.caido = True
        alvo.pv = max(0, alvo.pv - dano)
        if fonte == "golpe":
            atacante.dano_golpe += dano
        else:
            atacante.dano_tecnica += dano
        if alvo.pv == 0:
            alvo.caido = True
            if not alvo.armada:
                alvo.armadura_morta = True

    # ------------------------------------------------------------------
    def rolar_ataque(self, atacante: Lutador, alvo: Lutador, bonus: int,
                     def_extra: int = 0, passiva: int | None = None,
                     tecnica: bool = False) -> tuple[bool, bool]:
        """Devolve (acertou, crítico). O alvo pode Bloquear antes da rolagem.
        Com `passiva`, é uma Rolagem de Efeito: contra a defesa passiva, sem
        Bloquear e sem crítico."""
        v = self.vantagem(atacante, alvo)
        alvo.desprevenido = False
        if (tecnica and "ofuscante" in alvo.caracteristicas and not alvo.ofuscar_usado
                and alvo.armada and not alvo.caido):
            alvo.ofuscar_usado = True   # o brilho da armadura, uma vez por luta
            v = max(-1, v - 1)
        if atacante.vantagem_proxima:
            atacante.vantagem_proxima = False
            v = 1 if v == 0 else (0 if v < 0 else v)
        bloqueio = 0
        pode_bloquear = (passiva is None and alvo.armada
                         and alvo.reacao and "tato" not in alvo.sentidos_perdidos
                         and not alvo.caido and alvo.politica["bloquear"]
                         and not (R.APARAR_USA_REACAO and alvo.politica["aparar"]))
        if pode_bloquear:
            alvo.reacao = False
            bloqueio = (3 if alvo.acessorio == "escudo" else 2) + (1 if "guarda" in alvo.caracteristicas else 0)
        # A Hierarquia: o Prata diante de um Bronze.
        if atacante.posto == "prata" and alvo.posto == "bronze":
            bonus += R.HIERARQUIA
        elif alvo.posto == "prata" and atacante.posto == "bronze":
            bonus -= R.HIERARQUIA
        # O Sétimo dominado do Ouro: diante de um Sétimo recém-despertado,
        # ele ainda luta um pouco acima.
        if atacante.degrau >= 1 and alvo.degrau >= 1:
            if atacante.posto == "ouro" and alvo.posto != "ouro":
                bonus += R.DOMINIO_OURO
            elif alvo.posto == "ouro" and atacante.posto != "ouro":
                bonus -= R.DOMINIO_OURO
        nat = d20(self.rng, v)
        self.ultimo_natural = nat
        dois_degraus = alvo.degrau - atacante.degrau >= 2
        if nat == 1:
            return False, False
        if dois_degraus:
            return (nat == 20), (nat == 20 and passiva is None)
        if passiva is not None:
            return nat + bonus >= passiva + def_extra, False
        if nat == 20:
            return True, True
        return nat + bonus >= alvo.defesa + bloqueio + def_extra, False

    def rolar_efeito(self, x: Lutador, y: Lutador, t: Tecnica, def_extra: int = 0) -> bool:
        """Rolagem de Efeito contra a defesa passiva mais fraca do alvo."""
        passiva = min(y.defesas_passivas().values())
        ok, _ = self.rolar_ataque(x, y, x.bonus_ataque(t.natureza), def_extra=def_extra,
                                  passiva=passiva)
        return ok

    def critico_vs_elmo(self, alvo: Lutador, critico: bool) -> bool:
        if critico and alvo.elmo and alvo.armada:
            alvo.elmo = False
            return False
        return critico

    # ------------------------------------------------------------------
    def golpe(self, x: Lutador, y: Lutador):
        ganhou = 0
        for _ in range(R.ataques_por_golpe(x.nivel)):
            if y.caido:
                break
            acertou, crit = self.rolar_ataque(x, y, x.bonus_ataque("golpe"))
            if acertou:
                crit = crit or "paralisado" in y.condicoes
                crit = self.critico_vs_elmo(y, crit)
                self.aplicar_dano(y, x.dano_golpe_comum(self.rng, crit), atravessa=False,
                                  fonte="golpe", atacante=x, quebra=False)
                ganhou += 1
        if ganhou:
            x.subir_cosmo(R.COSMO_ACERTO * (ganhou if R.COSMO_POR_CADA_ACERTO else 1))

    def usar_tecnica(self, x: Lutador, y: Lutador, t: Tecnica, queima: int):
        if "carregar" in t.limites and x.carregado != t.nome:
            # carregar: neste turno, nenhuma técnica — só o golpe comum
            x.carregado = t.nome
            self.golpe(x, y)
            return
        x.carregado = ""
        x.usadas.add(t.nome)
        if "fere" in t.limites:
            x.pv = max(1, x.pv - rolar(self.rng, t.grau, 6))
        if "desprevenido" in t.limites:
            x.desprevenido = True
        custo = x.custo(t)
        x.tecnicas_usadas += 1
        pago = min(x.cosmo, custo)
        falta = custo - pago                     # o que o Cosmo não pagou, a vida paga
        extra = max(0, queima)                   # pontos queimados além do custo
        # O Cosmo não acaba: gastar nunca o leva abaixo do piso
        x.cosmo = max(x.piso, x.cosmo - pago)
        cai_depois = False
        if falta or extra:
            x.queimas += 1
            preco = rolar(self.rng, (falta + extra) * t.grau, R.dado_de_queima(x.nivel))
            if preco >= x.pv:
                x.pv = 1
                cai_depois = True                # o golpe sai; você cai depois
            else:
                x.pv -= preco
        lido = (t.nome in x.lido_por) and not (falta or extra)
        if t.condicao:
            acertou = self.rolar_efeito(x, y, t, def_extra=R.BONUS_LIDO if lido else 0)
            crit = False
            if acertou and t.nome not in y.imune:
                y.condicoes[t.condicao] = {"de": x, "tec": t}
        else:
            acertou, crit = self.rolar_ataque(x, y, x.bonus_ataque(t.natureza),
                                              def_extra=R.BONUS_LIDO if lido else 0, tecnica=True)
        x.lido_por.add(t.nome)
        self.choque(x, y, self.ultimo_natural)
        if acertou and t.dados_de_dano:
            if t.natureza == "golpe" and "paralisado" in y.condicoes and not t.condicao:
                crit = True
            crit = self.critico_vs_elmo(y, crit)
            ndados = t.dados_de_dano + extra * t.grau + (t.grau if crit else 0)
            dano = rolar(self.rng, ndados, t.lado) + x.mods[x.atr_golpe if t.natureza == "golpe" else x.atr_cosmo]
            self.aplicar_dano(y, dano, atravessa=t.atravessa, fonte="tecnica",
                              atacante=x, quebra=t.quebra)
        if falta or extra:
            x.cosmo = x.piso                     # queimou: o Cosmo volta ao piso, não a zero
        if cai_depois and not y.caido:
            x.pv = 0                             # o último golpe não derrubou: você cai
            x.caido = True

    # ------------------------------------------------------------------
    def dano_esperado(self, x: Lutador, t: Tecnica, extra: int = 0) -> float:
        return (t.dados_de_dano + extra * t.grau) * R.media_dado(t.lado) + x.mods[x.atr_golpe]

    def escolher_e_agir(self, x: Lutador, y: Lutador):
        pol = x.politica
        tecs = (sorted((t for t in x.tecnicas if not t.condicao), key=lambda t: t.dados_de_dano,
                       reverse=True) if pol["tecnicas"] else [])

        # 1) a maior técnica que o Cosmo paga (e que as limitações deixam usar)
        tecs = [t for t in tecs if x.pode_usar(t)]
        grande = tecs[0] if tecs else None
        pagaveis = [t for t in tecs if x.custo(t) <= x.cosmo]

        # Diante de um Sentido acima, o Bronze guarda o Cosmo até o Teto para
        # despertar, em vez de gastá-lo em técnicas pequenas.
        poupando = (pol["despertar"] and x.posto in ("bronze", "prata")
                    and x.sentido == "sexto" and y.degrau > x.degrau
                    and x.cosmo < x.teto)
        if poupando:
            pagaveis = []

        # 1b) uma técnica de condição, se o alvo ainda não está com ela
        if pol.get("condicoes", True):
            for t in x.tecnicas:
                if (t.condicao and t.condicao not in y.condicoes and t.custo() <= x.cosmo
                        and not y.caido and x.pode_usar(t) and t.nome not in y.imune):
                    self.usar_tecnica(x, y, t, queima=0)
                    return

        # 2) despertar o Sétimo (Bronze e Prata): Cosmo no Teto + um sacrifício.
        #    Queimar é o sacrifício mais comum; cegar-se é opcional.
        if (pol["despertar"] and x.posto in ("bronze", "prata") and x.sentido == "sexto"
                and x.cosmo >= x.teto and grande is not None):
            vale = y.degrau > x.degrau or x.pv < 0.5 * x.pv_max
            if vale and pol["cegar_se"] and "visao" not in x.sentidos_perdidos:
                # a mutilação gasta a ação: fica cego, desperta, e só age no próximo turno
                x.pv = max(1, x.pv - d(self.rng, 6))
                x.perder_sentido("visao")
                x.entrar_no_setimo(self.rng)
                return
            if vale and pol["queimar"]:
                x.entrar_no_setimo(self.rng)     # a queima desta técnica é o sacrifício
                q = min(x.queima_maxima(), max(1, x.queima_maxima() // 2))
                self.usar_tecnica(x, y, grande, queima=q)
                return

        # 3) queimar: só o necessário, e só quando vale. Queimar fecha uma
        #    técnica que o Cosmo não paga, ou soma os pontos que faltam para
        #    derrubar — descontando o que a armadura do alvo vai aparar.
        if pol["queimar"] and grande is not None:
            qmax = x.queima_maxima()
            custo = x.custo(grande)
            por_ponto = R.media_dado(R.dado_de_queima(x.nivel)) * grande.grau
            apara = 0.5 if (not grande.atravessa and y.armada) else 1.0
            if x.cosmo < custo and pol.get("vida_paga", True):
                # A vida paga o que falta, sem limite. Vale quando derruba (mesmo que
                # você caia depois: o último golpe), ou quando rende bem mais dano
                # do que custa de vida.
                falta = custo - x.cosmo
                preco = falta * por_ponto
                # o último golpe (cair depois) só vale no fim, ou com Convicção para levantar
                pode_cair = (x.pv <= 0.15 * x.pv_max
                             or (x.conviccoes > 0 and x.levantou < R.LEVANTAR_POR_LUTA))
                derruba = (y.pv <= apara * self.dano_esperado(x, grande)
                           and (x.pv > preco or pode_cair))
                rende = (apara * self.dano_esperado(x, grande) >= pol.get("rende", 3.0) * preco
                         and x.pv - preco > pol.get("reserva", 0.15) * x.pv_max)
                if derruba or rende:
                    self.usar_tecnica(x, y, grande, queima=0)
                    return
            if x.cosmo >= custo and y.pv > apara * self.dano_esperado(x, grande):
                for extra in range(1, qmax + 1):
                    if y.pv <= apara * self.dano_esperado(x, grande, extra):
                        if x.pv - extra * por_ponto > 0.4 * x.pv_max:
                            self.usar_tecnica(x, y, grande, queima=extra)
                            return
                        break

        if pagaveis:
            t = pagaveis[0]
            # guarda Cosmo para a grande se ela está a um passo, a não ser que a
            # pequena derrube
            if (t is not grande and grande is not None
                    and y.pv > self.dano_esperado(x, t) and x.pv > 0.3 * x.pv_max):
                pass    # guarda o Cosmo para a grande
            else:
                self.usar_tecnica(x, y, t, queima=0)
                return

        # 4) Concentrar quando isso fecha a grande e o golpe não fecharia
        if (pol["concentrar"] and grande is not None
                and x.cosmo + R.COSMO_ACERTO < x.custo(grande) <= x.cosmo + R.COSMO_CONCENTRAR):
            x.subir_cosmo(R.COSMO_CONCENTRAR)
            return

        self.golpe(x, y)

    # ------------------------------------------------------------------
    def turno(self, x: Lutador, rodada: int) -> None:
        y = self.oponente(x)
        x.reacao = True
        if x.caido:
            pode = (x.politica["levantar"] and x.conviccoes > 0
                    and x.levantou < R.LEVANTAR_POR_LUTA)
            if not pode:
                x.fora = True
                return
            x.conviccoes -= 1
            x.levantou += 1
            x.caido = False
            x.pv = R.ceil_div(x.pv_max, 4)
            if "coracao" in x.caracteristicas:
                x.vantagem_proxima = True        # o coração de estrela: levanta atacando
            x.cosmo = x.teto
            if x.posto in ("bronze", "prata"):
                x.entrar_no_setimo(self.rng)     # levantar é o sacrifício; a Convicção foi dita
        if rodada >= 2:
            x.subir_cosmo(R.COSMO_RELOGIO)
        if x.posto == "ouro":
            x.entrar_no_setimo(self.rng)
        # Centelhas dos aliados
        n = self.centelhas.get(x.nome, 0)
        while n and x.centelhas_recebidas < R.TETO_CENTELHA_MAX:
            x.centelhas_recebidas += 1
            x.teto_extra += 1
            x.subir_cosmo(R.COSMO_CENTELHA)
            if R.CENTELHA_VANTAGEM:
                x.vantagem_proxima = True
            n -= 1
            if self.travado:
                self.destravar()         # Cosmo de fora quebra a igualdade
        if any(c in x.condicoes for c in PERDE_O_TURNO):
            x.reacao = False
        else:
            self.escolher_e_agir(x, y)
        self.fim_do_turno(x)

    def fim_do_turno(self, x: Lutador):
        """Queimando fere; quem impôs cada condição rola de novo para mantê-la."""
        for nome, c in list(x.condicoes.items()):
            if nome == "queimando":
                x.pv = max(0, x.pv - rolar(self.rng, c["tec"].grau, 6))
                if x.pv == 0:
                    x.caido = True
            if c["de"].fora or not self.rolar_efeito(c["de"], x, c["tec"]):
                del x.condicoes[nome]
                if nome in R.CONDICOES_FORTES:
                    x.imune.add(c["tec"].nome)

    def lutar(self) -> Resultado:
        a, b, rng = self.a, self.b, self.rng
        a.reiniciar()
        b.reiniciar()
        ini_a = a.iniciativa(rng)
        ini_b = b.iniciativa(rng)
        ordem = [a, b] if (ini_a, a.mods["des"], rng.random()) >= (ini_b, b.mods["des"], rng.random()) else [b, a]
        for rodada in range(1, self.max_rodadas + 1):
            self.rodada = rodada
            for x in ordem:
                self.turno(x, rodada)
                y = self.oponente(x)
                if x.fora or y.fora:
                    break
                # quem caiu e não pode levantar perde na hora
                for z in (x, y):
                    if z.caido and not (z.politica["levantar"] and z.conviccoes > 0
                                        and z.levantou < R.LEVANTAR_POR_LUTA):
                        z.fora = True
                if x.fora or y.fora:
                    break
            if a.fora or b.fora:
                vencedor = None if (a.fora and b.fora) else (b.nome if a.fora else a.nome)
                return Resultado(vencedor, rodada, self.mil_dias_travou, self.detalhes())
            # Guerra dos Mil Dias
            if self.travados():
                self.mil_dias_travou = True
                self.contagem_mil_dias += 1
                if self.contagem_mil_dias >= R.MIL_DIAS_SEGMENTOS:
                    for z in (a, b):
                        z.pv = 0
                        z.armadura_morta = True
                    return Resultado(None, rodada, True, self.detalhes())
        return Resultado(None, self.max_rodadas, self.mil_dias_travou, self.detalhes())

    def detalhes(self) -> dict:
        out = {}
        for z in (self.a, self.b):
            out[z.nome] = {
                "dano_golpe": z.dano_golpe, "dano_tecnica": z.dano_tecnica,
                "tecnicas": z.tecnicas_usadas, "queimas": z.queimas,
                "despertou": z.despertou, "levantou": z.levantou,
                "armadura_morta": z.armadura_morta,
            }
        return out


# ---------------------------------------------------------------------------
# Um grupo contra um
# ---------------------------------------------------------------------------


class LutaGrupo(Luta):
    """Um grupo contra um lutador só. O grupo inteiro ataca o chefe; o chefe bate
    sempre no mais ferido de pé. Sem Guerra dos Mil Dias (ela é de duelo)."""

    def __init__(self, grupo: list, chefe: Lutador, rng: random.Random,
                 centelhas_grupo: int = 0, max_rodadas: int = 40,
                 pv_chefe: float = 1.0, acoes_chefe: int = 0):
        super().__init__(grupo[0], chefe, rng, max_rodadas=max_rodadas)
        self.grupo, self.chefe = grupo, chefe
        self.centelhas = {z.nome: centelhas_grupo for z in grupo}
        self.centelhas[chefe.nome] = 0
        # Sozinho contra muitos: PV multiplicados e ações a mais por rodada
        if not hasattr(chefe, "pv_base"):
            chefe.pv_base = chefe.pv_max
        chefe.pv_max = round(chefe.pv_base * pv_chefe)
        self.acoes_chefe = acoes_chefe

    def oponente(self, x: Lutador) -> Lutador:
        if x is not self.chefe:
            return self.chefe
        de_pe = [z for z in self.grupo if not z.fora and not z.caido]
        return min(de_pe or [z for z in self.grupo if not z.fora] or self.grupo,
                   key=lambda z: z.pv)

    def choque(self, x: Lutador, y: Lutador, natural: int):
        pass

    @staticmethod
    def pode_levantar(z: Lutador) -> bool:
        return z.politica["levantar"] and z.conviccoes > 0 and z.levantou < R.LEVANTAR_POR_LUTA

    def lutar(self) -> Resultado:
        todos = self.grupo + [self.chefe]
        for z in todos:
            z.reiniciar()
        ordem = sorted(todos, key=lambda z: (z.iniciativa(self.rng),
                                             z.mods["des"], self.rng.random()), reverse=True)
        for rodada in range(1, self.max_rodadas + 1):
            self.rodada = rodada
            extras = self.acoes_chefe
            for x in ordem:
                if x.fora:
                    continue
                self.turno(x, rodada)
                # a ação a mais do chefe vem logo depois do turno de alguém do grupo
                c = self.chefe
                if (x is not c and extras > 0 and not c.fora and not c.caido
                        and not any(k in c.condicoes for k in PERDE_O_TURNO)):
                    extras -= 1
                    if R.CHEFE_ACAO_SO_GOLPE:
                        self.golpe(c, self.oponente(c))
                    else:
                        self.escolher_e_agir(c, self.oponente(c))
                for z in todos:
                    if z.caido and not z.fora and not self.pode_levantar(z):
                        z.fora = True
                if self.chefe.fora:
                    return Resultado("grupo", rodada, False, {})
                if all(z.fora for z in self.grupo):
                    return Resultado(self.chefe.nome, rodada, False, {})
        return Resultado(None, self.max_rodadas, False, {})


def grupo_contra_um(fabrica_grupo, fabrica_chefe, n: int = 1000, semente: int = 1,
                    sozinho_contra_muitos: bool = True, **kw) -> dict:
    """Roda n lutas de grupo e resume: quanto o grupo vence, quantos caem. Um chefe
    com Convicções usa a regra Sozinho contra muitos, a não ser que se peça o contrário."""
    rng = random.Random(semente)
    g, c = fabrica_grupo(), fabrica_chefe()
    if sozinho_contra_muitos and c.conviccoes_max > 0:
        kw.setdefault("pv_chefe", R.chefe_pv(len(g)))
        kw.setdefault("acoes_chefe", R.chefe_acoes(len(g)))
    vit = emp = 0
    rodadas = caidos = 0
    for _ in range(n):
        r = LutaGrupo(g, c, rng, **kw).lutar()
        vit += r.vencedor == "grupo"
        emp += r.vencedor is None
        rodadas += r.rodadas
        caidos += sum(z.fora or z.caido for z in g)
    return {"grupo": vit / n, "empate": emp / n, "rodadas_media": rodadas / n,
            "caidos_media": caidos / n}


# ---------------------------------------------------------------------------
# Muitas lutas
# ---------------------------------------------------------------------------


def duelos(fabrica_a, fabrica_b, n: int = 2000, semente: int = 1, **kw) -> dict:
    """Roda n lutas e resume. As fábricas devolvem lutadores novos."""
    rng = random.Random(semente)
    a, b = fabrica_a(), fabrica_b()
    vit_a = vit_b = emp = mil = 0
    rodadas = []
    dano_tec = dano_golpe = 0
    tecs = queimas = desp_a = desp_b = lev = 0
    for _ in range(n):
        r = Luta(a, b, rng, **kw).lutar()
        rodadas.append(r.rodadas)
        if r.vencedor == a.nome:
            vit_a += 1
        elif r.vencedor == b.nome:
            vit_b += 1
        else:
            emp += 1
        mil += r.mil_dias
        for nome, det in r.detalhes.items():
            dano_tec += det["dano_tecnica"]
            dano_golpe += det["dano_golpe"]
            tecs += det["tecnicas"]
            queimas += det["queimas"]
            lev += det["levantou"]
        desp_a += r.detalhes[a.nome]["despertou"]
        desp_b += r.detalhes[b.nome]["despertou"]
    rodadas.sort()
    total = max(1, dano_tec + dano_golpe)
    return {
        "a": vit_a / n, "b": vit_b / n, "empate": emp / n, "mil_dias": mil / n,
        "rodadas_media": sum(rodadas) / n, "rodadas_mediana": rodadas[n // 2],
        "parte_tecnica": dano_tec / total,
        "tecnicas_por_luta": tecs / n, "queimas_por_luta": queimas / n,
        "levantadas_por_luta": lev / n,
        "despertar_a": desp_a / n, "despertar_b": desp_b / n,
    }
