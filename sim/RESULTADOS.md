# Resultados do simulador

Gerado por `python sim/cenarios.py`. Cada célula é a média de 1500 duelos com sementes fixas. Os lutadores são montados pelo livro: 15/14/13/12/10/8 com DES e CON na frente, duas técnicas de dano (a grande, no tamanho máximo, e uma pequena) e a política de jogo escrita em `sim/luta.py`.

## A luta ao longo dos níveis

Espelho de Bronze contra Bronze. *Rodadas* é a duração média da luta; *com Convicções* quer dizer que os dois podem levantar uma vez.

| Nível | PV | Rodadas, com Convicções | Rodadas, sem | Dano vindo de técnicas | Quem não usa técnica vence |
|---:|---:|---:|---:|---:|---:|
| 1 | 16 | 4.7 | 2.9 | 91% | 35% |
| 4 | 42 | 4.9 | 3.1 | 97% | 16% |
| 5 | 54 | 6.1 | 4.6 | 95% | 14% |
| 8 | 97 | 6.4 | 4.9 | 94% | 4% |
| 9 | 114 | 7.6 | 6.0 | 100% | 8% |
| 12 | 175 | 5.9 | 4.2 | 100% | 5% |
| 13 | 198 | 6.5 | 4.8 | 100% | 1% |
| 16 | 277 | 8.4 | 5.5 | 99% | 1% |
| 17 | 306 | 9.3 | 6.2 | 99% | 0% |
| 20 | 420 | 11.1 | 7.7 | 99% | 0% |

## Regra por regra

Porcentagem de vitórias do primeiro lutador. O espelho deve ficar perto de 50%; o resto mostra quanto cada escolha vale. O traço é um Posto que não existe naquele nível: Prata só a partir do 9, elite só a partir do 15.

| Confronto | Nível 1 | Nível 5 | Nível 9 | Nível 13 | Nível 15 | Nível 17 | Nível 20 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Espelho: Bronze contra Bronze | 50% | 51% | 51% | 50% | 50% | 51% | 49% |
| Quem não apara a armadura | 54% | 45% | 40% | 24% | 16% | 16% | 12% |
| Quem nunca queima | 47% | 45% | 42% | 34% | 42% | 49% | 51% |
| Quem nunca levanta | 6% | 8% | 14% | 10% | 3% | 1% | 1% |
| Prata contra Bronze | — | — | 89% | 90% | 91% | 91% | 90% |
| Bronze contra Prata | — | — | 11% | 11% | 8% | 8% | 6% |
| Prata contra Ouro | — | — | — | — | 0% | 0% | 0% |
| Um nível acima | 70% | 73% | 76% | 89% | 71% | 66% | — |
| Dois níveis acima | 79% | 81% | 88% | 95% | 89% | 76% | — |
| Bronze sozinho contra Ouro | — | — | — | — | 0% | 0% | 0% |
| Bronze com uma Centelha por rodada contra Ouro | — | — | — | — | 0% | 0% | 0% |
| Bronze que se cega contra Ouro | — | — | — | — | 0% | 0% | 0% |
| Armadura revivida três vezes (V4) contra a original | 59% | 65% | 64% | 62% | 66% | 66% | 67% |
| V4 com a forma de elite contra a original | 65% | 67% | 69% | 67% | 72% | 73% | 74% |
| Bronze V4 com a forma de elite contra Ouro | — | — | — | — | 1% | 0% | 0% |
| Bronze com as cinco formas, até a de deus, contra Ouro | — | — | — | — | 3% | 1% | 0% |
| Prata revivida quatro vezes contra a original | — | — | 65% | 64% | 67% | 66% | 64% |
| Prata com a escada inteira (quatro, elite, deus) contra Ouro | — | — | — | — | 7% | 2% | 2% (5% emp.) |
| Ouro revivido seis vezes contra o original | — | — | — | — | 69% (9% emp.) | 71% (11% emp.) | 69% (13% emp.) |
| Garras contra nenhum acessório | 49% | 50% | 51% | 49% | 48% | 51% | 47% |
| Escudo contra nenhum acessório | 47% | 49% | 51% | 49% | 48% | 48% | 46% |

## Guerra dos Mil Dias

Em quantas lutas os Cosmos travam num choque de técnicas.

| Confronto | Nível 1 | Nível 5 | Nível 9 | Nível 13 | Nível 15 | Nível 17 | Nível 20 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Ouro contra Ouro | — | — | — | — | 11% | 13% | 17% |
| Bronze contra Bronze | 1% | 1% | 1% | 1% | 3% | 2% | 2% |
