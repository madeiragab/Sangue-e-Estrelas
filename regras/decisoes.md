# Decisões de design

O registro do que já foi decidido e por quê. Quando uma regra do livro parecer
estranha, a explicação deveria estar aqui. Quando uma decisão mudar, ela muda
aqui primeiro.

## Base

- **Sistema próprio**, separado da Ascensão dos Semideuses. O motor de técnicas e
  a estrutura do livro vieram de lá; o resto é novo.
- **d20 principalmente.** `1d20 + modificador (+ proficiência)` contra CD, DEF ou
  defesa passiva (14 + atributo + proficiência). A ideia de "Sentido = tamanho do
  dado, Cosmo = quantidade" foi estudada e ficou de fora; as contas estão em
  `pesquisa/notas/motores_de_dado.md`.
- **Um livro só**, para jogador e Mestre.
- **Foco no sistema, não em campanha.** O livro não traz aventura pronta.
- **Projeto de fã, sem venda.** Aviso de independência em todas as páginas.

## Personagem

- **Sem classes escolhíveis.** A diferença entre guerreiros vem da constelação
  (forma da armadura e acessório), do treino (duas perícias e uma lição) e das
  técnicas montadas por pontos.
- **Postos: Bronze, Prata, Ouro.** Todo personagem começa Bronze, em qualquer
  exército.
- **Subir de Posto é narrativo, com requisito de nível** (0.2.0): Prata a partir do
  nível 9, elite a partir do 15 e com vaga vazia (na 0.2.0 eram 5 e 9, cedo demais). O momento vem da história.
- **A armadura sobe de Bronze a Prata na mesma constelação.** Precedente: Órion
  é Prata na obra do Kurumada e Bronze no Ômega.
- **Ouro é um conjunto fechado de vagas** (as 12 do zodíaco), e cada vaga tem um
  Golpe do Assento (Excalibur, Cólera dos Cem Dragões, Trovão Atômico). Quem assume
  a vaga continua usando as próprias técnicas.
- **Convicções:** três frases "eu luto…". Levantar gasta uma (uma vez por luta);
  despertar invoca uma. Voltam uma por semana de Interlúdio e todas ao subir de nível.
- **Glória** (0.2.0): subir de nível tem conta — vitórias contra nomeados, despertares,
  objetivos. O pedido foi de um sistema menos narrativo.

## Exércitos

- **Molde de exército** para o Mestre criar qualquer exército e hierarquia. Os
  quatro do livro (Atena, Poseidon, Hades, Asgard) são exemplos.
- O molde tem: o deus (fonte do sangue divino e do elo do Nono), os nomes, a
  hierarquia em três degraus equivalentes a Bronze, Prata e Ouro (elite com vagas
  contadas, cada uma com Golpe do Assento) e uma ou duas regras próprias.
- Poseidon e Asgard ganharam postos de base e do meio inventados, porque no
  anime eles quase só têm elite.

## Cosmo

- **O Cosmo cresce durante a luta** e paga as técnicas: pelo relógio (+1 por
  rodada a partir da segunda), pelo golpe comum que acerta (+1), por Concentrar
  (+2), pelos sentidos perdidos e pelas Centelhas.
- **Perder PV nunca dá Cosmo.** É a trava contra "apanhar de propósito".
  Referência: as reclamações sobre o modo Rage do Tekken. Medido: quem não apara a
  armadura vence 34% a 46%.
- **Teto de Cosmo = 3 + proficiência.** Só queimar passa dele.
- **Queimar** paga e reforça a técnica; custa **1d4 por ponto, vezes o Grau**; nunca
  derruba; zera o Cosmo; ignora Lida. Com preço fixo, quem queimava vencia 80% nos
  níveis altos.

## Sentidos

- **Sexto:** todo guerreiro.
- **Sétimo:** o Bronze (e o Prata) alcança em luta, perto da morte ou em esforço
  extremo, e precisa alcançar de novo em cada luta. O Ouro, pelos anos de treino e
  pela armadura de Ouro, entra quando quer. Na regra: Cosmo no Teto + um sacrifício
  (sentido, levantar ou queimar) + uma Convicção dita antes de rolar. **A primeira vez é
  um marco** (0.10.0): só do nível 5 em diante, numa luta que importa.
