# As ferramentas do Mestre, medidas

Gerado por `python sim/mestre.py`. 800 duelos por célula (400 nas lutas de grupo, 2000 nos bandos), sementes fixas. O personagem tem três Convicções e levanta no máximo uma vez por luta.

## Quanto pesa um inimigo

| Dificuldade | Inimigo | O personagem vence |
|---|---|---:|
| Fácil | Nomeado sem Convicção, do mesmo nível ou um acima | 56% a 99% |
| Justa | Mesmo nível e mesmo Posto, com três Convicções, como o personagem | 48% a 52% |
| Difícil | Rival um nível acima, com uma Convicção | 12% a 35% |
| Muito difícil | Rival dois níveis acima, com uma Convicção | 4% a 23% |
| Muito difícil | Um Prata do mesmo nível com uma Convicção, contra um Bronze | 6% a 12% |
| Mortal | Elite do mesmo nível, contra um Bronze ou um Prata | 0% |
| Mortal, mas possível | Elite três níveis abaixo do personagem (a partir do nível 18) | 0% a 5% |

| Nomeado sem Convicção um nível acima do personagem | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| O inimigo vence | 44% | 29% | 34% | 33% | 19% | 15% | 17% | 26% | 34% | 23% | 21% | 34% | 36% | 19% | 8% | 5% | 3% | 3% | 1% |

| A fronteira do Posto | O personagem vence |
|---|---:|
| Bronze de nível 8 contra Prata de nível 9, uma Convicção | 6% |
| Bronze de nível 9 contra Prata de nível 9, uma Convicção | 10% |
| Bronze de nível 14 contra elite de nível 15 | 0% |
| Prata de nível 14 contra elite de nível 15 | 0% |

## Figurantes

Um personagem sozinho contra um bando da tabela. O golpe comum que acerta derruba 2; a técnica de alvo único, 3; a de área, os que pegar, até 6. O dano do bando não se apara e o ataque dele não tem crítico.

| Nível | DEF · ataque · dano | Seis, sem área | Seis, com área | Dez, sem área | Doze, com área |
|---:|---|---|---|---|---|
| 1 | 11 · +4 · 2 | 4.0 rodadas, 28% dos PV | 1.8 rodadas, 13% dos PV | 5.7 rodadas, 47% dos PV, cai 2% | 4.2 rodadas, 36% dos PV, cai 1% |
| 2 | 11 · +4 · 3 | 4.0 rodadas, 29% dos PV | 1.8 rodadas, 13% dos PV | 5.7 rodadas, 49% dos PV, cai 2% | 4.2 rodadas, 37% dos PV, cai 1% |
| 3 | 12 · +4 · 4 | 3.8 rodadas, 27% dos PV | 1.7 rodadas, 12% dos PV | 6.1 rodadas, 53% dos PV, cai 4% | 3.8 rodadas, 34% dos PV, cai 1% |
| 4 | 12 · +4 · 6 | 3.8 rodadas, 30% dos PV, cai 1% | 1.7 rodadas, 14% dos PV | 6.1 rodadas, 57% dos PV, cai 8% | 3.9 rodadas, 38% dos PV, cai 4% |
| 5 | 12 · +5 · 7 | 2.9 rodadas, 22% dos PV | 1.4 rodadas, 11% dos PV | 5.7 rodadas, 52% dos PV, cai 2% | 2.9 rodadas, 26% dos PV |
| 6 | 13 · +5 · 9 | 2.9 rodadas, 20% dos PV | 1.4 rodadas, 10% dos PV | 5.8 rodadas, 51% dos PV, cai 3% | 2.9 rodadas, 25% dos PV |
| 7 | 13 · +5 · 11 | 2.9 rodadas, 21% dos PV | 1.4 rodadas, 10% dos PV | 5.7 rodadas, 51% dos PV, cai 2% | 2.8 rodadas, 25% dos PV |
| 8 | 13 · +5 · 13 | 2.9 rodadas, 20% dos PV | 1.4 rodadas, 10% dos PV | 5.6 rodadas, 50% dos PV, cai 2% | 2.9 rodadas, 25% dos PV |
| 9 | 14 · +6 · 15 | 2.5 rodadas, 19% dos PV | 1.4 rodadas, 10% dos PV | 3.8 rodadas, 34% dos PV | 2.9 rodadas, 26% dos PV |
| 10 | 14 · +6 · 17 | 2.3 rodadas, 16% dos PV | 1.3 rodadas, 8% dos PV | 3.6 rodadas, 29% dos PV | 2.6 rodadas, 22% dos PV |
| 11 | 14 · +6 · 20 | 2.3 rodadas, 16% dos PV | 1.3 rodadas, 8% dos PV | 3.6 rodadas, 30% dos PV | 2.7 rodadas, 22% dos PV |
| 12 | 15 · +6 · 23 | 2.4 rodadas, 18% dos PV | 1.4 rodadas, 10% dos PV | 3.8 rodadas, 32% dos PV | 2.8 rodadas, 24% dos PV |
| 13 | 15 · +7 · 26 | 2.3 rodadas, 17% dos PV | 1.3 rodadas, 9% dos PV | 3.6 rodadas, 32% dos PV | 2.7 rodadas, 24% dos PV |
| 14 | 15 · +7 · 29 | 2.2 rodadas, 15% dos PV | 1.3 rodadas, 8% dos PV | 3.4 rodadas, 28% dos PV | 2.5 rodadas, 21% dos PV |
| 15 | 16 · +7 · 32 | 2.3 rodadas, 16% dos PV | 1.3 rodadas, 8% dos PV | 3.6 rodadas, 29% dos PV | 2.7 rodadas, 23% dos PV |
| 16 | 16 · +7 · 36 | 2.3 rodadas, 16% dos PV | 1.3 rodadas, 9% dos PV | 3.6 rodadas, 30% dos PV | 2.7 rodadas, 23% dos PV |
| 17 | 16 · +8 · 40 | 2.2 rodadas, 16% dos PV | 1.2 rodadas, 8% dos PV | 3.4 rodadas, 29% dos PV | 2.5 rodadas, 22% dos PV |
| 18 | 17 · +8 · 44 | 2.3 rodadas, 16% dos PV | 1.3 rodadas, 9% dos PV | 3.6 rodadas, 30% dos PV | 2.7 rodadas, 23% dos PV |
| 19 | 17 · +8 · 48 | 2.3 rodadas, 16% dos PV | 1.3 rodadas, 9% dos PV | 3.6 rodadas, 30% dos PV | 2.6 rodadas, 22% dos PV |
| 20 | 17 · +8 · 52 | 2.3 rodadas, 16% dos PV | 1.4 rodadas, 9% dos PV | 3.6 rodadas, 30% dos PV | 2.7 rodadas, 23% dos PV |

