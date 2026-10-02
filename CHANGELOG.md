# Changelog

Todas as mudanças que alteram regra ou número ficam registradas aqui. O número
de versão do livro e do site sai da primeira linha `## [x.y.z]` deste arquivo.

## [0.10.0] - 2026-09-29

O primeiro playtest de campanha (um jogador, com o ChatGPT como Mestre, do humano de
nível 1 ao Bronze de nível 4) está em `regras/playtest-01.md`. Esta versão muda o que ele
achou de mais pesado e esclarece o que ele achou de ambíguo.

### Mudado

- **O primeiro Sétimo é um marco** (Capítulos Quatro e Cinco, decisão do usuário): o Bronze
  e o Prata só alcançam o Sétimo do nível 5 em diante, e a primeira vez vem numa luta que
  importa — contra alguém de Posto acima ou um nomeado com Convicção. Depois dela, vale a
  regra de sempre. No playtest, o Bronze de nível 1 levantou na primeira luta séria e, pela
  regra, despertou; no nível 1 o Teto é 5 e queimar um ponto custa 1d4, então o Sétimo virava
  rotina. Medido: nos níveis 1 a 4 o personagem ficou mais fraco contra quem está acima (o
  Cavaleiro Negro de nível 2 contra um Bronze de nível 1: de 84% para 58%; dois Espectros de
  nível 4 contra um de nível 3: de 28% para 5%), e apareceu um salto no nível 5 (quem chegou
  nele vence 88% contra quem está no 4; antes, 63%). As fichas prontas e a tabela de
  dificuldade dizem os números novos.
- **Figurante não racha armadura** (Capítulos Cinco, Sete e Dez): o dano do bando não se
  apara, e o ataque dele não tem crítico — o 20 natural acerta, mas não derruba o Elmo. No
  playtest, cinco dos seis pontos de Resistência da armadura foram gastos aparando golpes de
  3 de dano. O simulador sempre mediu o bando assim: nenhum número muda.
- **A área derruba até seis figurantes** (Capítulos Cinco e Dez). Antes, o bando inteiro; no
  playtest, uma técnica de tamanho 3 apagou uns quinze bandos, de até doze soldados. Medido:
  doze figurantes, com técnica em área, custam de 2,5 a 4,2 rodadas e de 21% a 38% dos PV.
- **Levantar só quando faz sentido** (Capítulo Cinco, pedido do usuário): a Convicção é um
  motivo, não um botão. Quem está Dominado ou sob controle da mente, Selado, Petrificado ou no
  sono de um veneno não levanta; numa luta que não toca nenhuma Convicção, o Mestre avisa
  antes. O simulador não tem essas condições: nenhum número muda.
- **Restaurar não espera o Interlúdio** (Capítulos Sete, Oito e Doze, pedido do usuário):
  leva os dias do trabalho (um por Versão), e a armadura pode voltar no meio da missão. Buscar
  o material se conta em dias: Pó de Estrelas 1, Gamânio 3, Oricalco 7, item raro 3.
- **O sangue doado, em dias e PV** (Capítulo Sete, pedido do usuário): um terço tira um
  terço dos PV máximos e dá Desvantagem nos testes de FOR e CON; dois terços derrubam por
  um dia; um terço volta a cada 3 dias (antes, uma semana de Interlúdio). Medido contra um
  Bronze inteiro do mesmo nível: 40% no nível 1, 23% no 13 e 9% no 20 com um terço doado.
- **O Interlúdio se conta em dias** (Capítulo Doze): cada ação tem a sua duração; uma
  Convicção volta a cada 7 dias sem luta. Uma campanha que não para ainda tem Interlúdio.
- **A técnica nova pode nascer numa luta** (Capítulo Seis): quando você levanta, a técnica
  escolhida ao subir de nível nasce ali, sem teste, como a assinatura na prova.

### Adicionado

- **Surpresa: o golpe de abertura** (Capítulo Cinco): quem pega o outro sem ser percebido dá
  um golpe comum antes da Iniciativa, com Vantagem, e o alvo fica sem reação até o primeiro
  turno dele. Sem surpresa, o primeiro soco sai na ordem da Iniciativa. No playtest, oito
  lutas começaram com um golpe fora da Iniciativa, que virava uma ação a mais. Medido num
  espelho: 52% a 66% para quem surpreende (uma ação inteira, com técnica, dava 60% a 81%).
- **Reações sem travar a mesa** (Capítulo Onze): diga a CD ou a DEF antes do dado, pare antes
  de resolver quando o alvo tem reação, e deixe o jogador declarar a guarda da rodada (alta,
  bloqueia; baixa, guarda para aparar). Grito não é declaração de queimar. Feche a ficha de
  todo nomeado antes da luta.
