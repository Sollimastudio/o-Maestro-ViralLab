"""
Testes do Mago Compositor.
Tests for the Mago Compositor.
"""

import pytest

from mago_compositor import MagoCompositor, Composicao
from mago_compositor.models import (
    Acorde,
    Compasso,
    Escala,
    Melodia,
    Nota,
    NOTAS_CROMATICAS,
)
from mago_compositor.templates import ESTILOS_DISPONIVEIS, PROGRESSOES_VIRAIS


# ──────────────────────────────────────────────
# Testes de modelos / Model tests
# ──────────────────────────────────────────────

class TestNota:
    def test_midi_do_central(self):
        nota = Nota("C", oitava=4)
        assert nota.midi == 60

    def test_midi_la_440(self):
        nota = Nota("A", oitava=4)
        assert nota.midi == 69

    def test_str_format(self):
        nota = Nota("D#", oitava=3, duracao=0.5)
        assert "D#" in str(nota)
        assert "3" in str(nota)


class TestAcorde:
    def test_acorde_maior_c(self):
        acorde = Acorde("C", "maior")
        notas = acorde.notas(oitava=4)
        nomes = [n.nome for n in notas]
        assert "C" in nomes
        assert "E" in nomes
        assert "G" in nomes

    def test_acorde_menor(self):
        acorde = Acorde("A", "menor")
        notas = acorde.notas(oitava=4)
        nomes = [n.nome for n in notas]
        assert "A" in nomes
        assert "C" in nomes
        assert "E" in nomes

    def test_str_maior_sem_sufixo(self):
        acorde = Acorde("G", "maior")
        assert str(acorde) == "G"

    def test_str_menor_com_sufixo(self):
        acorde = Acorde("E", "menor")
        assert str(acorde) == "Em"


# ──────────────────────────────────────────────
# Testes do compositor / Compositor tests
# ──────────────────────────────────────────────

class TestMagoCompositor:
    def setup_method(self):
        self.mago = MagoCompositor(semente=42)

    def test_listar_estilos_nao_vazio(self):
        estilos = self.mago.listar_estilos()
        assert len(estilos) > 0

    def test_listar_tonalidades(self):
        tons = self.mago.listar_tonalidades()
        assert "C" in tons
        assert "G" in tons
        assert len(tons) == 12

    def test_listar_escalas(self):
        escalas = self.mago.listar_escalas()
        assert Escala.MAIOR in escalas
        assert Escala.MENOR in escalas

    def test_compor_basico(self):
        comp = self.mago.compor(
            titulo="Teste",
            estilo="pop",
            tonalidade="C",
        )
        assert isinstance(comp, Composicao)
        assert comp.titulo == "Teste"
        assert comp.estilo.lower() == "pop"
        assert comp.tonalidade == "C"

    def test_compor_todos_os_estilos(self):
        for estilo in ESTILOS_DISPONIVEIS:
            comp = self.mago.compor(
                titulo=f"Teste {estilo}",
                estilo=estilo,
                tonalidade="G",
            )
            assert comp.estilo.lower() == estilo

    def test_compor_com_melodia(self):
        comp = self.mago.compor(
            titulo="Com Melodia",
            estilo="lofi",
            tonalidade="D",
            incluir_melodia=True,
        )
        assert comp.melodia is not None
        assert isinstance(comp.melodia, Melodia)
        assert len(comp.melodia.notas) > 0

    def test_compor_sem_melodia(self):
        comp = self.mago.compor(
            titulo="Sem Melodia",
            estilo="rock",
            tonalidade="E",
            incluir_melodia=False,
        )
        assert comp.melodia is None

    def test_compor_com_letra(self):
        comp = self.mago.compor(
            titulo="Com Letra",
            estilo="samba",
            tonalidade="F",
            incluir_letra=True,
        )
        assert comp.letra_sugerida is not None
        assert len(comp.letra_sugerida) > 0

    def test_compor_sem_letra(self):
        comp = self.mago.compor(
            titulo="Sem Letra",
            estilo="funk",
            tonalidade="A",
            incluir_letra=False,
        )
        assert comp.letra_sugerida is None

    def test_bpm_customizado(self):
        comp = self.mago.compor(
            titulo="BPM Fixo",
            estilo="edm",
            tonalidade="C",
            bpm=128,
        )
        assert comp.bpm == 128

    def test_estilo_invalido_levanta_erro(self):
        with pytest.raises(ValueError, match="não disponível"):
            self.mago.compor(
                titulo="Erro",
                estilo="jazz-fusion-progressivo-inexistente",
                tonalidade="C",
            )

    def test_tonalidade_invalida_levanta_erro(self):
        with pytest.raises(ValueError, match="inválida"):
            self.mago.compor(
                titulo="Erro",
                estilo="pop",
                tonalidade="X",
            )

    def test_progressao_nao_vazia(self):
        comp = self.mago.compor(
            titulo="Progressão",
            estilo="bossa",
            tonalidade="C",
        )
        assert len(comp.progressao.acordes) > 0

    def test_str_composicao_contem_titulo(self):
        comp = self.mago.compor(
            titulo="Minha Música",
            estilo="pop",
            tonalidade="C",
        )
        texto = str(comp)
        assert "Minha Música" in texto

    def test_sugerir_bpm_retorna_faixa(self):
        bpm_min, bpm_max = self.mago.sugerir_bpm("edm")
        assert bpm_min < bpm_max
        assert bpm_min > 0

    def test_semente_deterministica(self):
        mago1 = MagoCompositor(semente=99)
        mago2 = MagoCompositor(semente=99)
        comp1 = mago1.compor("T", "pop", "C")
        comp2 = mago2.compor("T", "pop", "C")
        assert comp1.bpm == comp2.bpm
        assert str(comp1.progressao) == str(comp2.progressao)

    def test_compasso_personalizado(self):
        comp = self.mago.compor(
            titulo="Valsa",
            estilo="pop",
            tonalidade="G",
            compasso=Compasso.TRES_QUARTOS,
        )
        assert comp.compasso == Compasso.TRES_QUARTOS

    def test_escala_menor(self):
        comp = self.mago.compor(
            titulo="Menor",
            estilo="rock",
            tonalidade="A",
            escala=Escala.MENOR,
        )
        assert comp.escala == Escala.MENOR

    def test_repeticoes_progressao(self):
        comp = self.mago.compor(
            titulo="Repetição",
            estilo="pop",
            tonalidade="C",
            repeticoes=4,
        )
        assert comp.progressao.repeticoes == 4
