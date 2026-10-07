# As ferramentas do Mestre, medidas

Gerado por `python sim/mestre.py`. 800 duelos por célula (400 nas lutas de grupo, 2000 nos bandos), sementes fixas. O personagem tem três Convicções e levanta no máximo uma vez por luta.

## Quanto pesa um inimigo

| Dificuldade | Inimigo | O personagem vence |
|---|---|---:|
| Fácil | Nomeado sem Convicção, do mesmo nível ou um acima | 56% a 97% |
| Justa | Mesmo nível e mesmo Posto, com três Convicções, como o personagem | 48% a 52% |
| Difícil | Rival um nível acima, com uma Convicção | 12% a 35% |
| Muito difícil | Rival dois níveis acima, com uma Convicção | 4% a 23% |
| Muito difícil | Um Prata do mesmo nível com uma Convicção, contra um Bronze | 6% a 12% |
| Mortal | Elite do mesmo nível, contra um Bronze ou um Prata | 0% |
| Mortal, mas possível | Elite três níveis abaixo do personagem (a partir do nível 18) | 0% a 5% |

| Nomeado sem Convicção um nível acima do personagem | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| O inimigo vence | 44% | 29% | 34% | 33% | 19% | 14% | 17% | 26% | 34% | 23% | 21% | 34% | 36% | 19% | 10% | 18% | 10% | 10% | 12% |

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

## O grupo contra um nomeado acima do nível dele

Personagens do mesmo nível contra um nomeado sem Convicção alguns níveis acima. Sem Convicção, ele não usa Sozinho contra muitos. Cada célula: quanto o grupo vence / quantos personagens caem, em média.

| Nível do grupo | 2 contra +2 | 2 contra +3 | 2 contra +4 | 3 contra +2 | 3 contra +3 | 3 contra +4 |
|---:|---|---|---|---|---|---|
| 1 | 97% / 0.4 | 88% / 0.7 | 89% / 0.7 | 100% / 0.4 | 99% / 0.5 | 100% / 0.5 |
| 3 | 97% / 0.4 | 86% / 0.8 | 75% / 1.0 | 100% / 0.3 | 100% / 0.5 | 99% / 0.8 |
| 5 | 100% / 0.2 | 99% / 0.3 | 95% / 0.6 | 100% / 0.2 | 100% / 0.2 | 100% / 0.4 |
| 9 | 100% / 0.2 | 100% / 0.2 | 98% / 0.4 | 100% / 0.1 | 100% / 0.1 | 100% / 0.2 |
| 13 | 100% / 0.1 | 100% / 0.1 | 100% / 0.2 | 100% / 0.0 | 100% / 0.0 | 100% / 0.1 |

## A armadura de Ouro emprestada

Um Bronze de armadura de Ouro emprestada: a linha do Ouro na tabela de Posto, três características, a Resistência da CON e da Vida, e nada das formas da armadura dele. A Hierarquia e o Sétimo continuam os do Bronze.

| Nível | Contra um Bronze (3 Convicções) | Contra um Prata (1) | Contra um Ouro (2) |
|---:|---|---|---|
| 5 | 50% → 80% | — | — |
| 9 | 50% → 84% | 11% → 44% | — |
| 13 | 52% → 84% | 12% → 42% | — |
| 17 | 48% → 86% | 7% → 40% | 0% → 1% |

| Quatro Bronzes contra um Ouro do mesmo nível | Sem | Um de armadura emprestada |
|---|---:|---:|
| Nível 15 | 66% | 73% |
| Nível 20 | 40% | 50% |

| Armadura de Prata emprestada, contra um Bronze do mesmo nível | Sem | Com |
|---|---:|---:|
| Nível 5 | 50% | 66% |
| Nível 9 | 50% | 66% |
| Nível 13 | 52% | 69% |
| Nível 17 | 49% | 69% |

## Os deuses

Personagens de nível 20 no Nono, com a armadura na forma Divina, contra um deus: a elite de nível 20 no Nono, com os PV multiplicados e a DEF somada (menor: × 1.5 e +2; maior: × 2 e +4). Só o combate: os efeitos de destino ficam de fora. Cada célula: quanto vencem / rodadas / quantos caem.

| Contra | Um Bronze | Um Ouro | Dois Bronzes | Três Bronzes |
|---|---|---|---|---|
| Deus menor | 78% / 18 / 0.2 | 85% / 17 / 0.2 | 99% / 8 / 0.1 | 100% / 5 / 0.0 |
| Deus maior | 25% / 22 / 0.7 | 40% / 22 / 0.6 | 80% / 15 / 0.7 | 100% / 9 / 0.2 |
| Deus menor, no Nono sem elo (sem a Divina, 0.25.0) | 0% / 6 / 1.0 | 1% / 7 / 1.0 | 3% / 7 / 2.0 | 47% / 8 / 2.0 |
| Deus maior, no Nono sem elo (sem a Divina, 0.25.0) | 0% / 5 / 1.0 | 0% / 7 / 1.0 | 0% / 6 / 2.0 | 2% / 9 / 3.0 |

