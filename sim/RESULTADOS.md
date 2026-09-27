# Resultados do simulador

Gerado por `python sim/cenarios.py`. Cada célula é a média de 1500 duelos com sementes fixas. Os lutadores são montados pelo livro: 15/14/13/12/10/8 com DES e CON na frente, duas técnicas de dano (a grande, no tamanho máximo, e uma pequena) e a política de jogo escrita em `sim/luta.py`.

## A luta ao longo dos níveis

Espelho de Bronze contra Bronze. *Rodadas* é a duração média da luta; *com Convicções* quer dizer que os dois podem levantar uma vez.

| Nível | PV | Rodadas, com Convicções | Rodadas, sem | Dano vindo de técnicas | Quem não usa técnica vence |
|---:|---:|---:|---:|---:|---:|
| 1 | 20 | 7.7 | 5.2 | 80% | 35% |
| 4 | 29 | 9.5 | 7.2 | 75% | 29% |
| 5 | 48 | 8.2 | 5.5 | 81% | 14% |
| 8 | 57 | 9.8 | 6.8 | 76% | 17% |
| 9 | 76 | 6.3 | 4.0 | 78% | 31% |
| 12 | 85 | 6.6 | 4.3 | 78% | 33% |
| 13 | 104 | 5.7 | 3.9 | 83% | 16% |
| 16 | 129 | 7.0 | 5.1 | 75% | 12% |
| 17 | 149 | 6.2 | 4.4 | 80% | 7% |
| 20 | 181 | 8.4 | 6.6 | 77% | 4% |

## Regra por regra

Porcentagem de vitórias do primeiro lutador. O espelho deve ficar perto de 50%; o resto mostra quanto cada escolha vale. O traço é um Posto que não existe naquele nível: Prata só a partir do 9, elite só a partir do 15.

| Confronto | Nível 1 | Nível 5 | Nível 9 | Nível 13 | Nível 15 | Nível 17 | Nível 20 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Espelho: Bronze contra Bronze | 48% | 48% | 48% | 50% | 47% | 49% | 49% |
| Quem não apara a armadura | 41% | 36% | 34% | 46% | 45% | 39% | 27% |
| Quem nunca queima | 41% | 43% | 41% (5% emp.) | 51% | 46% | 49% | 49% |
| Quem nunca levanta | 8% | 5% | 4% | 1% | 1% | 0% | 0% |
| Prata contra Bronze | — | — | 77% | 78% | 82% | 82% | 86% |
| Bronze contra Prata | — | — | 19% | 19% | 15% | 17% | 12% |
| Prata contra Ouro | — | — | — | — | 6% (8% emp.) | 6% (6% emp.) | 4% (9% emp.) |
| Um nível acima | 55% | 50% (6% emp.) | 51% | 52% | 61% | 53% | — |
| Dois níveis acima | 61% | 54% (5% emp.) | 53% | 63% | 79% | 62% | — |
| Bronze sozinho contra Ouro | — | — | — | — | 3% (6% emp.) | 3% (6% emp.) | 3% (7% emp.) |
| Bronze com uma Centelha por rodada contra Ouro | — | — | — | — | 3% (10% emp.) | 4% (6% emp.) | 3% (9% emp.) |
| Bronze que se cega contra Ouro | — | — | — | — | 2% (5% emp.) | 2% (7% emp.) | 1% (8% emp.) |
| Armadura revivida três vezes (V4) contra a original | 60% | 58% (6% emp.) | 57% | 60% | 63% | 60% | 63% |
| V4 com a forma de elite contra a original | 66% | 63% | 64% | 65% | 67% | 66% | 71% |
| Bronze V4 com a forma de elite contra Ouro | — | — | — | — | 9% (6% emp.) | 9% (7% emp.) | 5% (9% emp.) |
| Bronze com as cinco formas, até a de deus, contra Ouro | — | — | — | — | 14% (7% emp.) | 16% (8% emp.) | 11% (10% emp.) |
| Prata revivida quatro vezes contra a original | — | — | 58% (6% emp.) | 58% | 61% | 60% | 61% |
| Prata com a escada inteira (quatro, elite, deus) contra Ouro | — | — | — | — | 21% (7% emp.) | 23% (8% emp.) | 16% (9% emp.) |
| Ouro revivido seis vezes contra o original | — | — | — | — | 58% (13% emp.) | 60% (11% emp.) | 60% (15% emp.) |
| Garras contra nenhum acessório | 45% | 45% (5% emp.) | 49% (5% emp.) | 51% | 50% | 52% | 51% |
| Escudo contra nenhum acessório | 41% | 47% (5% emp.) | 46% (5% emp.) | 49% | 51% | 50% | 51% |

## Guerra dos Mil Dias

Em quantas lutas os Cosmos travam num choque de técnicas.

| Confronto | Nível 1 | Nível 5 | Nível 9 | Nível 13 | Nível 15 | Nível 17 | Nível 20 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Ouro contra Ouro | — | — | — | — | 14% | 14% | 15% |
| Bronze contra Bronze | 5% | 4% | 6% | 3% | 3% | 3% | 3% |
