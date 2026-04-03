"""
Assistente interativo do Mago Compositor — guia o usuário passo a passo.
Interactive Mago Compositor wizard — guides the user step by step.
"""

from __future__ import annotations

import sys
from typing import Optional

from .compositor import MagoCompositor
from .models import Compasso, Escala


BANNER = r"""
╔══════════════════════════════════════════════════════════╗
║   🎩  MAGO COMPOSITOR  —  o-Maestro ViralLab  🎶        ║
║      Seu assistente mágico de composição musical         ║
╚══════════════════════════════════════════════════════════╝
"""

SEPARADOR = "──────────────────────────────────────────────────────────"


def _imprimir(texto: str = "") -> None:
    print(texto)


def _perguntar(pergunta: str, padrao: str = "") -> str:
    sufixo = f" [{padrao}]" if padrao else ""
    try:
        resposta = input(f"  ➤  {pergunta}{sufixo}: ").strip()
    except (EOFError, KeyboardInterrupt):
        _imprimir("\n\n✨ Até a próxima, maestro!")
        sys.exit(0)
    return resposta if resposta else padrao


def _escolher_opcao(titulo: str, opcoes: list[str], padrao: Optional[str] = None) -> str:
    """Exibe uma lista numerada e retorna a opção escolhida."""
    _imprimir(f"\n  {titulo}")
    for i, op in enumerate(opcoes, 1):
        _imprimir(f"    {i}. {op}")

    padrao_idx = None
    if padrao and padrao in opcoes:
        padrao_idx = str(opcoes.index(padrao) + 1)

    while True:
        resposta = _perguntar("Escolha o número", padrao_idx or "1")
        try:
            idx = int(resposta) - 1
            if 0 <= idx < len(opcoes):
                return opcoes[idx]
        except ValueError:
            pass
        _imprimir(f"  ⚠  Opção inválida. Digite um número entre 1 e {len(opcoes)}.")


def _confirmar(pergunta: str, padrao: bool = True) -> bool:
    sufixo = "[S/n]" if padrao else "[s/N]"
    resposta = _perguntar(f"{pergunta} {sufixo}").lower()
    if not resposta:
        return padrao
    return resposta in ("s", "sim", "y", "yes")


class WizardMago:
    """
    Assistente interativo que guia o usuário na criação de uma composição.
    Interactive wizard that guides the user through creating a composition.
    """

    def __init__(self) -> None:
        self._mago = MagoCompositor()

    # ------------------------------------------------------------------
    # Passo a passo / Step by step
    # ------------------------------------------------------------------

    def _passo_titulo(self) -> str:
        _imprimir(f"\n{SEPARADOR}")
        _imprimir("  🎵  PASSO 1 de 5 — Título da composição")
        _imprimir(SEPARADOR)
        return _perguntar("Como se chamará sua música?", "Minha Composição Viral")

    def _passo_estilo(self) -> str:
        _imprimir(f"\n{SEPARADOR}")
        _imprimir("  🎸  PASSO 2 de 5 — Estilo musical")
        _imprimir(SEPARADOR)
        estilos = self._mago.listar_estilos()
        return _escolher_opcao("Qual estilo você quer?", estilos, padrao="pop")

    def _passo_tonalidade(self) -> tuple[str, Escala]:
        _imprimir(f"\n{SEPARADOR}")
        _imprimir("  🎹  PASSO 3 de 5 — Tonalidade e escala")
        _imprimir(SEPARADOR)

        tonalidades = self._mago.listar_tonalidades()
        tonalidade = _escolher_opcao("Qual a tonalidade?", tonalidades, padrao="C")

        escalas = self._mago.listar_escalas()
        nomes_escalas = [e.value for e in escalas]
        escala_nome = _escolher_opcao("Qual a escala?", nomes_escalas, padrao="maior")
        escala = next(e for e in escalas if e.value == escala_nome)

        return tonalidade, escala

    def _passo_ritmo(self, estilo: str) -> tuple[Compasso, int]:
        _imprimir(f"\n{SEPARADOR}")
        _imprimir("  🥁  PASSO 4 de 5 — Compasso e BPM")
        _imprimir(SEPARADOR)

        compassos = list(Compasso)
        nomes_comp = [c.value for c in compassos]
        comp_nome = _escolher_opcao("Qual o compasso?", nomes_comp, padrao="4/4")
        compasso = next(c for c in compassos if c.value == comp_nome)

        bpm_min, bpm_max = self._mago.sugerir_bpm(estilo)
        _imprimir(f"  💡 BPM sugerido para {estilo}: {bpm_min}–{bpm_max}")
        bpm_str = _perguntar("BPM desejado", str((bpm_min + bpm_max) // 2))
        try:
            bpm = max(40, min(300, int(bpm_str)))
        except ValueError:
            bpm = (bpm_min + bpm_max) // 2

        return compasso, bpm

    def _passo_extras(self) -> tuple[bool, bool, int]:
        _imprimir(f"\n{SEPARADOR}")
        _imprimir("  ✨  PASSO 5 de 5 — Opções extras")
        _imprimir(SEPARADOR)

        melodia = _confirmar("Gerar melodia sugerida?", padrao=True)
        letra = _confirmar("Sugerir verso de letra?", padrao=True)

        rep_str = _perguntar("Quantas repetições da progressão?", "2")
        try:
            repeticoes = max(1, min(8, int(rep_str)))
        except ValueError:
            repeticoes = 2

        return melodia, letra, repeticoes

    # ------------------------------------------------------------------
    # Execução principal / Main execution
    # ------------------------------------------------------------------

    def executar(self) -> None:
        """Executa o assistente interativo completo."""
        _imprimir(BANNER)
        _imprimir("  Bem-vindo(a) ao Mago Compositor!")
        _imprimir("  Vou te guiar na criação de uma composição musical viral.")
        _imprimir("  Pressione Ctrl+C a qualquer momento para sair.\n")

        titulo = self._passo_titulo()
        estilo = self._passo_estilo()
        tonalidade, escala = self._passo_tonalidade()
        compasso, bpm = self._passo_ritmo(estilo)
        incluir_melodia, incluir_letra, repeticoes = self._passo_extras()

        _imprimir(f"\n{SEPARADOR}")
        _imprimir("  🎩 O Mago está compondo sua música...")
        _imprimir(SEPARADOR)

        composicao = self._mago.compor(
            titulo=titulo,
            estilo=estilo,
            tonalidade=tonalidade,
            escala=escala,
            compasso=compasso,
            bpm=bpm,
            incluir_melodia=incluir_melodia,
            incluir_letra=incluir_letra,
            repeticoes=repeticoes,
        )

        _imprimir(f"\n{SEPARADOR}")
        _imprimir("  ✅  Sua composição está pronta!\n")
        _imprimir(str(composicao))
        _imprimir(f"\n{SEPARADOR}")
        _imprimir("  🎶 Boa sorte com sua música viral, maestro!")
        _imprimir(SEPARADOR + "\n")
