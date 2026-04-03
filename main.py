"""
Ponto de entrada do Mago Compositor.
Entry point for the Mago Compositor.

Uso / Usage:
    python main.py              # wizard interativo / interactive wizard
    python main.py --help       # ajuda / help
    python main.py --demo       # composição de demonstração / demo composition
"""

from __future__ import annotations

import argparse
import sys

from mago_compositor import MagoCompositor, WizardMago
from mago_compositor.models import Compasso, Escala


def _demo() -> None:
    """Executa uma composição de demonstração sem interação do usuário."""
    mago = MagoCompositor(semente=42)
    composicao = mago.compor(
        titulo="Sonho Viral",
        estilo="pop",
        tonalidade="C",
        escala=Escala.MAIOR,
        compasso=Compasso.QUATRO_QUARTOS,
        bpm=110,
        incluir_melodia=True,
        incluir_letra=True,
    )
    print("\n🎩 Composição de demonstração:\n")
    print(composicao)
    print()


def _listar() -> None:
    """Lista estilos, tonalidades e escalas disponíveis."""
    mago = MagoCompositor()
    print("\n🎸  Estilos disponíveis:")
    for e in mago.listar_estilos():
        bpm_min, bpm_max = mago.sugerir_bpm(e)
        print(f"   • {e:<10}  BPM: {bpm_min}–{bpm_max}")
    print("\n🎹  Tonalidades disponíveis:")
    print("   " + "  ".join(mago.listar_tonalidades()))
    print("\n🎼  Escalas disponíveis:")
    for escala in mago.listar_escalas():
        print(f"   • {escala.value}")
    print()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="mago-compositor",
        description="🎩 Mago Compositor — assistente mágico de composição musical viral",
    )
    parser.add_argument(
        "--demo", action="store_true",
        help="Exibe uma composição de demonstração",
    )
    parser.add_argument(
        "--listar", action="store_true",
        help="Lista estilos, tonalidades e escalas disponíveis",
    )
    args = parser.parse_args(argv)

    if args.demo:
        _demo()
        return 0

    if args.listar:
        _listar()
        return 0

    # Modo padrão: wizard interativo
    WizardMago().executar()
    return 0


if __name__ == "__main__":
    sys.exit(main())