- **A armadura de Ouro emprestada** (Capítulo Sete, pedido do usuário): por uma luta, para
  quem já despertou o Sétimo; dá a linha do Ouro, o acessório e as três características dela,
  e não dá as formas da sua armadura, o Golpe do Assento nem o Sétimo dominado. Ela não morre
  no corpo de quem a pegou. Medido: um Bronze com ela vence 80% a 86% contra um Bronze do
  mesmo nível, uns 40% contra um Prata (antes, uns 10%) e continua com 1% contra um Ouro.
- **Feitos do corpo e perigos** (Capítulo Dois, pedido do usuário): todo feito tem um degrau
  (de gente, de guerreiro, de Sétimo, de deus); abaixo do seu, sem rolar; no seu, CD 13 ou
  16; um acima, CD 22. Teste de CON, fôlego, queda, desabamento, fogo, frio e água, com o
  dano em acertos de bando do seu nível.
- **Veneno e doença** (Capítulo Cinco): um relógio de 6 segmentos, um teste de CON por
  manhã, Medicina segura, a cura apaga.
- **Um jogador só** (Capítulo Onze): o aliado de Posto acima fica com outro inimigo e no
  máximo manda Centelha; se dividir a luta, ela não dá Glória. Centelha para a luta de um
  personagem do Mestre não dá Glória.
- **Fichas novas** (Capítulo Dez): o Aprendiz rival (humano de nível 3), o Espectro Novato
  (nível 3) e o Espectro de Estrela Celeste (o Prata de Hades, nível 11). Mais um molde curto
  para ameaças que não são guerreiros, com um exemplo, e o grupo contra um nomeado acima do
  nível dele (vence de 75% a 100%, mas nos níveis 1 a 3 alguém costuma cair).
- **A prova em torneio e a faísca** (Capítulo Três).
- **Regra opcional: a armadura que se sacrifica** (Capítulo Sete): no último ponto de
  Resistência, ela segura o golpe inteiro e morre. Medido: numa luta comum, nada muda; com a
  armadura gasta de uma luta anterior, de 47% para 64% no nível 1; do 9 em diante, quase
  nunca aparece.
- `sim/mestre.py` mede a surpresa, o bando de doze, o grupo contra um nomeado acima, a
  armadura emprestada, o sangue doado e o sacrifício; `test.py` confere o nível do primeiro
  Sétimo, o golpe de abertura, o limite da área e as fichas e regras novas.

### Corrigido

- **O piso e a vida paga** (Capítulo Quatro): o livro dizia que o que a técnica custaria
  abaixo do piso "sai de graça", o que fazia a vida nunca pagar. O texto agora diz o que o
  simulador sempre fez: paga-se com o Cosmo que se tem, a diferença sai da vida, e o Cosmo
  para no piso. Com um exemplo.
- Arredondamento: sem regra dizendo para que lado, arredonde para cima (Capítulo Dois).
- Empate de Iniciativa entre um personagem e um bando: o personagem age primeiro.
- Ao subir de nível, os PV atuais sobem junto com os máximos (Capítulo Doze).
- O Elmo volta na luta seguinte (Capítulo Sete).
- Pular degraus na escada do sangue: sangue mais forte serve a qualquer momento, mas os
  degraus pulados se perdem — a armadura sobe uma Versão só, com o bônus do sangue que
  recebeu (como o simulador já fazia).
- Medicina: tratar não exige kit; o kit dá Vantagem e gasta um uso por pessoa.
- Níveis humanos: o Capítulo Três dizia um nível por ano e o Nove, três semanas. Ser
  escolhido já é o nível 2; no mundo, um nível por ano; com um personagem de jogador como
  mestre, três semanas de Interlúdio dedicadas valem um nível.
- O laço da Centelha: os aliados que lutam com você nesta missão contam como companheiros;
  quem manda precisa ter o Cosmo desperto. O Capítulo Onze lembra das Centelhas do Mestre.

## [0.9.4] - 2026-09-28

### Mudado

- **A casca** (Capítulo Sete, pedido do usuário): a armadura morta ainda atende ao chamado
  e ainda se veste. Dá a DEF do Posto (e a guarda) e deixa Bloquear; não tem Resistência,
  então não apara, e não dá características, formas, Elmo, Pernas nem acessório. Um crítico
  a derruba até o fim da luta; ela não morre de novo. Antes, a armadura morta não dava nada.
- Medido: contra um guerreiro do mesmo nível com a armadura viva, quem luta de casca vence
  de 9% a 49%; sem armadura, de 2% a 29%. A folha de consulta rápida (Capítulo Treze) traz
  a regra.

## [0.9.3] - 2026-09-28

### Mudado

- **Os atributos do humano** (Capítulo Três): 12 · 11 · 11 · 10 · 9 · 8, um valor para cada
  atributo (sugestão do usuário). Antes o livro só dizia "entre 8 e 12". Ao despertar, cada
  valor sobe para o do guerreiro na mesma posição: 12→15, os dois 11 viram 14 e 13, 10→12,
  9→10 e o 8 continua 8.
