# Sangue e Estrelas — RPG de mesa

Projeto de fã de RPG de mesa inspirado em *Os Cavaleiros do Zodíaco*. Um sistema
d20 em que o Cosmo cresce durante a luta, o Sétimo Sentido tem preço e a
armadura quebra, morre e volta com sangue.

**No ar:** https://madeiragab.github.io/sangue-e-estrelas/

> **Aviso de independência:** projeto de fã, não oficial e sem fins lucrativos.
> *Os Cavaleiros do Zodíaco* (*Saint Seiya*) e os elementos próprios dessa
> franquia pertencem a Masami Kurumada e aos seus respectivos titulares e
> licenciados, incluindo Shueisha, Toei Animation e Bandai. Este projeto não é
> afiliado, aprovado ou patrocinado por eles.

**Versão atual:** 0.1.0 · 27/09/2026 · [Changelog](CHANGELOG.md)

---

## O livro

Um livro só, para jogador e Mestre: [livro.html](https://madeiragab.github.io/sangue-e-estrelas/livro.html).

| | Capítulo | Conteúdo |
|---|---|---|
| I | Antes de tudo | O que é o jogo e o que você precisa |
| II | Como se joga | O d20, a dificuldade e os cinco números da ficha |
| III | Criação de personagem | Nove etapas, sem classes |
| IV | Cosmo e Sentidos | O Cosmo que cresce, queimar, o Sétimo, a Guerra dos Mil Dias, o Oitavo, o Nono, os cinco sentidos e as Centelhas |
| V | Combate | Ações, "o mesmo golpe não funciona duas vezes", cair e levantar, condições |
| VI | Técnicas | O motor para criar as suas, evolução e o Golpe do Assento |
| VII | Armaduras e itens | Peças, caixas, morte e a escada do sangue |
| VIII | Exércitos | O molde e quatro exércitos de exemplo |
| IX | Subir de nível | Do 1 ao 20 |
| X | Uma ficha pronta | Um personagem inteiro, um modelo de ficha e a consulta rápida |

## Como o sistema funciona, em cinco linhas

- **A rolagem** é `1d20 + modificador (+ proficiência)` contra um alvo. Quem causa rola.
- **O Cosmo** começa baixo e sobe a cada rodada e a cada golpe que entra. Ele paga as
  técnicas. Perder PV nunca dá Cosmo.
- **Os Sentidos** são o patamar do poder. O Ouro entra no Sétimo quando quer; o Bronze só
  no limite, e só por uma luta.
- **Os cinco sentidos** são o que você sacrifica para ir além — e cada um cobra.
- **A armadura** quebra peça por peça, pode morrer e só volta com sangue, pago em terços.

## Estrutura do repositório

| Caminho | O que é |
|---|---|
| `template/livro.html` | A casca do livro: capa, folha de rosto, sumário, colofão |
| `template/capitulos/*.html` | Um arquivo por capítulo — é aqui que as regras moram |
| `template/livro.css` | A folha de estilo |
| `build.py` | Monta o `livro.html` final, com o CSS e a capa embutidos |
| `livro.html` | O livro publicado (gerado — não edite à mão) |
| `index.html` | A página inicial do site |
| `regras/decisoes.md` | As decisões de design e de onde cada uma veio |
| `pesquisa/` | O relatório de referências e as notas da pesquisa |

## Montar o livro

```
python build.py
```

Stdlib pura, sem dependências. O script falha se sobrar um marcador sem
substituir ou se um link interno apontar para um lugar que não existe.

## Publicar

O site é servido pelo GitHub Pages a partir da raiz do branch `main`. O
`livro.html` gerado vai commitado junto, para o Pages não precisar rodar build.
