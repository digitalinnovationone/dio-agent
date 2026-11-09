"""Exemplo didático com consulta parametrizada.

Este exemplo demonstra somente a mitigação de SQL Injection.
Não é um sistema de autenticação pronto para produção: o armazenamento de
senhas em texto claro foi mantido apenas para isolar o tema do exercício.
"""

import sqlite3


def fazer_login(db_path, usuario, senha):
    """Consulta com parâmetros e tratamento simples de erro."""
    try:
        with sqlite3.connect(db_path) as conn:
            resultado = conn.execute(
                "SELECT 1 FROM usuarios WHERE username = ? AND password = ?",
                (usuario, senha),
            ).fetchone()
        return resultado is not None
    except sqlite3.Error:
        # Não expõe detalhes internos do banco para quem chama a função.
        return False