- A prova da armadura foi medida de novo com esses atributos (antes o simulador usava os de
  guerreiro): continua em cerca de 4 rodadas no nível humano 3 e 4,6 no 4, alguém sempre
  desperta, e os dois despertam em 84% das provas (eram 78%).

### Corrigido

- Ambiguidade: a tabela dos humanos escrevia "4 + CON" e "10 + DES" antes de o livro
  explicar o modificador. Agora a seção diz, com um exemplo, que nas contas o atributo é
  sempre o modificador, e a Etapa 3 diz o mesmo para o livro inteiro.

## [0.9.2] - 2026-09-28

### Corrigido

- **O Sétimo dominado nas fichas prontas** (Capítulo Dez): o Guerreiro Deus e o Cavaleiro
  de Ouro diziam "+2 no ataque e na DEF". A regra (Capítulo Quatro) e o simulador sempre
  usaram +3 nos ataques e nas Rolagens de Efeito do elite e −3 nos do recém-despertado;
  agora as quatro fichas de elite dizem isso, com o número tirado da mesma regra.
- A folha de consulta rápida (Capítulo Treze) dizia que só rival e chefe lembram a Técnica
  Lida depois da luta. Quem lembra é quem tem Convicção: personagem, rival e chefe.
- O colofão dizia que luta de grupo contra um inimigo ainda não tinha sido medida. Foi; o
  que falta é mesa.
- O Juiz do Inferno usava o "Grande Chifre do Wyvern"; o Grande Chifre é do Touro. A
  técnica agora é a Grande Cautela, a do Wyvern.

## [0.9.1] - 2026-09-28

### Mudado

- **Os níveis humanos** (Capítulo Três): antes de despertar, o humano tem os níveis dele,
  de 1 a 4. O nível 1 é o humano comum — todo mundo, automaticamente, sem proficiência nem
  Convicção. Do nível 2 em diante, quem tem um mestre é aprendiz: proficiência, as duas
  perícias do treino e uma Convicção. PV 4, 6, 8 e 10 (+ CON); golpe de 1d4, e de 1d6 a
  partir do 3. A prova da armadura pode acontecer a partir do nível 3, e o 4 é o limite do
  corpo humano. Quem desperta recomeça no nível 1 — de guerreiro; a tabela de 1 a 20 não
  muda. Antes, o aprendiz era um "nível 0" só.
- A cadeia de comando (Capítulo Nove) separa o humano (todo mundo) do aprendiz (quem um
  Prata ou um Ouro escolheu). Treinar um aprendiz sobe um nível humano a cada três semanas.
- Medido: a prova dura cerca de 4 rodadas no nível humano 3 e 4,5 no 4.

## [0.9.0] - 2026-09-28

### Adicionado

- **Antes do Sexto Sentido** (Capítulo Três): o status base de quem ainda é humano — o
  aprendiz, nível 0 — ao lado do desperto: 4 + CON de PV, DEF 10 + DES, golpe de
  1d4, defesas 10 + atributo, sem Cosmo nem técnica, uma Convicção. Gente
  comum usa a mesma coluna. Diante de um desperto, o humano é figurante.
- **A prova da armadura**: na prova, quem cai e levanta com a Convicção levanta desperto
  (um quarto dos PV do nível 1, Cosmo no Teto, a técnica assinatura). Medido: 3 a 4
  rodadas, alguém sempre desperta, e em quatro de cada cinco os dois despertam.
- **A cadeia de comando** (Capítulo Nove): aprendiz, Bronze, Prata, Ouro, o líder e o
  deus. Só Prata ou acima treina aprendiz; o Bronze responde a um Prata, o Prata a um Ouro,
  o Ouro ao líder (o Grande Mestre, o Dragão Marinho, Pandora, Hilda de Polaris) e o líder
  ao deus. A missão desce a escada.
- A etapa de Treino (Capítulo Três) pede um mestre de Posto acima do seu; o Interlúdio
  ganhou "Treinar um aprendiz"; o Mentor (Capítulo Onze) é sempre de Posto acima.

## [0.8.1] - 2026-09-28

### Mudado

- **A Resposta causa só o dano** (Capítulo Dez): condições e outros efeitos comprados da
  técnica não vêm junto, a não ser que a ficha do chefe diga que fazem parte da Resposta.
  Sem isso, um Lento ou um Caído na técnica mais barata sairia uma vez depois de cada
  personagem, de graça. "Montar um inimigo" ganhou o passo da Resposta, e as fichas prontas
  com Convicção trazem a Resposta escrita.

### Corrigido

- As contas finais da criação (Capítulo Três) ainda davam a Resistência antiga: agora é a
  do Posto, +1 sem acessório, + o modificador de CON, e depois Vida, formas e melhorias.

