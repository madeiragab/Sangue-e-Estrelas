# Resultados do simulador

Gerado por `python sim/cenarios.py`. Cada célula é a média de 1500 duelos com sementes fixas. Os lutadores são montados pelo livro: 15/14/13/12/10/8 com DES e CON na frente, duas técnicas de dano (a grande, no tamanho máximo, e uma pequena) e a política de jogo escrita em `sim/luta.py`.

## A luta ao longo dos níveis

Espelho de Bronze contra Bronze. *Rodadas* é a duração média da luta; *com Convicções* quer dizer que os dois podem levantar uma vez.

| Nível | PV | Rodadas, com Convicções | Rodadas, sem | Dano vindo de técnicas | Quem não usa técnica vence |
|---:|---:|---:|---:|---:|---:|
| 1 | 16 | 4.7 | 2.9 | 91% | 35% |
| 4 | 26 | 6.7 | 5.0 | 93% | 28% |
| 5 | 58 | 6.2 | 4.7 | 95% | 13% |
| 8 | 72 | 6.4 | 4.6 | 93% | 10% |
| 9 | 122 | 7.7 | 6.0 | 100% | 6% |
| 12 | 140 | 8.8 | 7.3 | 100% | 9% |
| 13 | 209 | 6.5 | 4.7 | 100% | 1% |
| 16 | 231 | 7.3 | 4.9 | 99% | 1% |
| 17 | 319 | 9.0 | 6.0 | 99% | 0% |
| 20 | 365 | 10.8 | 7.4 | 99% | 0% |

## Regra por regra

Porcentagem de vitórias do primeiro lutador. O espelho deve ficar perto de 50%; o resto mostra quanto cada escolha vale. O traço é um Posto que não existe naquele nível: Prata só a partir do 9, elite só a partir do 15.

| Confronto | Nível 1 | Nível 5 | Nível 9 | Nível 13 | Nível 15 | Nível 17 | Nível 20 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Espelho: Bronze contra Bronze | 50% | 49% | 51% | 49% | 48% | 50% | 49% |
| Quem não apara a armadura | 54% | 43% | 40% | 25% | 24% | 15% | 13% |
| Quem nunca queima | 47% | 45% | 45% | 33% | 41% | 49% | 48% |
| Quem nunca levanta | 6% | 7% | 13% | 10% | 10% | 2% | 1% |
| Prata contra Bronze | — | — | 89% | 88% | 87% | 92% | 92% |
| Bronze contra Prata | — | — | 12% | 11% | 12% | 8% | 7% |
| Prata contra Ouro | — | — | — | — | 1% | 0% | 0% |
| Um nível acima | 61% | 65% | 67% | 71% | 57% | 59% | — |
| Dois níveis acima | 61% | 70% | 70% | 71% | 94% | 59% | — |
| Bronze sozinho contra Ouro | — | — | — | — | 0% | 0% | 0% |
| Bronze com uma Centelha por rodada contra Ouro | — | — | — | — | 0% | 0% | 0% |
| Bronze que se cega contra Ouro | — | — | — | — | 0% | 0% | 0% |
| Armadura revivida três vezes (V4) contra a original | 59% | 59% | 65% | 62% | 64% | 65% | 68% |
| V4 com a forma de elite contra a original | 65% | 68% | 68% | 69% | 70% | 74% | 73% |
| Bronze V4 com a forma de elite contra Ouro | — | — | — | — | 1% | 0% | 0% |
| Bronze com as cinco formas, até a de deus, contra Ouro | — | — | — | — | 4% | 0% | 0% |
| Prata revivida quatro vezes contra a original | — | — | 64% | 62% | 63% | 67% | 64% |
| Prata com a escada inteira (quatro, elite, deus) contra Ouro | — | — | — | — | 11% | 2% | 2% |
| Ouro revivido seis vezes contra o original | — | — | — | — | 68% (8% emp.) | 70% (10% emp.) | 71% (11% emp.) |
| Garras contra nenhum acessório | 49% | 50% | 50% | 49% | 49% | 50% | 48% |
| Escudo contra nenhum acessório | 47% | 50% | 50% | 53% | 48% | 48% | 47% |

## Guerra dos Mil Dias

Em quantas lutas os Cosmos travam num choque de técnicas.

| Confronto | Nível 1 | Nível 5 | Nível 9 | Nível 13 | Nível 15 | Nível 17 | Nível 20 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Ouro contra Ouro | — | — | — | — | 9% | 15% | 14% |
| Bronze contra Bronze | 1% | 1% | 1% | 1% | 1% | 2% | 2% |