- **O Ouro domina o Sétimo** (0.2.0): +3 contra quem só o despertou; armadura de
  Ouro +6. O usuário apontou que, no anime, os Bronzes só venceram Ouros por roteiro
  (Shura deu a armadura ao Shiryu; Shun por milagre; Hyoga quase morreu). Medido: um
  Bronze sozinho vence um Ouro do mesmo nível (15 a 20) de 1% a 4%; com Centelhas, de 3%
  a 5%; e quase sempre depois de levantar do chão.
- **Ouro contra Ouro:** o Sétimo se anula (precedente: o RPG de CDZ de fã no sistema
  Daemon). **Guerra dos Mil Dias** começa num **choque de técnicas** (mesmo natural na
  mesma rodada). A primeira regra ("mesmo Teto") travava 95% das lutas equilibradas.
- **Oitavo:** treino + uma situação específica; **não necessariamente aumenta o
  poder**; dá o estado de Buda (morrer sem morrer) e a entrada viva no mundo dos
  mortos. **Todos precisam despertar**, inclusive os Ouros.
- **Nono:** o sentido dos deuses. Exige algo direto de um deus. **Só é
  verdadeiro com sangue**; um objeto ou vínculo (a pulseira/rosário do Tenma) dá
  um Nono condicional, que some quando o elo é cortado. Como o Sétimo do Bronze,
  **vale por luta**: depois, a armadura Divina volta à forma padrão.

## Os cinco sentidos

- Todo sentido perdido dá +1 Cosmo e +1 Teto.
- **Ninguém fecha um sentido de propósito** (0.2.0). Só se perde por técnica inimiga
  ou por mutilação (se cegar, se ensurdecer). O Ikki contra o Shaka foi genialidade
  contra uma técnica que arranca sentidos — e a regra permite isso: o sentido arrancado
  sobe o Cosmo. "Resistir" (entregar um sentido para não cair) saiu.

## Armadura

- **Duas coisas separadas:** a Resistência se gasta e se regenera; a vida da
  armadura pode acabar.
- **Resistência, um número só** (0.3.0). Antes eram caixas em cada uma das cinco
  peças, e o usuário achou confuso. Medido: as caixas por peça quase nunca acabavam
  numa luta, então não mudavam o resultado — eram só conta. Agora Aparar gasta 1 de
  Resistência e, a 0, a armadura está em pedaços e não dá mais nada.
- **A Hierarquia** (0.3.0): o Prata tem +2 em tudo contra um Bronze, e o Bronze −2
  contra ele. O usuário apontou que o Bronze também perde para o Prata, não tanto
  quanto para o Ouro. Subir a DEF do Prata não bastava: com +6, igual à do Ouro, ele
  vencia só ~70% e passava a vencer o Ouro mais vezes. A Hierarquia só vale para baixo,
  e não mexe no Prata contra o Ouro. Medido: o Bronze vence o Prata de 12% a 19%.
- **Aparar gasta a reação** e disputa com Bloquear (0.2.0). De graça, cortava toda
  técnica pela metade e as lutas passavam de dez rodadas.
- **Restaurar tem teste** (Ofício CD 14 + Versão), tempo e metal por Posto. Era
  14 + 2 × Versão; com a armadura de Ouro revivendo muitas vezes, a CD passava de 30.
- **Estilo clássico (urna) ou Ômega (pedra):** só visual. **Sem sistema
  elemental** do Ômega (a própria série abandonou na segunda metade).
- **Reviver com sangue, em terços:** 1/3 do sangue de uma pessoa por armadura; o
  Shiryu quase morreu porque reviver duas custou 2/3 (Seiyapedia, página do Mu).
- **A escada do sangue segue o mangá:** primeiro sangue de Cavaleiro (até três
  vezes no Bronze, e a armadura muda de forma a cada uma — a de Pégaso tem 5 versões no
  mangá e 3 no anime), depois sangue de Ouro, depois sangue de deus.
- **Mais vidas para Posto mais alto** (0.3.1, ajustado na 0.3.2): pedido do usuário.
  Sangue de guerreiro revive a de Bronze 3 vezes, a de Prata 4, a de Ouro 6. Na 0.3.1
  eram 3, 6 e 9; o usuário achou 9 demais — com tantas vidas, uma armadura de Ouro
  quase nunca morreria de vez. A de Ouro não tem o degrau de elite: o sangue de elite é
  o normal dela, com o bônus normal.