## [0.8.0] - 2026-09-28

Uma leitura crítica do livro apontou três coisas para atacar antes de chamar o sistema de
fechado: a FOR e a CON valiam menos que a DES e o Cosmo, a Técnica Lida pesava na ficha, e a
luta do grupo contra a elite era longa demais para a mesa. As três mudaram.

### Mudado

- **A guarda** (Capítulos Três e Sete): com a armadura no corpo, a DEF pode usar a FOR ou a
  CON, além da DES e do Atributo do Cosmo. Quem luta pela FOR vence de 44% a 50% contra quem
  luta pela DES (antes, 13% a 51%).
- **Resistência da CON e da Vida**: a Resistência que é sua passa a ser o modificador de CON
  (mínimo 0) e +1 a cada duas escolhas de Vida, no lugar do +1 fixo nos níveis 5, 7, 13 e 17.
  A CON na frente vence de 32% a 52% (antes, 8% a 52%); quem escolhe só Vida deixa de ficar
  sem armadura nos níveis altos (18% a 47% contra quem alterna; antes, 4% a 6% no 17 e no 20).
- **Sozinho contra muitos** (Capítulo Dez): os PV do chefe não se multiplicam mais. Depois do
  turno de cada personagem, ele responde contra quem agiu com a técnica de dano mais barata
  dele, sem gastar Cosmo. Quatro Bronzes contra um Ouro: 42% a 64%, em 8 a 11 rodadas (antes,
  13 a 18). O livro dá um rosto a cada resposta.
- **Técnica Lida** (Capítulo Cinco): quem leu anota, na ficha dele; só quem tem Convicção
  lembra depois da luta. A ficha do personagem ganhou "Lidas por mim".
- **Glória** (Capítulo Doze): um gatilho novo, resolver sem luta um conflito que importava.
- **Só a morte de verdade** (Capítulo Sete): a armadura destruída de propósito revive na
  mesma Versão, sem bônus.
- Fichas prontas e tabela de grupo medidas de novo com a regra do chefe.

### Adicionado

- **Apêndice: Notas de design e balanceamento.** As notas de "medido" e de "numa versão
  anterior" saíram do corpo dos capítulos — no lugar ficou uma linha de conselho de mesa — e
  foram para o apêndice, com um aviso do que o simulador sabe e do que não sabe.
- `test.py`: FOR e CON contra DES; nenhum extremo de Vida ou Cosmo vence quem alterna, e
  nenhum é armadilha; o grupo contra o Ouro em até 12 rodadas.

### Corrigido

- O Capítulo Dois dizia que um Bronze vence um Ouro do mesmo nível "menos de uma vez em
  dez"; desde a 0.6.0, no duelo justo, não vence.
- O chefe respondia também depois do turno do aliado de luta.

## [0.7.0] - 2026-09-27

### Mudado

- **Sem salto de nível** (Capítulos Seis e Doze): cada ponto de dano, de PV temporários ou
  de cura rola o dado + o **bônus do ponto**, que é o nível − 1, até o máximo do Grau da
  técnica (+3, +7, +11, +15, +19). Antes, 1d8 por Grau. A tabela de níveis ganhou a coluna
  Ponto.
- **PV base nível a nível** (14, 18, 23, 30 … 260), e **Vida** soma metade do nível (para
  cima) por escolha. Um nível acima vence de 55% a 91% (antes, 50% a 97%); os saltos de
  Posto — Bronze, Prata, elite — continuam.
- Crítico de técnica e ponto queimado: um ponto a mais (dado + bônus do ponto).
- **Figurantes** (Capítulo Dez): uma linha por nível, dano fixo; o golpe comum derruba
  dois, a técnica de alvo único três, a de área o bando inteiro. Seis figurantes custam de
  15% a 30% dos PV em 2 a 4 rodadas. Antes, derrubavam um personagem de nível 1 em 94% das
  vezes.
- **Aliado de luta** (Capítulo Onze): metade do nível do grupo, metade dos PV, e não conta
  para Sozinho contra muitos. Leva um duelo de 50% para 68% a 72%.
- **Tabela rápida de inimigos**: nível 1 a 20, com o Cosmo (começa, piso, Teto), sem
  características. **Montar um inimigo** ganhou o passo das escolhas de nível.
- Tabela de dificuldade medida de novo, com o rival um nível acima como "difícil"; o aviso
  da fronteira de Grau virou o da fronteira de Posto. Textos das fichas prontas, do grupo
  contra um Ouro (quatro Bronzes vencem de quatro a seis vezes em dez, em 13 a 18 rodadas)
  e todos os números medidos do livro, de novo.
- Os exemplos de Golpe do Assento estão no Grau 4 (a elite começa no nível 15).

### Adicionado

