import sqlite3
import tempfile
import unittest
from pathlib import Path

from fixed_app import fazer_login


class TestLoginSeguro(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.db_path = str(Path(self.temp_dir.name) / "teste.db")
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                "CREATE TABLE usuarios (username TEXT, password TEXT)"
            )
            conn.execute(
                "INSERT INTO usuarios (username, password) VALUES (?, ?)",
                ("aluno", "senha-de-teste"),
            )

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_usuario_valido_consegue_autenticar(self):
        self.assertTrue(fazer_login(self.db_path, "aluno", "senha-de-teste"))

    def test_senha_incorreta_e_rejeitada(self):
        self.assertFalse(fazer_login(self.db_path, "aluno", "errada"))

    def test_entrada_com_caracteres_sql_nao_burla_login(self):
        usuario = "' OR '1'='1' --"
        self.assertFalse(fazer_login(self.db_path, usuario, "qualquer"))


if __name__ == "__main__":
    unittest.main()
