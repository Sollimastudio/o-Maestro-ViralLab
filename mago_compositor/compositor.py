"""
Lógica central do Mago Compositor — constrói composições musicais.
Core logic of the Mago Compositor — builds musical compositions.
"""

from __future__ import annotations
import random as _random_module
from typing import List, Optional, Tuple

from .models import (
    Acorde,
    Compasso,
    Composicao,
    Escala,
    Melodia,
    Nota,
    Progressao,
    INTERVALOS_ESCALA,
    NOTAS_CROMATICAS,
)
from .templates import (
    BPMS,
    DICAS_PRODUCAO,
    ESTILOS_DISPONIVEIS,
    FRASES_INSPIRACAO,
    PADROES_RITMICOS,
    PROGRESSOES_VIRAIS,
)


def _indice_nota(nome: str) -> int:
    return NOTAS_CROMATICAS.index(nome)


def _nota_por_grau(tonalidade: str, escala: Escala, grau: int) -> str:
    """Retorna a nota de um grau da escala (1-indexed)."""
    intervalos = INTERVALOS_ESCALA[escala]
    idx_raiz = _indice_nota(tonalidade)
    semitom = intervalos[(grau - 1) % len(intervalos)]
    return NOTAS_CROMATICAS[(idx_raiz + semitom) % 12]


def _construir_progressao(
    nome_estilo: str,
    tonalidade: str,
    escala: Escala,
    repeticoes: int = 2,
) -> Progressao:
    """Constrói uma Progressao a partir de template e tonalidade."""
    template = PROGRESSOES_VIRAIS[nome_estilo]
    acordes: List[Acorde] = []
    for grau, tipo_acorde in template:
        raiz = _nota_por_grau(tonalidade, escala, grau)
        acordes.append(Acorde(raiz=raiz, tipo=tipo_acorde))
    nome_progressao = " - ".join(
        f"{_alg_romano(g)}{'m' if 'menor' in t else ''}" for g, t in template
    )
    return Progressao(nome=nome_progressao, acordes=acordes, repeticoes=repeticoes)


def _alg_romano(grau: int) -> str:
    mapa = {1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII"}
    return mapa.get(grau, str(grau))


def _gerar_melodia(
    tonalidade: str,
    escala: Escala,
    estilo: str,
    bpm: int,
    rng: _random_module.Random,
    num_notas: int = 16,
) -> Melodia:
    """Gera uma melodia simples baseada na escala e padrão rítmico do estilo."""
    intervalos = INTERVALOS_ESCALA[escala]
    idx_raiz = _indice_nota(tonalidade)
    notas_escala = [NOTAS_CROMATICAS[(idx_raiz + i) % 12] for i in intervalos]

    padrao_ritmo = PADROES_RITMICOS.get(estilo, [1.0, 0.5, 0.5, 1.0])
    notas: List[Nota] = []
    oitavas = [4, 4, 4, 5]  # preferência para oitavas centrais

    i = 0
    while len(notas) < num_notas:
        nome = rng.choice(notas_escala)
        oitava = rng.choice(oitavas)
        duracao = padrao_ritmo[i % len(padrao_ritmo)]
        notas.append(Nota(nome=nome, oitava=oitava, duracao=duracao))
        i += 1

    return Melodia(notas=notas, bpm=bpm)


def _escolher_frase(estilo: str, rng: _random_module.Random) -> str:
    frases = FRASES_INSPIRACAO.get(estilo, ["Uma música incrível está nascendo..."])
    return rng.choice(frases)


class MagoCompositor:
    """
    O Mago Compositor — cria composições musicais virais sob medida.
    The Mago Compositor — creates tailored viral musical compositions.
    """

    ESTILOS = ESTILOS_DISPONIVEIS
    TONALIDADES = NOTAS_CROMATICAS
    ESCALAS = list(Escala)
    COMPASSOS = list(Compasso)

    def __init__(self, semente: Optional[int] = None) -> None:
        self._rng = _random_module.Random(semente)

    # ------------------------------------------------------------------
    # API pública / Public API
    # ------------------------------------------------------------------

    def compor(
        self,
        titulo: str,
        estilo: str,
        tonalidade: str,
        escala: Escala = Escala.MAIOR,
        compasso: Compasso = Compasso.QUATRO_QUARTOS,
        bpm: Optional[int] = None,
        incluir_melodia: bool = True,
        incluir_letra: bool = True,
        repeticoes: int = 2,
    ) -> Composicao:
        """
        Cria uma composição completa com os parâmetros fornecidos.
        Creates a complete composition with the provided parameters.

        Args:
            titulo: Título da composição.
            estilo: Estilo musical (ver MagoCompositor.ESTILOS).
            tonalidade: Nota raiz (ex.: "C", "G#").
            escala: Tipo de escala (Escala enum).
            compasso: Fórmula de compasso (Compasso enum).
            bpm: Batidas por minuto; se None, usa faixa padrão do estilo.
            incluir_melodia: Se True, gera uma melodia sugerida.
            incluir_letra: Se True, sugere um verso de letra.
            repeticoes: Número de repetições da progressão.

        Returns:
            Composicao com todos os elementos gerados.
        """
        estilo = estilo.lower()
        if estilo not in PROGRESSOES_VIRAIS:
            raise ValueError(
                f"Estilo '{estilo}' não disponível. "
                f"Escolha entre: {', '.join(ESTILOS_DISPONIVEIS)}"
            )

        tonalidade = tonalidade.upper().replace("B", "A#").replace("Bb", "A#")
        if tonalidade not in NOTAS_CROMATICAS:
            raise ValueError(
                f"Tonalidade '{tonalidade}' inválida. "
                f"Use: {', '.join(NOTAS_CROMATICAS)}"
            )

        if bpm is None:
            bpm_min, bpm_max = BPMS[estilo]
            bpm = self._rng.randint(bpm_min, bpm_max)

        progressao = _construir_progressao(estilo, tonalidade, escala, repeticoes)

        melodia = None
        if incluir_melodia:
            melodia = _gerar_melodia(tonalidade, escala, estilo, bpm, self._rng)

        letra = None
        if incluir_letra:
            letra = _escolher_frase(estilo, self._rng)

        return Composicao(
            titulo=titulo,
            estilo=estilo.capitalize(),
            tonalidade=tonalidade,
            escala=escala,
            compasso=compasso,
            bpm=bpm,
            progressao=progressao,
            melodia=melodia,
            letra_sugerida=letra,
            descricao=DICAS_PRODUCAO.get(estilo, ""),
        )

    def sugerir_bpm(self, estilo: str) -> Tuple[int, int]:
        """Retorna a faixa de BPM recomendada para o estilo."""
        estilo = estilo.lower()
        return BPMS.get(estilo, (80, 140))

    def listar_estilos(self) -> List[str]:
        """Lista todos os estilos disponíveis."""
        return list(ESTILOS_DISPONIVEIS)

    def listar_tonalidades(self) -> List[str]:
        """Lista todas as tonalidades disponíveis."""
        return list(NOTAS_CROMATICAS)

    def listar_escalas(self) -> List[Escala]:
        """Lista todas as escalas disponíveis."""
        return list(Escala)
