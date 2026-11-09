"""Exemplo intencionalmente vulnerável para análise estática em laboratório.

NÃO use este arquivo em produção nem o exponha como serviço.
O objetivo didático é observar a construção insegura de uma consulta SQL.
"""

import sqlite3


def fazer_login(db_path, usuario, senha):
    """Demonstra o risco de interpolar entradas em uma consulta SQL."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    query = (
        f"SELECT * FROM usuarios "
        f"WHERE username = '{usuario}' AND password = '{senha}'"
    )
    cursor.execute(query)
    resultado = cursor.fetchone()
    conn.close()
    return resultado is not None