- `sim/mestre.py` e `sim/MESTRE.md`: dificuldade, figurantes, aliado de luta e fichas
  prontas, medidos. `test.py mestre` confere o nível sem salto, o bando, o aliado e cada
  frase das fichas prontas; `test.py extremos` confere que nem só Vida nem só Cosmo domina.

### Corrigido

- As fichas prontas davam a terceira defesa treinada a partir do nível 10; ela vem da
  escolha de nível (no lutador de referência, no 11).
- As fichas prontas mostravam o bônus de ataque de Golpe em técnicas de Cosmo.
- A tabela de duração do teste de estresse podia mostrar empate negativo.

## [0.6.0] - 2026-09-27

### Adicionado

- **O Cosmo não acaba** (Capítulo Quatro): o piso (1, +1 a cada duas escolhas de Cosmo);
  a vida paga o que falta de uma técnica, sem limite, a 1d4 por ponto × Grau; o último
  golpe — se o preço passar da vida que resta, o golpe sai; se derrubar o inimigo, você
  fica com 1 PV; se não, você cai.
- **Progressão por escolha** (Capítulo Doze): todo nível, Vida (+2 PV por Grau) ou Cosmo
  (+1 Teto, +1 Cosmo inicial, piso +1 a cada duas); nos níveis 4, 6, 8, 10, 12, 14, 16, 18
  e 20, técnica nova ou +2 num atributo; nos 3, 7, 11, 15 e 19, perícia ou defesa. A tabela
  de níveis mostra o que se ganha e o que se escolhe.

### Mudado

- **PV por Grau: 14, 40, 80, 135, 205.** A luta é curta e decisiva no começo e longa no
  fim: com Convicções, de 4,7 rodadas no nível 1 a 10,8 no nível 20 (sem, de 2,9 a 7,4).
- Queimar: só os pontos além do custo têm limite; depois, o Cosmo volta ao piso, não a zero.
- Guerra dos Mil Dias: o choque pede o mesmo natural de 16 a 20 (com técnica toda rodada,
  qualquer número igual travava metade das lutas entre Ouros). Agora 9% a 15%.
- Sozinho contra muitos: PV × 1¼, 1½, 1¾, 2, 2¼ para 2 a 6 oponentes, e 0 a 4 golpes comuns
  a mais por rodada (não ações livres). Quatro Bronzes contra um Ouro: 43% a 51%.
- Constelação viva: +1 no acerto no Sétimo. Coração de estrela: Vantagem no ataque depois
  de levantar. (Curar na hora de levantar valia até 64% no nível 13.)
- Saíram Cosmo Desperto, Cosmo Sereno, a Terceira defesa treinada e os aumentos de
  atributo fixos: tudo isso virou escolha.
- Téo tem 15 PV no nível 1. Tabelas de dificuldade, de grupo, de fronteira de Grau e as
  fichas prontas medidas de novo. No duelo justo, o Bronze não vence mais o Ouro (menos de
  1%); quatro Bronzes juntos, sim.

### Corrigido

- O simulador dava à Constelação viva +1 de Teto que o livro não tinha (0.5.0).

## [0.5.0] - 2026-09-27

### Adicionado

- **Características da armadura** (Capítulo Sete): 1 no Bronze, 2 na Prata, 3 na elite,
  escolhidas numa lista de onze — Couraça grossa, Espinhos, Espelhada, Pesada, Leve,
  Ressonante, Constelação viva, Coração de estrela, Cortante, Ofuscante e Elmo fechado. A
  cada forma nova, dá para trocar uma. A tabela sai do simulador no build. Mais o traço
  de origem, de graça, que não mexe na luta.
- Medido: cada característica, sozinha, vence 45% a 62% dos duelos contra a mesma
  armadura sem ela.
- As fichas prontas de inimigos têm as características delas; a criação (Capítulo Três),
  a ficha pronta do Téo (Cortante) e o modelo de ficha ganharam o campo.
- Metas novas em `test.py`: cada característica na faixa; as dos lutadores de referência
  estão na tabela do livro.

### Mudado

- **Sozinho contra muitos:** PV × 1¼, 1¾, 2¼, 2¾, 3¼ para 2 a 6 oponentes (eram × 1,5 a
  3,5). Com as características, o chefe ficava duro demais: quatro Bronzes venciam um Ouro
  25% a 32%. Agora, 38% a 42%.
- O simulador monta os lutadores de referência com as características típicas do Posto.
  Os números do livro foram medidos de novo: o Bronze vence o Prata 9% a 13%, o Ouro 0% a
  2%; a tabela de dificuldade e a de grupo contra um foram refeitas.

## [0.4.0] - 2026-09-27

O sistema passou por um teste de estresse: `sim/extremos.py` tenta quebrá-lo e escreve
`sim/EXTREMOS.md`. O simulador ganhou condições, limitações e luta de grupo contra um.

