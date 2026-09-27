# As ferramentas do Mestre, medidas

Gerado por `python sim/mestre.py`. 800 duelos por célula (400 nas lutas de grupo, 2000 nos bandos), sementes fixas. O personagem tem três Convicções e levanta no máximo uma vez por luta.

## Quanto pesa um inimigo

| Dificuldade | Inimigo | O personagem vence |
|---|---|---:|
| Fácil | Nomeado sem Convicção, do mesmo nível ou um acima | 64% a 99% |
| Justa | Mesmo nível e mesmo Posto, com três Convicções, como o personagem | 48% a 52% |
| Difícil | Rival um nível acima, com uma Convicção | 12% a 35% |
| Muito difícil | Rival dois níveis acima, com uma Convicção | 4% a 24% |
| Muito difícil | Um Prata do mesmo nível com uma Convicção, contra um Bronze | 6% a 12% |
| Mortal | Elite do mesmo nível, contra um Bronze ou um Prata | 0% |
| Mortal, mas possível | Elite três níveis abaixo do personagem (a partir do nível 18) | 0% a 5% |

| Nomeado sem Convicção um nível acima do personagem | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| O inimigo vence | 18% | 9% | 11% | 12% | 19% | 15% | 17% | 26% | 34% | 23% | 21% | 34% | 36% | 19% | 8% | 5% | 3% | 3% | 1% |

| A fronteira do Posto | O personagem vence |
|---|---:|
| Bronze de nível 8 contra Prata de nível 9, uma Convicção | 6% |
| Bronze de nível 9 contra Prata de nível 9, uma Convicção | 10% |
| Bronze de nível 14 contra elite de nível 15 | 0% |
| Prata de nível 14 contra elite de nível 15 | 0% |

## Figurantes

Um personagem sozinho contra um bando da tabela. O golpe comum que acerta derruba 2; a técnica de alvo único, 3; a de área, o bando inteiro.

| Nível | DEF · ataque · dano | Seis, sem área | Seis, com área | Dez, sem área |
|---:|---|---|---|---|
| 1 | 11 · +4 · 2 | 4.0 rodadas, 28% dos PV | 1.8 rodadas, 13% dos PV | 5.7 rodadas, 47% dos PV, cai 2% |
| 2 | 11 · +4 · 3 | 4.0 rodadas, 29% dos PV | 1.8 rodadas, 13% dos PV | 5.7 rodadas, 49% dos PV, cai 2% |
| 3 | 12 · +4 · 4 | 3.8 rodadas, 27% dos PV | 1.7 rodadas, 12% dos PV | 6.1 rodadas, 53% dos PV, cai 4% |
| 4 | 12 · +4 · 6 | 3.8 rodadas, 30% dos PV, cai 1% | 1.7 rodadas, 14% dos PV | 6.1 rodadas, 57% dos PV, cai 8% |
| 5 | 12 · +5 · 7 | 2.9 rodadas, 22% dos PV | 1.4 rodadas, 11% dos PV | 5.7 rodadas, 52% dos PV, cai 2% |
| 6 | 13 · +5 · 9 | 2.9 rodadas, 20% dos PV | 1.4 rodadas, 10% dos PV | 5.8 rodadas, 51% dos PV, cai 3% |
| 7 | 13 · +5 · 11 | 2.9 rodadas, 21% dos PV | 1.4 rodadas, 10% dos PV | 5.7 rodadas, 51% dos PV, cai 2% |
| 8 | 13 · +5 · 13 | 2.9 rodadas, 20% dos PV | 1.4 rodadas, 10% dos PV | 5.6 rodadas, 50% dos PV, cai 2% |
| 9 | 14 · +6 · 15 | 2.5 rodadas, 19% dos PV | 1.4 rodadas, 10% dos PV | 3.8 rodadas, 34% dos PV |
| 10 | 14 · +6 · 17 | 2.3 rodadas, 16% dos PV | 1.3 rodadas, 8% dos PV | 3.6 rodadas, 29% dos PV |
| 11 | 14 · +6 · 20 | 2.3 rodadas, 16% dos PV | 1.3 rodadas, 8% dos PV | 3.6 rodadas, 30% dos PV |
| 12 | 15 · +6 · 23 | 2.4 rodadas, 18% dos PV | 1.4 rodadas, 10% dos PV | 3.8 rodadas, 32% dos PV |
| 13 | 15 · +7 · 26 | 2.3 rodadas, 17% dos PV | 1.3 rodadas, 9% dos PV | 3.6 rodadas, 32% dos PV |
| 14 | 15 · +7 · 29 | 2.2 rodadas, 15% dos PV | 1.3 rodadas, 8% dos PV | 3.4 rodadas, 28% dos PV |
| 15 | 16 · +7 · 32 | 2.3 rodadas, 16% dos PV | 1.3 rodadas, 8% dos PV | 3.6 rodadas, 29% dos PV |
| 16 | 16 · +7 · 36 | 2.3 rodadas, 16% dos PV | 1.3 rodadas, 9% dos PV | 3.6 rodadas, 30% dos PV |
| 17 | 16 · +8 · 40 | 2.2 rodadas, 16% dos PV | 1.2 rodadas, 8% dos PV | 3.4 rodadas, 29% dos PV |
| 18 | 17 · +8 · 44 | 2.3 rodadas, 16% dos PV | 1.3 rodadas, 9% dos PV | 3.6 rodadas, 30% dos PV |
| 19 | 17 · +8 · 48 | 2.3 rodadas, 16% dos PV | 1.3 rodadas, 9% dos PV | 3.6 rodadas, 30% dos PV |
| 20 | 17 · +8 · 52 | 2.3 rodadas, 16% dos PV | 1.4 rodadas, 9% dos PV | 3.6 rodadas, 30% dos PV |

