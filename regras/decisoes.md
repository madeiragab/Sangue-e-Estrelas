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
  (sentido, levantar ou queimar) + uma Convicção dita antes de rolar.
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
- **Restaurar tem teste** (Ofício CD 14 + 2 × Versão), tempo e metal por Posto.
- **Estilo clássico (urna) ou Ômega (pedra):** só visual. **Sem sistema
  elemental** do Ômega (a própria série abandonou na segunda metade).
- **Reviver com sangue, em terços:** 1/3 do sangue de uma pessoa por armadura; o
  Shiryu quase morreu porque reviver duas custou 2/3 (Seiyapedia, página do Mu).
- **A escada do sangue segue o mangá:** primeiro sangue de Cavaleiro (até três
  vezes, e a armadura muda de forma a cada uma — a de Pégaso tem 5 versões no
  mangá e 3 no anime), depois sangue de Ouro, depois sangue de deus.
- **Cada forma nova é mais forte** (0.3.0): pedido do usuário, com bônus maior
  para o sangue de elite e maior ainda para o de deus. Guerreiro +1 DEF e +1 de
  Resistência; elite +2 e +2; deus +3 e +3. Medido: a armadura de Bronze com as cinco
  formas vence um Ouro de 19% a 25% — chega perto, não iguala.
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

## Pendências

- Medir lutas de grupo contra um inimigo só; hoje só o duelo está medido.
- Conferir no mangá a mudança de forma da armadura de Pégaso na Ilha da Rainha da
  Morte.
- Nome do sistema: **Sangue e Estrelas** (decidido).