### Adicionado

- **Sozinho contra muitos** (Capítulo Dez): inimigo com Convicção, sozinho contra dois ou
  mais personagens, tem PV × (oponentes + 1) ÷ 2 e ações a mais por rodada (uma para cada
  dois oponentes). Sem ela, três Bronzes venciam um Ouro do mesmo nível 92% das vezes;
  com ela, quatro Bronzes vencem 47% a 48%, e uns três caem.
- **O mesmo golpe não funciona duas vezes, para condições:** uma condição forte que
  acabou não volta com a mesma técnica, no mesmo alvo, naquela luta.
- Aviso da fronteira de Grau na tabela de dificuldade: o inimigo que já cruzou o 5, 9,
  13 ou 17 conta como dois degraus mais difícil.
- Conselho de build no Capítulo Três: dois jeitos de lutar, e a CON na frente como
  armadilha.
- `sim/extremos.py` e `sim/EXTREMOS.md`; condições, limitações e grupo contra um no
  simulador (`sim/luta.py`); metas novas em `test.py` (bloco `extremos`).

### Mudado

- **DEF = 10 + DES ou o Atributo do Cosmo, o que for maior, + armadura.** O golpe comum
  pode usar FOR, DES ou o Atributo do Cosmo. Quem lutava pelo Cosmo vencia 21% a 38%;
  agora, 39% a 59%.
- **Atordoado:** perde a ação e a reação, sem dar Vantagem a quem ataca. Quem atordoava
  vencia até 89%; agora, 48% a 60%.
- **Limitações:** "causa 1d6 em você" virou 1d6 por Grau; "exige carregar" agora é "no
  turno anterior você não usa técnica", em vez de gastar a ação inteira.
- A regra de bolso "cada personagem a mais vale dois níveis" saiu: medido, valia uns seis.
- Fichas prontas: Guerreiro Deus, Cavaleiro de Ouro e Juiz do Inferno ganharam o quanto
  pesam contra um grupo de quatro.

## [0.3.2] - 2026-09-27

### Mudado

- **Menos vidas:** o sangue de guerreiro revive a armadura de Bronze até 3 vezes, a de
  Prata até 4 e a de elite até 6 (eram 3, 6 e 9). Com nove, uma armadura de Ouro quase
  nunca morria de vez. Medido: a Prata revivida quatro vezes vence a original 58% a
  61%; o Ouro revivido seis vezes, 58% a 60%; a Prata com a escada inteira vence um
  Ouro 16% a 23%.

## [0.3.1] - 2026-09-27

### Mudado

- **Mais vidas para Posto mais alto.** O sangue de guerreiro revive a armadura de
  Bronze até 3 vezes, a de Prata até 6 e a de elite até 9. A armadura de elite não tem
  o degrau de elite: para ela, o sangue de elite é o normal, com o bônus normal. Elite
  e deus continuam uma vez cada (a elite, só para Bronze e Prata).
- **Bônus das formas menores.** Com mais vidas, os bônus da 0.3.0 somavam demais: a
  Prata com a escada inteira vencia um Ouro 58% a 66%. Agora cada forma de guerreiro
  alterna +1 no acerto (1ª, 3ª, 5ª…) e +1 de Resistência (2ª, 4ª…); a de elite dá +1
  na DEF; a de deus, +1 na DEF e +1 no acerto. O acerto e a DEF das formas só valem com
  a armadura no corpo. Medido: a V4 de Bronze vence a original 57% a 63%; a Prata com a
  escada inteira vence um Ouro 22% a 29%; o Ouro revivido nove vezes vence o original
  69% a 71%.
- **Restaurar: Ofício contra CD 14 + a Versão** (era 14 + 2 × a Versão, que passava de
  30 numa armadura de Ouro revivida nove vezes).
- Metas novas em `test.py`: a escada por Posto, o exemplo do Capítulo Sete, a Prata com
  a escada inteira abaixo do Ouro, o Ouro revivido nove vezes forte sem ser imbatível.

## [0.3.0] - 2026-09-27

### Adicionado

- **A Hierarquia:** um Prata tem +2 em todas as rolagens contra um Bronze, e o Bronze
  tem −2 contra ele. A elite não usa a Hierarquia. Medido: do mesmo nível, o Bronze
  vence o Prata de 12% a 19% das vezes (era cerca de 40%) e o Ouro de 1% a 4%.
- **Cada forma nova da armadura é mais forte:** a cada revivida, o sangue deixa um
  bônus permanente. Guerreiro: +1 DEF e +1 de Resistência. Elite: +2 e +2. Deus: +3 e
  +3. Os bônus somam. A tabela da escada do sangue sai do simulador no build.
  Medido: a V4 vence a original de 64% a 69%; com a forma de elite, de 73% a 81%; a
  armadura de Bronze com as cinco formas vence um Ouro de 19% a 25%.