Fora do Nono, só uma fração do dano entra na divindade menor (25% no Sétimo, 50% com o Oitavo); no deus maior, nada. Ouros de nível 20 no Sétimo, revividos seis vezes:

| Contra a divindade menor | Um | Três | Cinco |
|---|---|---|---|
| Só o Sétimo | 0% / 1.0 caem | 0% / 3.0 caem | 0% / 5.0 caem |
| Com o Oitavo | 0% / 1.0 caem | 0% / 3.0 caem | 6% / 4.9 caem |

O semideus (0.23.0): a elite de nível 20 no Sétimo, com os PV × 2 e +2 na DEF. Do Sexto entra 25% do dano, do Sétimo 50%, com o Oitavo 100%. Os acertos de técnica dele tiram o Grau de Resistência; os da divindade menor despedaçam a armadura, e os do deus maior, qualquer acerto. A armadura Divina perde só 1.

| Contra o semideus | Um | Três | Cinco |
|---|---|---|---|
| Só o Sétimo | 0% / 11 rodadas / 1.0 caem | 62% / 11 rodadas / 1.8 caem | 100% / 6 rodadas / 0.5 caem |
| Com o Oitavo | 1% / 11 rodadas / 1.0 caem | 88% / 8 rodadas / 0.9 caem | 100% / 4 rodadas / 0.1 caem |

Ao lado do próprio deus, quem está no Sétimo fere um deus normalmente. Ouros de nível 20 no Sétimo, ferindo por inteiro:

| Ao lado do próprio deus | Um | Três | Cinco |
|---|---|---|---|
| Contra o deus menor | 1% / 1.0 caem | 52% / 1.9 caem | 98% / 0.6 caem |
| Contra o deus maior | 0% / 1.0 caem | 2% / 3.0 caem | 40% / 3.7 caem |

Ao lado do próprio deus que só protege, o Cosmo dele cobre as armaduras: contra a quebra divina, perdem só 1 (0.23.1). Se o deus de vocês luta junto, ele está num corpo humano e usa a linha da divindade menor, sem Resposta ao turno dele, e não cobre mais as armaduras; entre deuses, ninguém despedaça a armadura do outro:

| Com o seu deus lutando | Só ele | Mais um Ouro | Mais três | Mais cinco |
|---|---|---|---|---|
| Contra o deus menor | 47% / 20 rodadas | 74% / 21 rodadas | 95% / 13 rodadas | 99% / 8 rodadas |
| Contra o deus maior | 13% / 24 rodadas | 28% / 28 rodadas | 46% / 27 rodadas | 61% / 25 rodadas |

## O sangue doado

Um Bronze que doou sangue contra um Bronze inteiro do mesmo nível, os dois com três Convicções. Cada terço doado tira um terço dos PV máximos.

| Terços doados | 1 | 5 | 9 | 13 | 17 | 20 |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 52% | 50% | 53% | 48% | 47% | 49% |
| 1 | 40% | 31% | 28% | 23% | 11% | 9% |
| 2 | 34% | 17% | 11% | 9% | 4% | 2% |

## A armadura que se sacrifica (regra opcional)

No último ponto de Resistência, quando a metade do dano ainda derrubaria, a armadura segura o golpe inteiro e morre. Sem e com a regra, contra um Bronze inteiro do mesmo nível.

| Começa a luta com | 1 | 5 | 9 | 13 | 17 | 20 |
|---|---:|---:|---:|---:|---:|---:|
| a Resistência cheia | 51% → 51% | 47% → 47% | 49% → 49% | 52% → 52% | 48% → 48% | 49% → 49% |
| Resistência 2 | 47% → 64% | 44% → 65% | 42% → 42% | 17% → 17% | 8% → 8% | 4% → 4% |
| Resistência 1 | 38% → 49% | 39% → 38% | 20% → 20% | 17% → 17% | 3% → 3% | 4% → 4% |

## Os que Hades traz de volta

Três Bronzes (personagens ou companheiros) contra um Prata de nível 9: vivo, com uma Convicção, e corrompido, sem nenhuma. Cada célula: quanto vencem / quantos caem.

| Nível dos três | Contra o Prata vivo | Contra o corrompido |
|---:|---|---|
| 4 | 0% / 3.0 | 63% / 2.0 |
| 5 | 17% / 2.8 | 97% / 1.0 |
| 7 | 79% / 1.6 | 100% / 0.4 |
| 9 | 94% / 1.0 | 100% / 0.1 |

