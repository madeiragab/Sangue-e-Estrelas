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
    formas: tuple = ()                 # o sangue de cada revivida, em ordem

    def __post_init__(self):
        self.mods = {k: R.mod(v) for k, v in self.atributos.items()}
        self.prof = R.prof(self.nivel)
        self.pv_max = R.pv_maximo(self.nivel, self.mods["con"], self.treino_extra_pv)
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
        self.cosmo = R.cosmo_inicial(self.mods[self.atr_cosmo], self.nivel)
        self.sentido = "sexto"
        self.teto_extra = 0            # Sétimo, Nono, sentidos, Centelhas
        self.centelhas_recebidas = 0
        self.sentidos_perdidos = []
        self.levantou = 0
        self.reacao = True
        self.lido_por: set = set()     # nomes das minhas técnicas que o oponente já leu
        self.vantagem_proxima = False  # Centelha: Vantagem no próximo ataque
        bonus, res = R.POSTO[self.posto]
        forma_def, forma_res = R.bonus_das_formas(self.formas)
        self.armadura_def = bonus + forma_def
        self.resistencia_max = (res + forma_res + self.resistencia_extra
                                + (1 if self.acessorio == "nenhum" else 0)
                                + R.resistencia_por_nivel(self.nivel))
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
        return R.teto_base(self.nivel) + self.teto_extra + self.teto_fixo

    @property
    def armada(self) -> bool:
        """A armadura ainda está no corpo: nem morta, nem em pedaços."""
        return not self.armadura_morta and self.resistencia > 0

    @property
    def defesa(self) -> int:
        d_ = 10 + self.mods["des"]
        if self.armada:
            d_ += self.armadura_def
        if "visao" in self.sentidos_perdidos:
            d_ -= 2                    # não vê o golpe vindo
        return d_

    @property
    def degrau(self) -> int:
        return R.DEGRAU[self.sentido]

    def bonus_ataque(self, natureza: str) -> int:
        atr = self.atr_golpe if natureza == "golpe" else self.atr_cosmo
        return self.mods[atr] + self.prof

    def dano_golpe_comum(self, rng, critico: bool) -> int:
        lados = 10 if self.acessorio == "garras" and self.armada else 8
        n = 2 if critico else 1
        return rolar(rng, n, lados) + self.mods[self.atr_golpe]

    def queima_maxima(self) -> int:
        return self.prof + (2 if self.degrau >= 1 else 0)

    # ------------------------------------------------------------------
    def subir_cosmo(self, n: int):
        self.cosmo = min(self.teto, self.cosmo + n)

    def entrar_no_setimo(self):
        if self.sentido == "sexto":
            self.sentido = "setimo"
            self.teto_extra += R.TETO_SETIMO
            self.despertou = True
            self.lido_por.clear()      # o golpe conhecido volta na velocidade da luz

    def perder_sentido(self, qual: str):
        self.sentidos_perdidos.append(qual)
        self.teto_extra += 1
        self.subir_cosmo(1)


# ---------------------------------------------------------------------------
# Montar um lutador pelo livro
# ---------------------------------------------------------------------------


