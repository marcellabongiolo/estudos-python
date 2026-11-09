import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

from fundamentals.hello_cs50 import main, saudar


class TestSaudacao(unittest.TestCase):
    def test_nome_simples(self):
        self.assertEqual(saudar("Marcella"), "Olá, Marcella!")

    def test_normaliza_espacos(self):
        self.assertEqual(saudar("  Ana   Maria  "), "Olá, Ana Maria!")

    def test_preserva_acentos(self):
        self.assertEqual(saudar("João"), "Olá, João!")

    def test_rejeita_nome_vazio(self):
        with self.assertRaises(ValueError):
            saudar("   ")

    def test_rejeita_tipo_invalido(self):
        with self.assertRaises(TypeError):
            saudar(None)

    def test_cli_exibe_erro_para_nome_vazio(self):
        saida = io.StringIO()
        with patch("builtins.input", return_value="  "), redirect_stdout(saida):
            main()
        self.assertEqual(saida.getvalue().strip(), "Informe um nome.")


if __name__ == "__main__":
    unittest.main()