## Os golpes famosos

Montados com as peças novas do motor como Golpe do Assento, no lugar do comum. Duelo: um Ouro de nível 16 com o golpe contra outro com o Assento comum. Chefe: quanto quatro Bronzes de nível 15 vencem o Ouro com o golpe.

| Golpe | Tamanho · custo | Duelo | Quatro Bronzes vencem |
|---|---|---:|---:|
| Golpe do Assento comum | 7 · 7 | 48% | 62% |
| Agulha Escarlate | 6 · 6 | 34% | 64% |
| Caixão de Gelo | 6 · 5 | 38% | 54% |
| Ondas do Inferno | 7 · 6 | 30% | 68% |
| Muralha de Cristal | 5 · 4 | 58% | 61% |

## Vários contra vários

O grupo concentra os golpes no inimigo mais ferido; cada inimigo bate no personagem mais ferido. Sem a resposta de Sozinho contra muitos. Cada célula: quanto o grupo vence, para 2, 3 e 4 personagens.

| Inimigos | Nível 3 | Nível 9 | Nível 15 |
|---|---|---|---|
| Nomeados, tantos quanto os personagens, do mesmo nível | 95% · 93% · 96% | 95% · 95% · 98% | 100% · 99% · 99% |
| Nomeados, um a mais que os personagens, do mesmo nível | 47% · 73% · 78% | 45% · 65% · 82% | 45% · 79% · 95% |
| Nomeados, tantos quanto, dois níveis acima | 56% · 70% · 74% | 64% · 65% · 66% | 71% · 87% · 82% |
| Nomeados, tantos quanto, três níveis acima | 21% · 22% · 16% | 48% · 47% · 42% | 42% · 56% · 63% |
| Rivais (uma Convicção), um a menos que os personagens | 97% · 95% · 90% | 100% · 95% · 93% | 100% · 100% · 99% |
| Rivais, tantos quanto os personagens | 48% · 48% · 51% | 46% · 51% · 48% | 49% · 54% · 47% |
| Rivais, tantos quanto, um nível acima | 27% · 27% · 26% | 21% · 14% · 7% | 33% · 27% · 35% |
| Rivais, um a mais que os personagens | 5% · 10% · 12% | 1% · 7% · 11% | 1% · 2% · 5% |

## O milagre

Um Bronze sozinho contra um Ouro do mesmo nível, os dois com três Convicções: sem e com a Centelha do deus quando ele levanta.

| Nível | Sem | Com o milagre |
|---:|---:|---:|
| 15 | 0% | 9% |
| 17 | 0% | 7% |
| 20 | 0% | 4% |

## O Cosmo de uma luta para a outra

Sem descanso longo, a luta seguinte começa com o Cosmo que sobrou. Um Bronze contra outro descansado, os dois com três Convicções.

| Chega com | 1 | 5 | 9 | 13 | 17 | 20 |
|---|---:|---:|---:|---:|---:|---:|
| O Cosmo inicial | 53% | 53% | 50% | 50% | 45% | 49% |
| O Cosmo no Teto | 56% | 56% | 52% | 50% | 45% | 49% |
| O Cosmo no piso | 48% | 46% | 45% | 39% | 50% | 51% |

## O aliado de luta

Metade do nível do grupo, metade dos PV, sem Convicção; não conta para Sozinho contra muitos.

| Contra um rival do mesmo nível, com uma Convicção | Sozinho | Com o aliado |
|---|---:|---:|
| Nível 3 | 51% | 78% |
| Nível 7 | 49% | 72% |
| Nível 11 | 48% | 72% |
| Nível 15 | 51% | 70% |
| Nível 19 | 52% | 67% |

| Bronzes contra um Ouro do mesmo nível | Sem aliado | Com um aliado |
|---|---:|---:|
| 3 Bronzes, nível 15 | 27% | 35% |
| 4 Bronzes, nível 15 | 59% | 67% |
| 3 Bronzes, nível 20 | 10% | 12% |
| 4 Bronzes, nível 20 | 43% | 44% |

| Quatro Bronzes contra um Ouro do mesmo nível | Vence | Caem | Rodadas |
|---|---:|---:|---:|
| Nível 15 | 64% | 2.3 | 7.8 |
| Nível 17 | 47% | 2.7 | 8.7 |
| Nível 20 | 42% | 2.9 | 10.8 |

## As fichas prontas