### Mudado

- **A armadura agora tem Resistência, um número só**, no lugar das caixas em cada
  peça. Bronze 3, Prata 4, Ouro 5, forma Divina 6; +1 sem acessório; +1 nos níveis 5,
  7, 13 e 17. Aparar gasta 1. A 0, a armadura está em pedaços: sem DEF, Bloquear,
  Elmo, Pernas nem acessório até se refazer. As caixas por peça quase nunca acabavam
  numa luta simulada: davam trabalho sem mudar o resultado.
- O Elmo segura o primeiro crítico uma vez por luta. Quebrar a armadura tira 1 de
  Resistência por acerto.
- Melhorias, remédios, a Escama dos Marinas, a ficha pronta, o modelo de ficha e as
  fichas de inimigos passaram para a Resistência.
- A dourada no Sétimo virou só o traço do sangue de elite; o ganho de números está no
  bônus da forma.
- Tabela de dificuldade medida de novo: o Prata do mesmo nível virou linha própria,
  "Muito difícil" (o Bronze vence de 11% a 19%). O Cavaleiro de Prata pronto foi
  medido de novo: um Bronze do mesmo nível vence uma vez em cinco.
- Metas novas em `test.py`: o Bronze normalmente perde para o Prata; perde mais para
  o Ouro que para o Prata; cada forma nova ajuda; nem com sangue de deus a armadura
  de Bronze iguala o Ouro.

## [0.2.2] - 2026-09-27

### Mudado

- **O Prata só a partir do nível 9** (era 5). A elite continua no 15.
- O Cavaleiro de Prata pronto subiu do nível 6 para o 9. Medido: um Bronze do mesmo
  nível vence 36% das vezes; um de nível 8, 6%, porque o Grau muda no 9.
- A tabela rápida de inimigos mostra um traço na DEF de Prata e de elite nos níveis em
  que esses Postos ainda não existem, e ganhou as linhas dos níveis 9 e 15.
- O simulador e os testes só medem Prata e Ouro onde eles existem, e passaram a medir
  também os níveis 15 e 20. Os números de Bronze contra Ouro foram refeitos com o Ouro do
  15 ao 20: sozinho, de 1% a 4%; com uma Centelha por rodada, de 3% a 5% (a 0.2.0 dizia
  até 13%, medido com um Ouro de nível 9); das vitórias, mais de 95% depois de levantar.
  A Guerra dos Mil Dias entre Ouros ficou em 14% a 17%.
- A meta "Centelhas dão uma chance pequena" virou "Centelhas não tiram o Ouro do lugar",
  com margem de 3 pontos para o acaso: do 15 em diante, a Centelha vale cerca de 1 ponto
  contra um Ouro.
- O livro e as fichas prontas passaram a ser conferidos contra o requisito de Posto:
  `test.py` falha se o texto disser outro nível ou se uma ficha estiver abaixo dele.

## [0.2.1] - 2026-09-27

### Mudado

- **A elite só a partir do nível 15** (era 9): Ouro, General Marina, Juiz do
  Inferno e Guerreiro Deus. O Prata continua a partir do nível 5.
- As fichas prontas de elite subiram junto: Guerreiro Deus e General Marina no
  15, Cavaleiro de Ouro no 16, Juiz do Inferno no 18.
- A tabela "Quanto pesa um inimigo" foi medida de novo com elites do 15 ao 20:
  elite do mesmo nível, 2% a 6%; elite três níveis abaixo (personagem no 18 ou
  mais), 6% a 20%. A 0.2.0 dizia 22% a 36%, medido com elites de nível baixo que
  agora não existem.

## [0.2.0] - 2026-09-27

O sistema passou pelo simulador, ficou mais mecânico e ganhou os capítulos do
Mestre. Tudo que mudou de número mudou por uma medição, e a medição está no
livro ao lado da regra.

### Adicionado

- **Simulador** (`sim/`): o motor de técnicas em código, a luta inteira rodada a
  rodada com todas as regras do livro, e os experimentos que decidiram os
  números (`sim/cenarios.py` gera `sim/RESULTADOS.md`).
- **`test.py`**: confere as contas das técnicas impressas, o build do livro e
  as metas de equilíbrio. Roda em segundos, sem dependências, e no CI.
- **Tabelas geradas**: a tabela de níveis, a de Posto, a tabela rápida de
  inimigos e as sete fichas prontas saem do simulador na hora do build.
- **Capítulo Oito · Itens e relíquias**: raridade, Sintonia, como conseguir
  itens, equipamento comum, remédios e consumíveis, os três metais, melhorias
  de armadura, relíquias e itens divinos. Nenhuma arma.
- **Capítulo Dez · Inimigos**: três tipos, como montar, figurantes em bando,
  a tabela de dificuldade medida e sete inimigos prontos.
