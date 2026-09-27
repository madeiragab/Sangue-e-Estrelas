# Changelog

Todas as mudanças que alteram regra ou número ficam registradas aqui. O número
de versão do livro e do site sai da primeira linha `## [x.y.z]` deste arquivo.

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