| Ficha | Quem enfrenta | Vence | Caem |
|---|---|---:|---:|
| Cavaleiro Negro | Um Bronze de nível 1 | 58% | — |
| Espectro Novato | Um Bronze de nível 1 | 46% | — |
| Espectro Novato | Um Bronze de nível 2 | 67% | — |
| Espectro Novato | Dois Bronzes de nível 1 | 99% | 0.3 |
| Espectro Novato | Três Bronzes de nível 1 | 100% | 0.4 |
| Espectro de Estrela Terrestre | Um Bronze de nível 3 | 65% | — |
| Espectro de Estrela Terrestre | Um Bronze de nível 4 | 76% | — |
| Cavaleiro de Prata | Um Bronze de nível 8 | 6% | — |
| Cavaleiro de Prata | Um Bronze de nível 9 | 11% | — |
| Cavaleiro de Prata | Um Bronze de nível 13 | 88% | — |
| Cavaleiro de Prata | Dois Bronzes de nível 9 | 58% | 1.2 |
| Cavaleiro de Prata | Três Bronzes de nível 9 | 94% | 0.9 |
| Espectro de Estrela Celeste | Um Bronze de nível 11 | 15% | — |
| Espectro de Estrela Celeste | Um Bronze de nível 13 | 63% | — |
| Espectro de Estrela Celeste | Dois Bronzes de nível 11 | 69% | 1.1 |
| Espectro de Estrela Celeste | Três Bronzes de nível 9 | 72% | 1.7 |
| Espectro de Estrela Celeste | Três Bronzes de nível 11 | 95% | 0.7 |
| Comandante sem armadura | Um Bronze de nível 5 | 27% | — |
| Comandante sem armadura | Um Bronze de nível 9 | 85% | — |
| Comandante sem armadura | Três Bronzes de nível 5 | 98% | 0.9 |
| Satélite de Ártemis | Um Bronze de nível 6 | 50% | — |
| Satélite de Ártemis | Dois Bronzes de nível 5 | 80% | 0.9 |
| Palasita de Terceira Classe | Um Bronze de nível 7 | 55% | — |
| Palasita de Terceira Classe | Um Bronze de nível 6 | 39% | — |
| Marciano | Um Bronze de nível 10 | 11% | — |
| Marciano | Três Bronzes de nível 9 | 72% | 1.7 |
| Cavaleiro da Coroa | Um Bronze de nível 13 | 10% | — |
| Cavaleiro da Coroa | Três Bronzes de nível 12 | 84% | 1.4 |
| Anjo Caído | Um Bronze de nível 14 | 12% | — |
| Anjo Caído | Três Bronzes de nível 13 | 82% | 1.4 |
| Cavaleiro Fantasma | Um Bronze de nível 16 | 4% | — |
| Cavaleiro Fantasma | Três Bronzes de nível 15 | 100% | 0.6 |
| Titã meio desperto | Quatro Bronzes de nível 17 | 26% | 3.4 |
| Titã meio desperto | Cinco Bronzes de nível 17 | 64% | 2.9 |
| Guerreiro Deus | Quatro Bronzes de nível 12 | 10% | 3.8 |
| Guerreiro Deus | Quatro Bronzes de nível 15 | 68% | 2.1 |
| General Marina | Quatro Bronzes de nível 15 | 60% | 2.3 |
| Cavaleiro de Ouro | Um Bronze de nível 16 | 0% | — |
| Cavaleiro de Ouro | Quatro Bronzes de nível 15 | 52% | 2.7 |
| Cavaleiro de Ouro | Cinco Bronzes de nível 15 | 82% | 2.1 |
| Juiz do Inferno | Quatro Bronzes de nível 17 | 56% | 2.6 |
| Juiz do Inferno | Quatro Bronzes de nível 18 | 64% | 2.3 |

| Espectros juntos contra um Bronze | O Bronze vence |
|---|---:|
| 2 Espectros contra um Bronze de nível 3 | 5% |
| 2 Espectros contra um Bronze de nível 4 | 14% |
| 3 Espectros contra um Bronze de nível 4 | 2% |
| 3 Espectros contra um Bronze de nível 5 | 20% |
| 2 Espectros Novatos contra um Bronze de nível 2 | 11% |
| 2 Espectros Novatos contra um Bronze de nível 3 | 21% |
| 2 Espectros Novatos contra um Bronze de nível 4 | 33% |

## Antes do Sexto Sentido: a prova da armadura

Dois aprendizes do mesmo nível humano (FOR ou DES 12 e CON 11, que viram 15 e 14 ao despertar) num duelo. Quem cai gasta a Convicção e levanta — humano, ou desperto.

| Nível humano | PV | Golpe | Rodadas, sem despertar | Rodadas, despertando | Alguém desperta | Os dois despertam |
|---:|---:|---|---:|---:|---:|---:|
| 3 | 8 | 1d6 + 1 | 4.1 | 4.1 | 100% | 84% |
| 4 | 10 | 1d6 + 1 | 4.6 | 4.6 | 100% | 85% |

Diante de um desperto, o humano é figurante: a linha do nível 1 da tabela de figurantes, na seção acima.