- **Capítulo Onze · Aliados e a luta na mesa**: aliados de luta, de longe e
  mentores; o deus do exército; como narrar técnicas, quedas e o levantar;
  duelos em paralelo; a Guerra dos Mil Dias na mesa; uma cena de exemplo.
- **Glória**: subir de nível passa a ter conta — vitórias, despertares e
  objetivos.
- **Interlúdio em semanas**, com oito ações concretas.

### Mudado

- **Os cinco sentidos não se fecham de propósito.** Só se perdem por técnica
  inimiga ou mutilação (Visão ou Audição). "Resistir" saiu.
- **O Ouro domina o Sétimo**: +3 contra quem só o despertou. Armadura de Ouro
  com +6 na DEF, Prata com +4. Medido: um Bronze sozinho vence um Ouro do mesmo
  nível de 3% a 4% das vezes, e quase sempre depois de levantar do chão.
- **Guerra dos Mil Dias**: agora começa num choque de técnicas — o mesmo número
  natural na mesma rodada. A regra antiga travava 95% das lutas equilibradas.
- **Aparar gasta a reação** e disputa com Bloquear.
- **Queimar custa 1d4 por ponto, vezes o Grau**, e nunca derruba quem queima.
  A Queima Controlada saiu.
- **PV por Grau**: 18, 38, 58, 78 e 98, mais 1 por nível dentro da faixa, mais
  CON por nível. Acaba o dente de serra das lutas longas no fim de cada faixa.
- **Ataque Extra no nível 9.** No nível 5, quem nunca usava técnica vencia
  metade dos duelos.
- **Centelhas dão Vantagem** no próximo ataque, além do Cosmo e do Teto.
- **Levantar: uma vez por luta.** Convicções voltam uma por semana de
  Interlúdio e todas ao subir de nível — o "fim do arco" saiu.
- **Oitavo Sentido** com requisito, treino e situação definidos.
- **Restaurar armadura** com teste, tempo e metal por Posto.
- **Posto** com requisito de nível (Prata no 5, elite no 9 com vaga vazia).
- Prazos concretos para a Estrela Maligna, a Súplice e a armadura viva.

## [0.1.0] - 2026-09-27

Primeira versão escrita do sistema: um rascunho jogável em d20, com um livro só
para jogador e Mestre.

### Adicionado

- **Como se joga:** `1d20 + modificador (+ proficiência)` contra CD, DEF ou
  defesa passiva; Vantagem e Desvantagem; crítico; os cinco números da ficha
  (PV, Cosmo, sentidos, Convicções e Centelhas).
- **Criação em nove etapas, sem classes:** exército, constelação e acessório,
  atributos, Atributo do Cosmo, treino (seis opções com uma lição cada),
  Convicções, perícias e defesas, duas técnicas e as contas finais.
- **Cosmo:** começa no modificador do Atributo do Cosmo e sobe pelo relógio,
  pelo golpe que acerta, por Concentrar, pelos sentidos perdidos e pelas
  Centelhas. Nunca sobe por perder PV. Teto de Cosmo = 3 + proficiência.
  Queimar paga e reforça a técnica, e custa dano e o Cosmo inteiro.
- **Sentidos:** diferença de Sentido em degraus (Sexto, Sétimo, Nono); o Ouro
  entra no Sétimo quando quer, o Bronze e o Prata despertam com Cosmo no Teto,
  um sacrifício e uma Convicção, e só por uma luta. Guerra dos Mil Dias. O
  Oitavo sem ganho de poder. O Nono com elo divino de sangue ou de ligação.
- **Os cinco sentidos** como trilha de sacrifício, com penalidade própria para
  cada um.
- **Combate:** golpe comum, ações, "o mesmo golpe não funciona duas vezes"
  (marca de Lida), figurantes, cair sem morrer e levantar com Convicção,
  condições e descanso.
- **Técnicas:** o motor de criação por pontos, adaptado da Ascensão dos
  Semideuses, pago em Cosmo; evolução; técnica assinatura; Golpe do Assento;
  oito técnicas de exemplo.
- **Armaduras:** cinco peças com caixas, Aparar, regeneração, morte, a escada
  do sangue em terços, Versões, o traço do sangue e a forma Divina.
- **Exércitos:** o molde e quatro exemplos (Atena, Poseidon, Hades, Asgard).
- **Níveis 1 a 20**, uma ficha pronta, um modelo de ficha e a consulta rápida.
- **Pesquisa:** o relatório de referências e as notas, em `pesquisa/`.

### A medir

Nenhum número desta versão passou por simulador ainda. Os primeiros a medir:
o ritmo do Cosmo numa luta de três a cinco rodadas, o custo de queimar, o bônus
de Lida, as caixas de armadura por Posto e os ganhos de nível.