def montar(nome: str, nivel: int, posto: str = "bronze", *, acessorio: str = "nenhum",
           conviccoes: int | None = None, politica: dict | None = None,
           kit: str = "padrao", formas: tuple = ()) -> Lutador:
    """Um lutador de Golpe (DES) com o Cosmo em SAB, construído pelo livro.

    Distribuição 15/14/13/12/10/8: DES 15, CON 14, SAB 13, FOR 12, INT 10,
    CAR 8. Os aumentos vão para a DES até 20 e depois para a CON.
    """
    atr = {
        "des": R.atributo_no_nivel(15, nivel, 0),
        "con": R.atributo_no_nivel(14, nivel, 1),
        "sab": 13, "for": 12, "int": 10, "car": 8,
    }
    g = R.grau(nivel)
    tam = R.TAMANHO_MAXIMO[g]
    # O kit padrão: a técnica grande (todo o tamanho em dano) e uma pequena, de
    # 2 pontos, para usar quando o Cosmo não fecha a grande.
    tecs = [tecnica_de_dano(tam, g, nome="grande"), tecnica_de_dano(2, g, nome="pequena")]
    if kit == "tres" or R.tecnicas_conhecidas(nivel) >= 3:
        tecs.append(tecnica_de_dano(max(3, tam - 2), g, nome="media"))
    if posto == "ouro":
        # Golpe do Assento: tamanho máximo + 1, com atravessa
        assento = Tecnica("assento", "golpe", {"dano": tam}, mais=("atravessa",),
                          grau=g, assento=True)
        tecs.append(assento)
    pol = dict(POLITICA_PADRAO)
    if politica:
        pol.update(politica)
    return Lutador(nome, nivel, posto, atr, tecs, acessorio=acessorio,
                   conviccoes=conviccoes, politica=pol, formas=tuple(formas))


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
        v = 1 if dif >= 1 else (-1 if dif <= -1 else 0)
        return v

    def travados(self) -> bool:
        return self.travado

    def choque(self, x: Lutador, y: Lutador, natural: int):
        """Choque de Cosmos: no mesmo Sentido (Sétimo ou acima), se as técnicas
        dos dois na mesma rodada tiram o mesmo número natural, os Cosmos travam."""
        anterior = self.ultimo_natural_tecnica.get(y.nome)
        self.ultimo_natural_tecnica[x.nome] = (self.rodada, natural)
        if (not self.travado and x.degrau >= 1 and x.degrau == y.degrau
                and anterior is not None and anterior[0] == self.rodada
                and anterior[1] == natural):
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
        pol = alvo.politica
        reacao_ok = alvo.reacao or not R.APARAR_USA_REACAO
        if (not atravessa and pol["aparar"] and reacao_ok
                and (dano >= pol["aparar_limiar"] * alvo.pv_max or dano >= alvo.pv)):
            if alvo.armada:
                alvo.resistencia -= 1
                dano //= 2
                if R.APARAR_USA_REACAO:
                    alvo.reacao = False
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
                     def_extra: int = 0) -> tuple[bool, bool]:
        """Devolve (acertou, crítico). O alvo pode Bloquear antes da rolagem."""
        v = self.vantagem(atacante, alvo)
        if atacante.vantagem_proxima:
            atacante.vantagem_proxima = False
            v = 1 if v == 0 else (0 if v < 0 else v)
        bloqueio = 0
        pode_bloquear = (alvo.armada
                         and alvo.reacao and "tato" not in alvo.sentidos_perdidos
                         and not alvo.caido and alvo.politica["bloquear"]
                         and not (R.APARAR_USA_REACAO and alvo.politica["aparar"]))
        if pode_bloquear:
            alvo.reacao = False
            bloqueio = 3 if alvo.acessorio == "escudo" else 2
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
            return (nat == 20), (nat == 20)
        if nat == 20:
            return True, True
        return nat + bonus >= alvo.defesa + bloqueio + def_extra, False

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
                crit = self.critico_vs_elmo(y, crit)
                self.aplicar_dano(y, x.dano_golpe_comum(self.rng, crit), atravessa=False,
                                  fonte="golpe", atacante=x, quebra=False)
                ganhou += 1
        if ganhou:
            x.subir_cosmo(R.COSMO_ACERTO * (ganhou if R.COSMO_POR_CADA_ACERTO else 1))

    def usar_tecnica(self, x: Lutador, y: Lutador, t: Tecnica, queima: int):
        x.tecnicas_usadas += 1
        custo = t.custo()
        pago = min(x.cosmo, custo)
        falta = custo - pago
        extra = max(0, queima - falta)          # pontos queimados além do custo
        x.cosmo -= pago
        if queima:
            x.queimas += 1
            x.pv = max(1, x.pv - rolar(self.rng, queima * t.grau, R.dado_de_queima(x.nivel)))
        lido = (t.nome in x.lido_por) and queima == 0
        acertou, crit = self.rolar_ataque(x, y, x.bonus_ataque(t.natureza),
                                          def_extra=R.BONUS_LIDO if lido else 0)
        x.lido_por.add(t.nome)
        self.choque(x, y, self.ultimo_natural)
        if acertou:
            crit = self.critico_vs_elmo(y, crit)
            ndados = t.dados_de_dano + extra * t.grau + (t.grau if crit else 0)
            dano = rolar(self.rng, ndados, t.lado) + x.mods[x.atr_golpe if t.natureza == "golpe" else x.atr_cosmo]
            self.aplicar_dano(y, dano, atravessa=t.atravessa, fonte="tecnica",
                              atacante=x, quebra=t.quebra)
        if queima:
            x.cosmo = 0

    # ------------------------------------------------------------------
    def dano_esperado(self, x: Lutador, t: Tecnica, extra: int = 0) -> float:
        return (t.dados_de_dano + extra * t.grau) * R.media_dado(t.lado) + x.mods[x.atr_golpe]

    def escolher_e_agir(self, x: Lutador, y: Lutador):
        pol = x.politica
        tecs = sorted(x.tecnicas, key=lambda t: t.dados_de_dano, reverse=True) if pol["tecnicas"] else []
        grande = tecs[0] if tecs else None

        # 1) a maior técnica que o Cosmo paga
        pagaveis = [t for t in tecs if t.custo() <= x.cosmo]

        # Diante de um Sentido acima, o Bronze guarda o Cosmo até o Teto para
        # despertar, em vez de gastá-lo em técnicas pequenas.
        poupando = (pol["despertar"] and x.posto in ("bronze", "prata")
                    and x.sentido == "sexto" and y.degrau > x.degrau
                    and x.cosmo < x.teto)
        if poupando:
            pagaveis = []

        # 2) despertar o Sétimo (Bronze e Prata): Cosmo no Teto + um sacrifício.
        #    Queimar é o sacrifício mais comum; cegar-se é opcional.
        if (pol["despertar"] and x.posto in ("bronze", "prata") and x.sentido == "sexto"
                and x.cosmo >= x.teto and grande is not None):
            vale = y.degrau > x.degrau or x.pv < 0.5 * x.pv_max
            if vale and pol["cegar_se"] and "visao" not in x.sentidos_perdidos:
                # a mutilação gasta a ação: fica cego, desperta, e só age no próximo turno
                x.pv = max(1, x.pv - d(self.rng, 6))
                x.perder_sentido("visao")
                x.entrar_no_setimo()
                return
            if vale and pol["queimar"]:
                x.entrar_no_setimo()     # a queima desta técnica é o sacrifício
                q = min(x.queima_maxima(), max(1, x.queima_maxima() // 2))
                self.usar_tecnica(x, y, grande, queima=q)
                return

        # 3) queimar: só o necessário, e só quando vale. Queimar fecha uma
        #    técnica que o Cosmo não paga, ou soma os pontos que faltam para
        #    derrubar — descontando o que a armadura do alvo vai aparar.
        if pol["queimar"] and grande is not None:
            qmax = x.queima_maxima()
            custo = grande.custo()
            por_ponto = R.media_dado(R.dado_de_queima(x.nivel)) * grande.grau
            apara = 0.5 if (not grande.atravessa and y.armada) else 1.0
            if x.cosmo < custo <= x.cosmo + qmax:
                falta = custo - x.cosmo
                if (y.pv <= apara * self.dano_esperado(x, grande) or x.pv <= 0.35 * x.pv_max) \
                        and x.pv - falta * por_ponto > 0.25 * x.pv_max:
                    self.usar_tecnica(x, y, grande, queima=falta)
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
                and x.cosmo + R.COSMO_ACERTO < grande.custo() <= x.cosmo + R.COSMO_CONCENTRAR):
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
            x.cosmo = x.teto
            if x.posto in ("bronze", "prata"):
                x.entrar_no_setimo()     # levantar é o sacrifício; a Convicção foi dita
        if rodada >= 2:
            x.subir_cosmo(R.COSMO_RELOGIO)
        if x.posto == "ouro":
            x.entrar_no_setimo()
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
        self.escolher_e_agir(x, y)

    def lutar(self) -> Resultado:
        a, b, rng = self.a, self.b, self.rng
        a.reiniciar()
        b.reiniciar()
        ini_a = rng.randint(1, 20) + a.mods["des"]
        ini_b = rng.randint(1, 20) + b.mods["des"]
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