## O aliado de luta

Metade do nível do grupo, metade dos PV, sem Convicção; não conta para Sozinho contra muitos.

| Contra um rival do mesmo nível, com uma Convicção | Sozinho | Com o aliado |
|---|---:|---:|
| Nível 3 | 52% | 72% |
| Nível 7 | 49% | 72% |
| Nível 11 | 48% | 72% |
| Nível 15 | 51% | 70% |
| Nível 19 | 52% | 68% |

| Bronzes contra um Ouro do mesmo nível | Sem aliado | Com um aliado |
|---|---:|---:|
| 3 Bronzes, nível 15 | 19% | 32% |
| 4 Bronzes, nível 15 | 45% | 60% |
| 3 Bronzes, nível 20 | 23% | 34% |
| 4 Bronzes, nível 20 | 62% | 72% |

| Quatro Bronzes contra um Ouro do mesmo nível | Vence | Caem | Rodadas |
|---|---:|---:|---:|
| Nível 15 | 50% | 3.0 | 12.8 |
| Nível 17 | 37% | 3.3 | 15.4 |
| Nível 20 | 64% | 2.8 | 17.6 |

## As fichas prontas

| Ficha | Quem enfrenta | Vence | Caem |
|---|---|---:|---:|
| Cavaleiro Negro | Um Bronze de nível 1 | 85% | — |
| Espectro de Estrela Terrestre | Um Bronze de nível 3 | 87% | — |
| Espectro de Estrela Terrestre | Um Bronze de nível 4 | 91% | — |
| Cavaleiro de Prata | Um Bronze de nível 8 | 6% | — |
| Cavaleiro de Prata | Um Bronze de nível 9 | 11% | — |
| Cavaleiro de Prata | Um Bronze de nível 13 | 86% | — |
| Cavaleiro de Prata | Dois Bronzes de nível 9 | 71% | 1.0 |
| Cavaleiro de Prata | Três Bronzes de nível 9 | 86% | 1.5 |
| Guerreiro Deus | Quatro Bronzes de nível 12 | 3% | 4.0 |
| Guerreiro Deus | Quatro Bronzes de nível 15 | 66% | 2.6 |
| General Marina | Quatro Bronzes de nível 15 | 49% | 3.0 |
| Cavaleiro de Ouro | Um Bronze de nível 16 | 0% | — |
| Cavaleiro de Ouro | Quatro Bronzes de nível 15 | 34% | 3.4 |
| Cavaleiro de Ouro | Cinco Bronzes de nível 15 | 58% | 3.6 |
| Juiz do Inferno | Quatro Bronzes de nível 17 | 47% | 3.1 |
| Juiz do Inferno | Quatro Bronzes de nível 18 | 66% | 2.7 |

| Espectros juntos contra um Bronze | O Bronze vence |
|---|---:|
| 2 Espectros contra um Bronze de nível 3 | 28% |
| 2 Espectros contra um Bronze de nível 4 | 45% |
| 3 Espectros contra um Bronze de nível 4 | 9% |
| 3 Espectros contra um Bronze de nível 5 | 21% |
