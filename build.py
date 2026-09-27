"""Monta o livro de Sangue e Estrelas em um único HTML autossuficiente.

    template/livro.html          a casca: capa, folha de rosto, sumário, colofão
    template/livro.css           a folha de estilo
    template/capitulos/*.html    um arquivo por capítulo, em ordem de nome
    imagens/capa.webp            a capa, embutida no próprio HTML
    CHANGELOG.md                 de onde sai o número da versão

    ->  livro.html

Uso:  python build.py

Nada de dependência externa: é stdlib pura, para rodar em qualquer máquina.
O livro publicado não carrega nenhum arquivo de fora — a capa entra
codificada no HTML — então dá para salvar a página e abrir offline.
"""

from __future__ import annotations

import base64
import html
import pathlib
import re
import sys

RAIZ = pathlib.Path(__file__).parent
TEMPLATE = RAIZ / "template"
SAIDA = RAIZ / "livro.html"

# As tabelas de números e as fichas de inimigos saem do simulador: o livro
# imprime exatamente o que foi medido.
sys.path.insert(0, str(RAIZ / "sim"))
import inimigos  # noqa: E402

DESCRICAO = ("Sangue e Estrelas: RPG de mesa de fã inspirado em Cavaleiros do "
             "Zodíaco. d20, Cosmo que cresce na luta, os Sentidos, técnicas "
             "montadas por pontos e armaduras que revivem com sangue.")


def versao_do_changelog() -> tuple[str, str]:
    """A versão publicada é a primeira linha `## [x.y.z] - data` do CHANGELOG.

    Um número copiado em quatro lugares vira quatro números diferentes. Aqui
    só existe um: o do topo do CHANGELOG.
    """
    texto = (RAIZ / "CHANGELOG.md").read_text(encoding="utf-8")
    m = re.search(r"^## \[(\d+\.\d+\.\d+)\] - (\d{4}-\d{2}-\d{2})", texto, re.M)
    if not m:
        raise SystemExit("CHANGELOG.md sem uma linha no formato "
                         "'## [x.y.z] - AAAA-MM-DD'.")
    return m.group(1), m.group(2)


def data_br(data: str) -> str:
    a, m, d = data.split("-")
    return f"{d}/{m}/{a}"


def capa_embutida() -> str:
    dados = (RAIZ / "imagens" / "capa.webp").read_bytes()
    return "data:image/webp;base64," + base64.b64encode(dados).decode("ascii")


def capitulos() -> str:
    arquivos = sorted((TEMPLATE / "capitulos").glob("*.html"))
    if not arquivos:
        raise SystemExit("template/capitulos/ está vazio.")
    return "\n\n".join(a.read_text(encoding="utf-8").strip() for a in arquivos)


def botao_flutuante() -> str:
    """Um livro só não precisa de estante: o botão volta ao sumário e ao site."""
    return (
        '<details class="biblioteca-flutuante">'
        '<summary aria-label="Navegar pelo livro" title="Navegar">'
        '<span aria-hidden="true">✦</span></summary>'
        '<nav aria-label="Navegar pelo livro"><strong>Sangue e Estrelas</strong>'
        '<a href="#sumario"><span><b>Sumário</b><small>voltar ao índice</small></span></a>'
        '<a href="#consulta"><span><b>Consulta rápida</b><small>a folha do meio da mesa</small></span></a>'
        '<a class="estante-completa" href="index.html">Página inicial</a>'
        '</nav></details>'
    )


def aviso_independencia() -> str:
    return (
        '<aside class="aviso-independencia" role="note">'
        '<strong>Projeto de fã, não oficial e sem fins lucrativos.</strong> '
        '<span><em>Os Cavaleiros do Zodíaco</em> (<em>Saint Seiya</em>) e os '
        'elementos próprios dessa franquia pertencem a Masami Kurumada e aos '
        'seus respectivos titulares e licenciados, incluindo Shueisha, Toei '
        'Animation e Bandai. Este projeto não é afiliado, aprovado ou '
        'patrocinado por eles.</span></aside>'
    )


def envelopar(corpo_e_cabeca: str) -> str:
    """Fecha o livro num documento HTML de verdade.

    A casca começa no <title> e segue no <style>. O corte é no fim do
    </style>: o que vem antes é cabeça, o que vem depois é corpo.
    """
    marca = "</style>"
    i = corpo_e_cabeca.rindex(marca) + len(marca)
    cabeca, corpo = corpo_e_cabeca[:i], corpo_e_cabeca[i:]
    return (
        "<!doctype html>\n"
        '<html lang="pt-BR">\n<head>\n'
        '<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        f'<meta name="description" content="{html.escape(DESCRICAO, quote=True)}">\n'
        + cabeca
        + "\n</head>\n<body>\n"
        + botao_flutuante()
        + "\n"
        + corpo.strip()
        + "\n"
        + aviso_independencia()
        + "\n</body>\n</html>\n"
    )


def atualizar_versao_em(arquivo: str, padrao: str, novo: str) -> None:
    alvo = RAIZ / arquivo
    if not alvo.exists():
        return
    texto = alvo.read_text(encoding="utf-8")
    trocado = re.sub(padrao, novo, texto, count=1)
    if trocado != texto:
        alvo.write_text(trocado, encoding="utf-8")


def main() -> None:
    versao, data = versao_do_changelog()
    s = (TEMPLATE / "livro.html").read_text(encoding="utf-8")
    s = s.replace("{{CSS}}", (TEMPLATE / "livro.css").read_text(encoding="utf-8"))
    s = s.replace("{{CAPITULOS}}", capitulos())
    s = s.replace("{{CAPA}}", capa_embutida())
    s = s.replace("{{VERSAO}}", versao)
    s = s.replace("{{DATA}}", data_br(data))
    s = s.replace("{{TABELA_NIVEIS}}", inimigos.tabela_niveis())
    s = s.replace("{{TABELA_POSTO}}", inimigos.tabela_posto())
    s = s.replace("{{TABELA_FORMAS}}", inimigos.tabela_formas())
    s = s.replace("{{TABELA_CARACTERISTICAS}}", inimigos.tabela_caracteristicas())
    s = s.replace("{{TABELA_INIMIGOS}}", inimigos.tabela_rapida())
    s = re.sub(r"\{\{INIMIGO:([a-z-]+)\}\}", lambda m: inimigos.bloco(m.group(1)), s)

    faltando = set(re.findall(r"\{\{[A-Z_]+(?::[a-z-]+)?\}\}", s))
    if faltando:
        raise SystemExit(f"marcadores não substituídos: {faltando}")

    # Toda âncora do sumário e das remissões precisa existir no livro.
    ids = set(re.findall(r'\bid="([^"]+)"', s))
    quebrados = sorted({h for h in re.findall(r'href="#([^"]+)"', s)} - ids)
    if quebrados:
        raise SystemExit(f"links internos sem destino: {quebrados}")

    SAIDA.write_text(envelopar(s), encoding="utf-8")
    print(f"  livro.html  {round(SAIDA.stat().st_size / 1024)} KB  ·  versão {versao}")

    atualizar_versao_em("index.html", r"Sangue e Estrelas · versão [^·]*·",
                        f"Sangue e Estrelas · versão {versao} ·")
    atualizar_versao_em("README.md", r"(\*\*Versão atual:\*\* )[^\n]*",
                        rf"\g<1>{versao} · {data_br(data)} · [Changelog](CHANGELOG.md)")


if __name__ == "__main__":
    main()