- **Cada forma nova é um pouco mais forte** (0.3.0, rebalanceado na 0.3.1): pedido do
  usuário. Os bônus da 0.3.0 (guerreiro +1 DEF e +1 de Resistência, elite +2 e +2, deus
  +3 e +3) somados às novas vidas faziam a Prata com a escada inteira vencer um Ouro 58%
  a 66%. O usuário pediu bônus menores ("+1 no acerto por evolução, +1 na DEF quando é
  de Ouro"). Agora: guerreiro alterna +1 no acerto (1ª, 3ª, 5ª…) e +1 de Resistência
  (2ª, 4ª…); elite +1 DEF; deus +1 DEF e +1 no acerto. Só Resistência não bastava: +1 de
  Resistência sozinho não mudava a luta (48% a 51%). Medido (0.3.2): a Prata com a
  escada inteira vence um Ouro 16% a 23%; o Ouro revivido seis vezes vence o original 58%
  a 60%.
- **Sangue de Ouro:** a armadura fica dourada no Sétimo (a New Cloth do Seiya,
  com o sangue do Aiolia).
- **Sangue de deus não vira Divina direto.** A Divina é um estado: sangue de deus
  na armadura + Cosmo no nível de um deus (o Nono). Precedente: Seiya em Elysion.
- **Lost Canvas:** o Tenma teve a Divina por instantes graças ao rosário da Sasha
  (elo de ligação), e a perdeu quando a conexão foi cortada no último episódio do
  anime.

## Técnicas

- **Montadas por pontos**, com o motor da Ascensão; custo pago em Cosmo, não numa
  reserva do dia.
- **"O mesmo golpe não funciona duas vezes":** marca de Lida por oponente
  nomeado, +2 fixo nas defesas contra a técnica. Queimar, despertar ou evoluir
  passa por cima. Nenhum RPG pesquisado tinha essa regra.
- **Sem armas.** O juramento dos Cavaleiros de Atena; armas de armadura (Libra,
  lanças dos Marinas) entram como acessório ou Golpe do Assento.

## Números (0.2.0)

- **PV por Grau:** 18, 38, 58, 78, 98, mais 1 por nível na faixa, mais CON por nível.
  Com PV subindo todo nível, o nível 4 passava de 12 rodadas.
- **Ataque Extra no nível 9.** No 5, dar só golpes comuns rendia o mesmo que usar
  técnicas.
- **Centelha:** +1 Cosmo, +1 Teto, Vantagem no próximo ataque.

## O primeiro playtest (0.10.0)

Uma campanha de um jogador só, com o ChatGPT de Mestre, do humano de nível 1 ao Bronze de
nível 4 (`regras/playtest-01.md`). O que mudou:

- **O primeiro Sétimo é um marco, do nível 5 em diante** (decisão do usuário, "nível 5 mais
  a situação"). Pela regra, o Bronze de nível 1 despertou ao levantar na primeira luta séria;
  o usuário vetou na campanha ("o Sétimo só desperta bem mais para a frente, contra um
  inimigo de verdade"). O problema não era só o levantar: no nível 1 o Teto é 5 e queimar um
  ponto custa 1d4. A primeira vez agora pede o nível 5 e uma luta contra Posto acima ou um
  nomeado com Convicção; depois, vale a regra de sempre. O simulador trata o nível mínimo
  como a primeira vez já acontecida. Custo aceito: nos níveis 1 a 4 o personagem perde o
  Sétimo que levantar dava, e o nível 5 virou um salto (88% contra quem está no 4).
- **Figurante não racha armadura.** O dano do bando não se apara e o ataque dele não tem
  crítico. Na mesa, a armadura morreu aparando soldado raso; o simulador nunca modelou isso,
  então o livro passou a dizer o que o simulador media.
- **A área derruba até seis.** "O bando inteiro" deixava uma técnica de tamanho 3 apagar
  bandos de doze toda rodada (com piso 2, ela sai de graça: 3 de Cosmo, paga, volta ao piso 2,
  +1 no turno). Testado e descartado: bandos de no máximo seis, cada um atacando — dois bandos
  juntos derrubavam um personagem de nível 1 a 4 em 8% a 12% das lutas e custavam metade dos
  PV.
- **Surpresa: o golpe de abertura**, só golpe comum, com Vantagem. Testados e descartados:
  uma ação inteira antes da Iniciativa (60% a 81% num espelho) e agir primeiro com Vantagem
  (59% a 78%). Só agir primeiro já vale 54% a 69%: a Iniciativa pesa neste jogo.
- **O ritmo da Glória fica** (decisão do usuário): um nível por missão, do N1 ao N4 em duas
  semanas de história, foi o que ele quis.
- Esclarecimentos sem número: o piso e a vida paga (o texto dizia "sai de graça"; o
  simulador sempre cobrou da vida o que passa do Cosmo que se tem), arredondamento para
  cima, empate com bando, PV ao subir de nível, Elmo na luta seguinte, pular degraus da
  escada do sangue, kit de medicina, nível humano por ano × três semanas, laço da Centelha.
- **Pedidos do usuário depois do playtest (0.11.0):** armaduras de Ouro emprestadas por uma luta;
  restaurar sem esperar o Interlúdio; o custo do sangue em dias e PV; testes para as
  "coisas idiotas" (respirar, porta, corrente); levantar só quando faz sentido (quem está
  controlado não usa a Convicção).
- **A armadura emprestada pede o Sétimo** (do nível 5 em diante no Bronze): amarra ao
  marco que o usuário escolheu e é o que a série mostra. Ela dá a linha do Ouro e as
  características dela, não as formas da armadura do personagem, nem o Assento, nem o
  domínio: medido, 80% a 86% contra um Bronze do mesmo nível, 1% contra um Ouro.
- **Os feitos por degrau, não por CD fixa.** Um guerreiro não rola para arrombar uma porta
  de madeira; um humano não tenta partir uma rocha. O degrau (gente, guerreiro, Sétimo, deus)
  resolve as duas coisas com uma regra. Os perigos usam o mesmo degrau, e o dano em acertos
  de bando do nível, para pesar parecido em toda a campanha.
- **O sangue volta em 3 dias por terço.** Antes, uma semana de Interlúdio — numa campanha
  sem Interlúdio, nunca. Medido: lutar Debilitado é quase perder (40% no nível 1, 9% no 20),
  então três dias bastam para o custo pesar.
- **O sacrifício da armadura é opcional.** Medido, não muda nada numa luta comum (a
  Resistência quase nunca acaba); com a armadura gasta de uma luta anterior, ajuda muito nos
  níveis 1 a 5. O preço real é a armadura morta.
- **Fichas novas:** o Espectro Novato fica no nível 3 (o Cavaleiro Negro já é o 2), e a
  Estrela Celeste no 11, acima do Cavaleiro de Prata (9).
- **A raridade dos Sentidos** (0.12.0, pedido do usuário): Sétimo quase impossível no Bronze, raro
  no Prata veterano, padrão na elite; Oitavo, um ou dois Ouros por geração; Nono, nem
  conhecido. Os personagens são a exceção. Virou regra do Mestre: Bronze e Prata sem
  Convicção não despertam. Medido, quase nada muda — o nomeado sem Convicção raramente
  chegava ao Sétimo.
- **"Se for de Ouro mantém o Sétimo, se for de Prata não"** foi lido como requisito: a
  armadura de Ouro emprestada continua pedindo o Sétimo, a de Prata não. As emprestadas podem
  vir de donos mortos (Sagitário para o Seiya, Aquário para o Hyoga).
- **Os deuses em dois tamanhos** (pedido do usuário: "no Nono e de armadura Divina, supera
  divindades menores e luta quase no nível de um deus maior"). Medido no simulador, que
  passou a ter o Nono numa luta e o deus montado sobre a elite de nível 20. O deus apara pelo
  tamanho do golpe, não pela fração dos PV dele — sem isso, um deus com mais PV aparava menos
  e perdia mais. Testado: 3 × os PV, +4 e duas ações (0% a 1% para um personagem sozinho);
  2 × e +2 com uma ação (42% e 64%: perto demais). Ficou 2 × e +4 (25% e 40%).

## Antes do Sexto Sentido e a cadeia de comando (0.9.0)

- **Pedido do usuário:** para virar guerreiro é preciso ser treinado por uma patente
  maior; o Bronze não pode ter aprendiz, Prata e Ouro podem; Prata comanda Bronzes, Ouro
  comanda Pratas, o Grande Mestre comanda os Ouros e o deus comanda o Grande Mestre. E um
  status base com que todos começam, antes de despertar o Sexto Sentido — o ponto em que a
  pessoa vira sobre-humana (o Bronze de nível 1).
- **O humano não luta contra o desperto com ficha própria: é figurante.** É o que a série
  mostra (a guarda do Santuário não segura um Cavaleiro), e a tabela do bando já está
  medida. A ficha do humano (4 + CON de PV, 1d4 no golpe, defesas 10 + atributo) serve para
  cenas entre humanos: o treino e a prova.
- **O despertar acontece no limite**, como tudo neste jogo: na prova, quem cai e levanta
  com a Convicção levanta desperto. Medido: 3 a 4 rodadas; em quatro de cada cinco provas
  os dois despertam — a armadura vai para quem vence.
- **A cadeia de comando é história, não regra de combate.** Treinar aprendiz é uma ação de
  Interlúdio (Prata ou acima); a missão, e com ela o objetivo que vale Glória, desce a
  escada. Líderes: Grande Mestre (Atena), o General do Dragão Marinho (Poseidon), Pandora e,
  acima dela, Hypnos e Thanatos (Hades), Hilda de Polaris (Asgard).

## Lapidar: FOR, CON, chefe, Lida (0.8.0)

- **Pedido do usuário:** atacar três pontos de uma leitura crítica do livro — FOR e CON
  valendo menos que DES e Cosmo; a Técnica Lida pesando na ficha; a luta do grupo contra a
  elite longa demais — e mais três menores (Glória fora da luta, farm de morte de armadura,
  notas de design no corpo do livro). O princípio da constelação ficou para depois.
- **A guarda.** Medido: FOR na frente vencia 13% a 51% contra DES (a DEF dependia de outro
  atributo). Com a armadura no corpo, FOR ou CON entram na DEF: 44% a 50%. Sem armadura, a
  guarda cai — quebrar a armadura do Touro abre a guarda dele.
- **Resistência = CON (mínimo 0) + 1 a cada duas escolhas de Vida**, no lugar de +1 nos
  níveis 5, 7, 13 e 17. A CON na frente foi de 8%–52% para 32%–52%; a duração das lutas não
  mudou; o salto do nível 17 sumiu. Sem o +1 da Vida, quem escolhia só Vida vencia 4% a 6%
  contra quem alterna no 17 e no 20 (a armadura acabava nas lutas longas); com ele, 18% a
  47%. Testado e descartado: Vida valendo o nível inteiro em PV (não resolvia: o problema era
  a armadura, não os PV); teto no piso do Cosmo (tirava do Cosmo sem ajudar a Vida).
- **O chefe responde.** Com PV × 1¼ a 2¼ e golpes comuns a mais, quatro Bronzes contra um
  Ouro levavam 13 a 18 rodadas — e o golpe comum, que não cresce com o nível, quase não pesava
  no 20. Agora: PV normais e uma resposta depois do turno de cada personagem, com a técnica de
  dano mais barata, sem Cosmo, contra quem agiu. 42% a 64% em 8 a 11 rodadas. Testados:
  golpes comuns (o grupo vencia até 86%), técnicas livres (81% no 15, 29% no 20), a técnica
  média (duro demais com três), PV × 1⅛ a 1½ com respostas (o Ouro ficava duro demais).
  Um Prata sozinho contra três ou mais cai depressa; o livro manda pôr dois.
- **A Resposta é só o dano** (0.8.1, apontado na mesma leitura): a técnica mais barata
  sai uma vez depois de cada personagem, e um efeito barato nela (Lento, Caído, quebrar)
  sairia junto, de graça. Agora só o dano, salvo o que a ficha do chefe escrever; as fichas
  prontas trazem a Resposta. O simulador já usava técnicas sem efeito: números iguais.
- **Lida** — quem leu anota; só quem tem Convicção lembra depois da luta. Sem efeito no
  simulador (ele mede uma luta de cada vez); o ganho é de ficha.
- **Glória** — resolver sem luta um conflito que importava vale 1.
- **Armadura** — morte de propósito não dá forma nova.
- **Apêndice** — as notas medidas saíram do corpo dos capítulos.

## Sem salto de nível, e o motor do Mestre conferido (0.7.0)

- **Pedido do usuário:** "suaviza o salto de nível, mas não o de grau, tipo Bronze pra
  Prata, Prata pra Ouro". Até a 0.6.0 o dano de cada ponto era 1d8 por Grau e os PV
  vinham por Grau: nos níveis 5, 9, 13 e 17 os dois saltavam juntos, e um nível acima
  vencia até 97%.
- **O dano de cada ponto é 1d8 + nível − 1** (o "bônus do ponto"). Nos começos de faixa dá
  a mesma média do 1d8 por Grau; no meio, cresce aos poucos. A técnica soma no máximo o
  bônus do último nível do Grau dela (+3, +7, +11, +15, +19): a evolução continua valendo.
  O crítico de técnica e o ponto queimado somam um ponto inteiro (dado + bônus).
- **PV base nível a nível:** 14, 18, 23, 30, 38, 46, 55, 65, 76, 88, 101, 115, 130, 146,
  163, 181, 200, 220, 240, 260. **Vida** soma metade do nível (para cima) por escolha, e
  cresce a cada nível.
- Medido: um nível acima vence de 55% a 91% (antes, 50% a 97%). O pico que sobrou, nos
  níveis 13 e 14, é a proficiência e o +2 de atributo chegando juntos, numa luta que já é
  longa. Testado e descartado: tirar a Resistência ganha por nível achata a curva (máximo
  74%), mas encurta a luta do nível 20 de 11 para 8 rodadas, e o usuário pediu luta longa
  no fim. Também descartado: o preço da vida paga por nível (1d4 + metade do nível) em vez
  de por Grau — o pico do nível 13 subia para 92%.
- **Os saltos de Posto ficaram**, como pedido: o Bronze de nível 8 vence o Prata de nível
  9 (uma Convicção) 6% das vezes; ninguém de nível 14 vence a elite de nível 15.
- **Figurantes refeitos.** Com a tabela antiga, um bando de seis derrubava um personagem de
  nível 1 em 94% das vezes, e a luta durava 9 rodadas (o livro dizia 2 ou 3). Agora cada
  nível tem a sua linha (DEF 11 + nível ÷ 3, ataque proficiência + 2, dano fixo de um
  quinto da base de PV), o golpe comum derruba dois figurantes, a técnica de alvo único
  três e a de área o bando inteiro. Medido: seis figurantes custam de 15% a 30% dos PV em 2
  a 4 rodadas, e quase ninguém cai.
- **Aliado de luta: metade do nível do grupo, metade dos PV, e não conta para Sozinho
  contra muitos.** Dois níveis abaixo e com os PV inteiros, com os níveis agora próximos,
  ele virava um segundo personagem: 96% contra um rival que o personagem venceria na
  metade das vezes. Testado e descartado: contá-lo como oponente do chefe (um aliado fraco
  deixava o grupo pior do que sem ele). Agora, 68% a 72%; com o grupo contra um Ouro, +10
  a +15 pontos.
- **A tabela rápida** traz o Cosmo (começa, piso, Teto — com as escolhas de Cosmo; antes
  o livro mandava usar o Teto da tabela de níveis, que não tem as escolhas), não traz
  características (o Mestre soma as dele) e vai do nível 1 ao 20. As fichas prontas mostram
  o piso, e a defesa treinada vem da escolha de nível (antes, do nível 10 em diante, sem
  escolha).
- **A tabela de dificuldade** foi medida de novo, com uma linha a mais: o rival um nível
  acima é "difícil" (12% a 35%); dois níveis acima, "muito difícil" (4% a 24%). O aviso
  da fronteira de Grau virou o aviso da fronteira de Posto.
- `sim/mestre.py` mede tudo isso e escreve `sim/MESTRE.md`; `test.py mestre` confere cada
  frase das fichas prontas.

## O Cosmo não acaba, e a progressão é escolhida (0.6.0)

- **O Cosmo não acaba** (pedido do usuário: "diferente de ASD, o cosmo simplesmente não
  pode acabar; Seiya e os outros podem lançar seus ataques mesmo muito debilitados").
  Escolhido entre três opções: piso + a vida paga. Gastar nunca leva o Cosmo abaixo do
  piso; o que falta de uma técnica a vida paga, sem limite (1d4 por ponto × Grau); se o
  preço passar da vida que resta, o golpe sai — derrubou, você fica com 1 PV; não
  derrubou, você cai. Queimar deixa o Cosmo no piso, não em zero.
- **O piso é 1, não o Atributo do Cosmo.** A opção escolhida falava no Atributo do Cosmo,
  mas medido assim a técnica média saía de graça toda rodada para quem tinha SAB alta, e a
  build de Cosmo vencia 72% a 77%. Com piso 1 (+1 a cada duas escolhas de Cosmo), 47% a 52%.
- **O último golpe que derruba deixa você de pé.** Na primeira versão, os dois caíam juntos
  e 16% das lutas do nível 1 terminavam empatadas; agora, nenhuma.
- **Só PV e Cosmo** — como já era; nada de SP e MP como na Ascensão.
- **Progressão por escolha** (pedido do usuário): todo nível, Vida (+2 PV por Grau) ou Cosmo
  (+1 Teto, +1 Cosmo inicial, +1 piso a cada duas); nos níveis pares a partir do 4,
  técnica nova ou +2 num atributo; nos 3, 7, 11, 15 e 19, perícia ou defesa. Saíram os
  ganhos fixos Cosmo Desperto, Cosmo Sereno e Terceira defesa treinada, e os aumentos de
  atributo fixos. Medido: só Vida contra só Cosmo, 41% a 61%.
- **Curta no começo, longa no fim** (pedido do usuário): PV base por Grau de 14, 40, 80,
  135 e 205. A luta com Convicções vai de 4,7 rodadas no nível 1 a 10,8 no nível 20. Custo:
  o salto de Grau cresceu (um nível acima nas fronteiras vence 92% a 97%), e em luta longa o
  favorito vence mais — no duelo justo, o Bronze não vence mais o Ouro.
- **Guerra dos Mil Dias com 16 a 20.** Com técnica quase toda rodada, qualquer natural
  igual travava metade das lutas entre Ouros; com 16 a 20, 9% a 15%.
- **Sozinho contra muitos, de novo:** PV × 1¼ a 2¼ e golpes comuns a mais (não ações
  livres — com o Cosmo que não acaba, uma ação livre é uma técnica a mais e o chefe não
  perdia). Quatro Bronzes contra um Ouro: 43% a 51%. A luta é longa: 12 a 17 rodadas.
- **Constelação viva e Coração de estrela mudaram de efeito.** Curar PV na hora de levantar
  valia demais no nível 13 (64%), mesmo pouca cura: +1 no acerto no Sétimo e Vantagem no
  ataque depois de levantar. O simulador ainda dava à Constelação +1 de Teto que o livro
  não tinha; corrigido.

## Características da armadura (0.5.0)

- **Pedido do usuário:** "quero mais características de armaduras". Onze características
  (Couraça grossa, Espinhos, Espelhada, Pesada, Leve, Ressonante, Constelação viva,
  Coração de estrela, Cortante, Ofuscante, Elmo fechado): 1 no Bronze, 2 na Prata, 3 na
  elite; a cada forma nova, dá para trocar uma. Mais um traço de origem de graça, que não
  mexe na luta.
- **Cada uma é um empurrão**: medidas uma a uma, vencem 45% a 62% contra a mesma armadura
  sem ela. Na primeira versão, +2 de Resistência e +1 de Teto não mudavam nada (44% a
  52%); Espinhos de 1d4 por Grau a cada golpe e Espelhada devolvendo metade chegavam a 73%
  e 68%. Foram refeitas até caberem na faixa. "Guarda alta" (+1 no Bloquear) saiu: o
  simulador não a mediria.
- **Sozinho contra muitos, recalibrado**: com as características, as que protegem pesam
  mais num chefe (ele leva muitos ataques). Os PV passaram de × (n+1)/2 para × (n/2 + ¼).
  Medido com características típicas (1 no Bronze, 3 no Ouro): quatro Bronzes vencem um
  Ouro 38% a 42%.
- Os lutadores de referência do simulador agora têm as características típicas do Posto
  (Ressonante; mais Ofuscante na Prata; mais Pesada na elite). Com elas o Bronze vence o
  Prata 9% a 13% e o Ouro 0% a 2%.

## Teste de estresse (0.4.0)

`sim/extremos.py` tenta quebrar o sistema e escreve `sim/EXTREMOS.md`. O usuário pediu
"testa tudo em condições extremas, veja se tá balanceado". O que ele achou e o que mudou:

- **Grupo contra um era um massacre.** Três Bronzes venciam um Ouro do mesmo nível 92%;
  quatro, 100%. A regra de bolso do livro ("cada personagem a mais vale dois níveis")
  estava errada: o segundo personagem valia uns seis. Nova regra, **Sozinho contra
  muitos**: inimigo com Convicção, sozinho contra 2+ personagens, tem PV × (oponentes + 1)
  ÷ 2 e metade dos oponentes em ações a mais por rodada. Medido: quatro Bronzes contra um
  Ouro do mesmo nível, 47% a 48%, com uns três caindo. Testadas e descartadas: só PV × n
  (quatro Bronzes ainda venciam 69% a 77%), PV × n com uma ação por oponente (o Ouro
  nunca perdia), só ações (quatro Bronzes, 86% a 93%).
- **DES decidia tudo.** Acerto, dano e DEF no mesmo atributo; quem lutava pelo Cosmo
  vencia 21% a 38%. Agora a DEF usa a DES ou o Atributo do Cosmo (o maior) e o golpe
  comum pode usar o Atributo do Cosmo: 39% a 59%. A CON na frente continua perdendo
  (25% a 49%) — o livro avisa em vez de mudar.
- **Atordoar decidia a luta** (até 89%): o alvo perdia turnos seguidos com Vantagem
  contra ele. Agora uma condição forte que acabou não volta com a mesma técnica naquela
  luta ("o mesmo golpe não funciona duas vezes") e o Atordoado não dá mais Vantagem:
  48% a 60%. Testado e descartado: condição forte de um turno só (caía para 5% a 24%).
- **Condições médias não são fracas**: usadas uma vez, 38% a 59%. O que perde é repeti-las
  toda rodada. O livro avisa.
- **Limitações não são brecha**: uma limitação, 28% a 56%; duas, 18% a 46%. "Causa 1d6
  em você" passou a 1d6 por Grau (1d6 fixo não pesava no nível alto). "Exige carregar"
  deixou de gastar a ação inteira: no turno anterior, só não se usa técnica (antes, 19%
  a 27%).
- **Fronteira de Grau**: nos níveis 5, 9, 13 e 17, um nível acima vence 69% a 84% (nos
  outros, 46% a 66%). É o salto de dano e de PV do Grau, que é o coração do motor de
  técnicas; ficou como está, e o livro manda contar o inimigo que cruzou a fronteira como
  dois degraus mais difícil.
- Sem problema: acessórios (40% a 51%), políticas extremas (41% a 58%), quatro
  Convicções em vez de três (sem diferença, só se levanta uma vez), Centelhas (uma por
  rodada é melhor que três de uma vez, porque cada uma dá uma Vantagem), duração (nenhuma
  luta chega ao limite de 40 rodadas).

## Pendências

- Grupo contra grupo (hoje: duelo e grupo contra um).
- Princípio da constelação: um comportamento pequeno por constelação, medido como as
  características (adiado na 0.8.0).
- Playtest humano das lutas de grupo contra a elite e do nível alto.
- Um milagre possível para o Bronze contra o Ouro no duelo, se a mesa quiser.
- Conferir no mangá a mudança de forma da armadura de Pégaso na Ilha da Rainha da
  Morte.
- Do playtest (`regras/playtest-01.md`): tudo entrou na 0.10.0 e na 0.11.0. Falta jogar de novo —
  principalmente o Sétimo no nível 5, o veneno e a armadura emprestada.
- Nome do sistema: **Sangue e Estrelas** (decidido).
