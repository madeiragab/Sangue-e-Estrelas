# Resultados do simulador

Gerado por `python sim/cenarios.py`. Cada célula é a média de 1500 duelos com sementes fixas. Os lutadores são montados pelo livro: 15/14/13/12/10/8 com DES e CON na frente, duas técnicas de dano (a grande, no tamanho máximo, e uma pequena) e a política de jogo escrita em `sim/luta.py`.

## A luta ao longo dos níveis

Espelho de Bronze contra Bronze. *Rodadas* é a duração média da luta; *com Convicções* quer dizer que os dois podem levantar uma vez.

| Nível | PV | Rodadas, com Convicções | Rodadas, sem | Dano vindo de técnicas | Quem não usa técnica vence |
|---:|---:|---:|---:|---:|---:|
| 1 | 20 | 7.9 | 5.2 | 79% | 28% |
| 4 | 29 | 10.1 | 7.2 | 74% | 27% |
| 5 | 48 | 8.2 | 5.5 | 81% | 14% |
| 8 | 57 | 9.8 | 6.8 | 76% | 17% |
| 9 | 76 | 6.3 | 4.0 | 78% | 31% |
| 12 | 85 | 6.6 | 4.3 | 78% | 34% |
| 13 | 104 | 5.7 | 3.9 | 83% | 16% |
| 16 | 129 | 6.9 | 5.0 | 76% | 12% |
| 17 | 149 | 6.2 | 4.4 | 80% | 6% |
| 20 | 181 | 8.4 | 6.6 | 77% | 5% |

## Regra por regra

Porcentagem de vitórias do primeiro lutador. O espelho deve ficar perto de 50%; o resto mostra quanto cada escolha vale. O traço é um Posto que não existe naquele nível: Prata só a partir do 9, elite só a partir do 15.

| Confronto | Nível 1 | Nível 5 | Nível 9 | Nível 13 | Nível 15 | Nível 17 | Nível 20 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Espelho: Bronze contra Bronze | 47% | 49% (5% emp.) | 47% (5% emp.) | 49% | 48% | 49% | 49% |
| Quem não apara a armadura | 38% (5% emp.) | 35% (5% emp.) | 34% | 46% | 45% | 39% | 27% |
| Quem nunca queima | 44% | 42% | 42% (5% emp.) | 52% | 47% | 50% | 48% |
| Quem nunca levanta | 7% | 5% | 4% | 1% | 1% | 0% | 0% |
| Prata contra Bronze | — | — | 58% (5% emp.) | 58% | 59% | 62% | 62% |
| Um nível acima | 57% | 50% (5% emp.) | 50% | 51% | 58% | 53% | — |
| Dois níveis acima | 61% (5% emp.) | 54% | 52% (5% emp.) | 59% | 78% | 63% | — |
| Bronze sozinho contra Ouro | — | — | — | — | 3% (6% emp.) | 3% (5% emp.) | 1% (8% emp.) |
| Bronze com uma Centelha por rodada contra Ouro | — | — | — | — | 3% (8% emp.) | 5% (7% emp.) | 4% (8% emp.) |
| Bronze que se cega contra Ouro | — | — | — | — | 2% (6% emp.) | 3% (7% emp.) | 2% (9% emp.) |
| Garras contra nenhum acessório | 47% | 47% | 50% | 47% | 52% | 51% | 51% |
| Escudo contra nenhum acessório | 47% | 48% (5% emp.) | 46% | 48% | 49% | 46% | 50% |

## Guerra dos Mil Dias

Em quantas lutas os Cosmos travam num choque de técnicas.

| Confronto | Nível 1 | Nível 5 | Nível 9 | Nível 13 | Nível 15 | Nível 17 | Nível 20 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Ouro contra Ouro | — | — | — | — | 14% | 14% | 15% |
| Bronze contra Bronze | 5% | 5% | 6% | 3% | 3% | 3% | 4% |
