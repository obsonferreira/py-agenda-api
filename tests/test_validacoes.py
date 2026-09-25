import sys
import unittest
from pathlib import Path


CONTROLLERS = Path(__file__).resolve().parents[1] / "controllers"
sys.path.insert(0, str(CONTROLLERS))

from validaNome import valida_nome
from validaTelefone import valida_telefone


class TestValidaNome(unittest.TestCase):
    def test_aceita_nome_valido(self):
        resultado = valida_nome("Maria", "nome")

        self.assertFalse(resultado["erro"])
        self.assertEqual(resultado["valor"], "maria")

    def test_rejeita_nome_com_menos_de_tres_letras(self):
        resultado = valida_nome("Jo", "nome")

        self.assertTrue(resultado["erro"])

    def test_rejeita_nome_com_numero(self):
        resultado = valida_nome("Maria2", "nome")

        self.assertTrue(resultado["erro"])

    def test_rejeita_nome_vazio(self):
        resultado = valida_nome("", "nome")

        self.assertTrue(resultado["erro"])


class TestValidaTelefone(unittest.TestCase):
    def test_aceita_telefone_com_nove_digitos(self):
        resultado = valida_telefone("987654321", "telefone")

        self.assertFalse(resultado["erro"])
        self.assertEqual(resultado["valor"], "987654321")

    def test_rejeita_telefone_com_menos_de_nove_digitos(self):
        resultado = valida_telefone("123", "telefone")

        self.assertTrue(resultado["erro"])

    def test_rejeita_telefone_com_mais_de_nove_digitos(self):
        resultado = valida_telefone("1234567890", "telefone")

        self.assertTrue(resultado["erro"])

    def test_rejeita_telefone_com_letra(self):
        resultado = valida_telefone("98765A321", "telefone")

        self.assertTrue(resultado["erro"])

    def test_rejeita_telefone_vazio(self):
        resultado = valida_telefone("", "telefone")

        self.assertTrue(resultado["erro"])


if __name__ == "__main__":
    unittest.main()
