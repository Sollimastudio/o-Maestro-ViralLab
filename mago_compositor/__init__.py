"""
Mago Compositor — assistente mágico de composição musical viral.
Mago Compositor — magical viral music composition assistant.
"""

from .compositor import MagoCompositor
from .models import (
    Acorde,
    Compasso,
    Composicao,
    Escala,
    Melodia,
    Nota,
    Progressao,
)
from .wizard import WizardMago

__all__ = [
    "MagoCompositor",
    "WizardMago",
    "Composicao",
    "Progressao",
    "Melodia",
    "Acorde",
    "Nota",
    "Escala",
    "Compasso",
]

__version__ = "1.0.0"
