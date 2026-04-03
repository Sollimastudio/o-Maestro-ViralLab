# o-Maestro-ViralLab 🎩

**Mago Compositor** — seu assistente mágico de composição musical viral.

Crie progressões harmônicas, melodias e sugestões de letra para músicas virais em estilos como Pop, EDM, Lo-fi, Trap, Funk, Samba, Bossa Nova e Rock — tudo guiado por um wizard interativo.

---

## 🚀 Início rápido

```bash
# 1. Clone o repositório
git clone https://github.com/Sollimastudio/o-Maestro-ViralLab.git
cd o-Maestro-ViralLab

# 2. (Opcional) Crie um ambiente virtual
python -m venv .venv && source .venv/bin/activate

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Execute o wizard interativo
python main.py

# 5. Ou experimente uma composição de demonstração
python main.py --demo

# 6. Liste estilos e opções disponíveis
python main.py --listar
```

---

## 🎵 Funcionalidades

| Recurso | Descrição |
|---|---|
| **Wizard interativo** | 5 passos guiados para criar sua composição |
| **8 estilos virais** | Pop, EDM, Lo-fi, Trap, Funk, Samba, Bossa, Rock |
| **Progressões harmônicas** | Acordes gerados automaticamente para a tonalidade escolhida |
| **Geração de melodia** | Padrões rítmicos e notas da escala selecionada |
| **Sugestão de letra** | Frases de inspiração para cada estilo |
| **Dicas de produção** | Orientações de mixagem e instrumentação por estilo |

---

## 🐍 Uso como biblioteca

```python
from mago_compositor import MagoCompositor
from mago_compositor.models import Escala, Compasso

mago = MagoCompositor()

composicao = mago.compor(
    titulo="Minha Música Viral",
    estilo="pop",          # pop, edm, lofi, trap, funk, samba, bossa, rock
    tonalidade="C",        # C, C#, D, D#, E, F, F#, G, G#, A, A#, B
    escala=Escala.MAIOR,
    compasso=Compasso.QUATRO_QUARTOS,
    bpm=110,
    incluir_melodia=True,
    incluir_letra=True,
)

print(composicao)
```

Saída de exemplo:

```
🎵 Minha Música Viral
   Estilo    : Pop
   Tonalidade: C maior
   Compasso  : 4/4  |  BPM: 110
   Harmonia  : I - V - VI - IV: C | G | Am | F
   Melodia   : E4(1.0b) G4(0.5b) A4(0.5b) ...
   Letra     : Você ilumina o meu mundo como ninguém
   Dica      : Use sintetizadores brilhantes, bateria eletrônica...
```

---

## 🧪 Testes

```bash
pip install pytest
pytest tests/ -v
```

---

## 📁 Estrutura do projeto

```
o-Maestro-ViralLab/
├── mago_compositor/
│   ├── __init__.py       # Exportações públicas
│   ├── models.py         # Modelos de dados musicais (Nota, Acorde, Composição…)
│   ├── templates.py      # Templates de estilos virais
│   ├── compositor.py     # Lógica central — MagoCompositor
│   └── wizard.py         # Wizard interativo — WizardMago
├── tests/
│   └── test_mago_compositor.py
├── main.py               # Ponto de entrada CLI
├── requirements.txt
└── README.md
```

---

## 🌟 Estilos disponíveis

| Estilo | Progressão base | BPM típico |
|--------|----------------|------------|
| Pop | I – V – vi – IV | 90–120 |
| EDM | i – VI – III – VII | 125–140 |
| Lo-fi | I – vi – ii – V | 70–90 |
| Trap | i – i – VI – VII | 130–160 |
| Funk | I7 – IV7 – I7 – V7 | 90–110 |
| Samba | I – V7 – I – IV | 100–130 |
| Bossa | Imaj7 – IVmaj7 – IIIm7 – VIm7 | 80–110 |
| Rock | I – IV – V – I | 110–140 |

---

*Feito com ✨ pelo o-Maestro ViralLab*