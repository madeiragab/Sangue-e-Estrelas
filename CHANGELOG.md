# Changelog

Todas as mudanças que alteram regra ou número ficam registradas aqui. O número
de versão do livro e do site sai da primeira linha `## [x.y.z]` deste arquivo.

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
