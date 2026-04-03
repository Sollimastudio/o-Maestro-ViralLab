"""
Templates de estilos musicais virais para o Mago Compositor.
Viral music style templates for the Mago Compositor.
"""

from __future__ import annotations
from typing import Dict, List, Tuple

# Progressões populares por grau (algarismo romano)
# Popular progressions by degree (roman numeral)
PROGRESSOES_VIRAIS: Dict[str, List[Tuple[int, str]]] = {
    "pop":   [(1, "maior"), (5, "maior"), (6, "menor"), (4, "maior")],  # I-V-vi-IV
    "edm":   [(1, "menor"), (6, "maior"), (3, "maior"), (7, "maior")],  # i-VI-III-VII
    "lofi":  [(1, "maior"), (6, "menor"), (2, "menor"), (5, "7")],      # I-vi-ii-V
    "trap":  [(1, "menor"), (1, "menor"), (6, "maior"), (7, "maior")],  # i-i-VI-VII
    "funk":  [(1, "7"), (4, "7"), (1, "7"), (5, "7")],                  # I7-IV7-I7-V7
    "samba": [(1, "maior"), (5, "7"), (1, "maior"), (4, "maior")],      # I-V7-I-IV
    "bossa": [(1, "maj7"), (4, "maj7"), (3, "m7"), (6, "m7")],          # Imaj7-IVmaj7-IIIm7-VIm7
    "rock":  [(1, "maior"), (4, "maior"), (5, "maior"), (1, "maior")],  # I-IV-V-I
}

# BPM típico por estilo
BPMS: Dict[str, Tuple[int, int]] = {
    "pop":   (90, 120),
    "edm":   (125, 140),
    "lofi":  (70, 90),
    "trap":  (130, 160),
    "funk":  (90, 110),
    "samba": (100, 130),
    "bossa": (80, 110),
    "rock":  (110, 140),
}

# Padrões rítmicos de melodia (em frações de tempo; 1 = semínima, 0.5 = colcheia)
PADROES_RITMICOS: Dict[str, List[float]] = {
    "pop":   [1.0, 0.5, 0.5, 1.0, 1.0],
    "edm":   [0.5, 0.5, 0.5, 0.5, 1.0, 1.0],
    "lofi":  [1.5, 0.5, 1.0, 1.0],
    "trap":  [0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 1.0],
    "funk":  [0.5, 0.25, 0.25, 0.5, 0.5, 1.0],
    "samba": [0.5, 0.5, 1.0, 0.5, 0.5, 1.0],
    "bossa": [1.5, 0.5, 1.0, 1.0],
    "rock":  [1.0, 1.0, 0.5, 0.5, 1.0],
}

# Letras/frases de inspiração por estilo
FRASES_INSPIRACAO: Dict[str, List[str]] = {
    "pop": [
        "Você ilumina o meu mundo como ninguém",
        "Não consigo parar de pensar em você",
        "Cada momento ao seu lado é eterno",
        "Vamos voar alto, até as estrelas",
    ],
    "edm": [
        "Sinta a batida no seu coração",
        "Deixa a música te levar",
        "Neste ritmo não tem como parar",
        "Pulsa, vive, sente o som",
    ],
    "lofi": [
        "Tarde de chuva, café e melodia",
        "O tempo passa devagar quando estou aqui",
        "Notas ao vento, pensamentos livres",
        "Uma canção para os dias calmos",
    ],
    "trap": [
        "De baixo pra cima, nunca desisto",
        "Minha história, minha glória",
        "Cada obstáculo é um degrau a mais",
        "Chegamos longe, mas ainda há mais",
    ],
    "funk": [
        "Vem cá dançar, não tem como resistir",
        "O baile tá on, bora agitar",
        "Rebolô, rebolô, todo mundo junto aqui",
        "O funk é a voz da nossa gente",
    ],
    "samba": [
        "Na avenida, o povo canta e sorri",
        "Samba no pé, alegria no coração",
        "Brasil, meu Brasil, que maravilha",
        "O tamborim chama, o carnaval chegou",
    ],
    "bossa": [
        "Garota de Ipanema passa e sorri",
        "Tarde suave, mar de calmaria",
        "Viola, voz e solidão",
        "Aquarela de um sonho cor-de-rosa",
    ],
    "rock": [
        "Liberdade é o nosso grito",
        "Guitarra distorcida, alma liberada",
        "Nada vai nos parar agora",
        "Acorda, o show deve continuar",
    ],
}

# Descrições de produção por estilo
DICAS_PRODUCAO: Dict[str, str] = {
    "pop":   "Use sintetizadores brilhantes, bateria eletrônica e backing vocals em camadas para o som pop viral.",
    "edm":   "Adicione drops impactantes, sidechain compression e filtros de abertura para energia máxima na pista.",
    "lofi":  "Use amostras com vinil, bateria solta com swing e piano elétrico levemente desafinado para o clima lo-fi.",
    "trap":  "Hi-hats em triplets, 808 com portamento e reverb longo nos percussivos criam a identidade trap.",
    "funk":  "Baixo slap groovado, guitarra rítmica em colcheias e metais criam a pegada funk irresistível.",
    "samba": "Surdo, caixa, pandeiro e cuíca constroem o samba. Adicione cavaquinho e violão 7 cordas.",
    "bossa": "Violão com dedilhado syncopado, contrabaixo acústico e voz suave compõem a essência da bossa nova.",
    "rock":  "Guitarra power chords, bateria poderosa e baixo drive. Distorção moderada para o rock clássico.",
}

ESTILOS_DISPONIVEIS: List[str] = list(PROGRESSOES_VIRAIS.keys())
