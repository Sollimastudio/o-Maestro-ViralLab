"""
Modelos de dados musicais para o Mago Compositor.
Musical data models for the Mago Compositor.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from enum import Enum


class Escala(Enum):
    """Escalas musicais disponíveis / Available musical scales."""
    MAIOR = "maior"
    MENOR = "menor"
    PENTATONICA_MAIOR = "pentatônica maior"
    PENTATONICA_MENOR = "pentatônica menor"
    BLUES = "blues"
    DORIA = "dórico"
    MISOLIDIA = "mixolídia"


class Compasso(Enum):
    """Compassos disponíveis / Available time signatures."""
    QUATRO_QUARTOS = "4/4"
    TRES_QUARTOS = "3/4"
    SEIS_OITAVOS = "6/8"
    DOIS_QUARTOS = "2/4"


INTERVALOS_ESCALA: dict[Escala, List[int]] = {
    Escala.MAIOR:              [0, 2, 4, 5, 7, 9, 11],
    Escala.MENOR:              [0, 2, 3, 5, 7, 8, 10],
    Escala.PENTATONICA_MAIOR:  [0, 2, 4, 7, 9],
    Escala.PENTATONICA_MENOR:  [0, 3, 5, 7, 10],
    Escala.BLUES:              [0, 3, 5, 6, 7, 10],
    Escala.DORIA:              [0, 2, 3, 5, 7, 9, 10],
    Escala.MISOLIDIA:          [0, 2, 4, 5, 7, 9, 10],
}

NOTAS_CROMATICAS = ["C", "C#", "D", "D#", "E", "F",
                    "F#", "G", "G#", "A", "A#", "B"]


@dataclass
class Nota:
    """Representa uma nota musical / Represents a musical note."""
    nome: str          # e.g. "C", "D#"
    oitava: int = 4    # 0–8
    duracao: float = 1.0  # em tempos / in beats

    @property
    def midi(self) -> int:
        """Número MIDI da nota (0-127)."""
        indice = NOTAS_CROMATICAS.index(self.nome)
        return (self.oitava + 1) * 12 + indice

    def __str__(self) -> str:
        return f"{self.nome}{self.oitava}({self.duracao}b)"


@dataclass
class Acorde:
    """Representa um acorde / Represents a chord."""
    raiz: str          # Nota raiz / Root note
    tipo: str          # "maior", "menor", "dim", "aug", "7", "m7"
    duracao: float = 4.0  # em tempos / in beats

    INTERVALOS_TIPO: dict[str, List[int]] = field(default_factory=dict, repr=False)

    def __post_init__(self) -> None:
        self.INTERVALOS_TIPO = {
            "maior":  [0, 4, 7],
            "menor":  [0, 3, 7],
            "dim":    [0, 3, 6],
            "aug":    [0, 4, 8],
            "7":      [0, 4, 7, 10],
            "m7":     [0, 3, 7, 10],
            "maj7":   [0, 4, 7, 11],
            "sus2":   [0, 2, 7],
            "sus4":   [0, 5, 7],
        }

    def notas(self, oitava: int = 4) -> List[Nota]:
        """Retorna as notas que compõem o acorde."""
        intervalos = self.INTERVALOS_TIPO.get(self.tipo, [0, 4, 7])
        indice_raiz = NOTAS_CROMATICAS.index(self.raiz)
        resultado: List[Nota] = []
        for intervalo in intervalos:
            idx = (indice_raiz + intervalo) % 12
            oit = oitava + (indice_raiz + intervalo) // 12
            resultado.append(Nota(NOTAS_CROMATICAS[idx], oit, self.duracao))
        return resultado

    def __str__(self) -> str:
        abreviacoes = {
            "maior": "",
            "menor": "m",
            "dim": "dim",
            "aug": "aug",
            "7": "7",
            "m7": "m7",
            "maj7": "maj7",
            "sus2": "sus2",
            "sus4": "sus4",
        }
        sufixo = abreviacoes.get(self.tipo, self.tipo)
        return f"{self.raiz}{sufixo}"


@dataclass
class Progressao:
    """Progressão harmônica / Harmonic progression."""
    nome: str
    acordes: List[Acorde]
    repeticoes: int = 1

    def __str__(self) -> str:
        return f"{self.nome}: {' | '.join(str(a) for a in self.acordes)}"


@dataclass
class Melodia:
    """Sequência melódica / Melodic sequence."""
    notas: List[Nota]
    bpm: int = 120

    def duracao_total(self) -> float:
        """Duração total em tempos."""
        return sum(n.duracao for n in self.notas)

    def __str__(self) -> str:
        return " ".join(str(n) for n in self.notas)


@dataclass
class Composicao:
    """Composição musical completa / Complete musical composition."""
    titulo: str
    estilo: str
    tonalidade: str
    escala: Escala
    compasso: Compasso
    bpm: int
    progressao: Progressao
    melodia: Optional[Melodia] = None
    letra_sugerida: Optional[str] = None
    descricao: str = ""

    def __str__(self) -> str:
        linhas = [
            f"🎵 {self.titulo}",
            f"   Estilo    : {self.estilo}",
            f"   Tonalidade: {self.tonalidade} {self.escala.value}",
            f"   Compasso  : {self.compasso.value}  |  BPM: {self.bpm}",
            f"   Harmonia  : {self.progressao}",
        ]
        if self.melodia:
            linhas.append(f"   Melodia   : {self.melodia}")
        if self.letra_sugerida:
            linhas.append(f"   Letra     :\n{self.letra_sugerida}")
        if self.descricao:
            linhas.append(f"   Dica      : {self.descricao}")
        return "\n".join(linhas)