## A surpresa

Dois Bronzes do mesmo nível; o primeiro pegou o outro sem ser percebido e dá o golpe de abertura: um golpe comum antes da Iniciativa, com Vantagem, e o outro sem reação até o primeiro turno dele.

| Nível | 1 | 3 | 5 | 9 | 13 | 17 | 20 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Quem surpreende vence | 59% | 66% | 60% | 61% | 63% | 60% | 52% |

## O aliado de luta

Metade do nível do grupo, metade dos PV, sem Convicção; não conta para Sozinho contra muitos.

| Contra um rival do mesmo nível, com uma Convicção | Sozinho | Com o aliado |
|---|---:|---:|
| Nível 3 | 51% | 78% |
| Nível 7 | 49% | 72% |
| Nível 11 | 48% | 72% |
| Nível 15 | 51% | 70% |
| Nível 19 | 52% | 68% |

| Bronzes contra um Ouro do mesmo nível | Sem aliado | Com um aliado |
|---|---:|---:|
| 3 Bronzes, nível 15 | 27% | 35% |
| 4 Bronzes, nível 15 | 59% | 67% |
| 3 Bronzes, nível 20 | 10% | 16% |
| 4 Bronzes, nível 20 | 43% | 48% |

| Quatro Bronzes contra um Ouro do mesmo nível | Vence | Caem | Rodadas |
|---|---:|---:|---:|
| Nível 15 | 64% | 2.3 | 7.8 |
| Nível 17 | 47% | 2.7 | 8.7 |
| Nível 20 | 42% | 2.9 | 10.8 |

## As fichas prontas

| Ficha | Quem enfrenta | Vence | Caem |
|---|---|---:|---:|
| Cavaleiro Negro | Um Bronze de nível 1 | 58% | — |
| Espectro de Estrela Terrestre | Um Bronze de nível 3 | 64% | — |
| Espectro de Estrela Terrestre | Um Bronze de nível 4 | 78% | — |
| Cavaleiro de Prata | Um Bronze de nível 8 | 6% | — |
| Cavaleiro de Prata | Um Bronze de nível 9 | 11% | — |
| Cavaleiro de Prata | Um Bronze de nível 13 | 86% | — |
| Cavaleiro de Prata | Dois Bronzes de nível 9 | 60% | 1.2 |
| Cavaleiro de Prata | Três Bronzes de nível 9 | 96% | 0.9 |
| Guerreiro Deus | Quatro Bronzes de nível 12 | 15% | 3.7 |
| Guerreiro Deus | Quatro Bronzes de nível 15 | 70% | 2.0 |
| General Marina | Quatro Bronzes de nível 15 | 65% | 2.2 |
| Cavaleiro de Ouro | Um Bronze de nível 16 | 0% | — |
| Cavaleiro de Ouro | Quatro Bronzes de nível 15 | 48% | 2.8 |
| Cavaleiro de Ouro | Cinco Bronzes de nível 15 | 77% | 2.2 |
| Juiz do Inferno | Quatro Bronzes de nível 17 | 54% | 2.6 |
| Juiz do Inferno | Quatro Bronzes de nível 18 | 66% | 2.3 |

| Espectros juntos contra um Bronze | O Bronze vence |
|---|---:|
| 2 Espectros contra um Bronze de nível 3 | 5% |
| 2 Espectros contra um Bronze de nível 4 | 14% |
| 3 Espectros contra um Bronze de nível 4 | 2% |
| 3 Espectros contra um Bronze de nível 5 | 20% |

## Antes do Sexto Sentido: a prova da armadura

Dois aprendizes do mesmo nível humano (FOR ou DES 12 e CON 11, que viram 15 e 14 ao despertar) num duelo. Quem cai gasta a Convicção e levanta — humano, ou desperto.

| Nível humano | PV | Golpe | Rodadas, sem despertar | Rodadas, despertando | Alguém desperta | Os dois despertam |
|---:|---:|---|---:|---:|---:|---:|
| 3 | 8 | 1d6 + 1 | 4.1 | 4.1 | 100% | 84% |
| 4 | 10 | 1d6 + 1 | 4.6 | 4.6 | 100% | 85% |

Diante de um desperto, o humano é figurante: a linha do nível 1 da tabela de figurantes, na seção acima.
