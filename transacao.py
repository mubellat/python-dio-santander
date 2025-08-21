import sqlite3
from pathlib import Path

ROOT_PATH = Path("/home/muliro/python-dio-santander/conexao.py").parent

conexao = sqlite3.connect(ROOT_PATH / "meu_banco.sqlite")
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row

try:
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?)", ("Teste 1", "teste1@gmail.com"))
    cursor.execute("INSERT INTO clientes (id, nome, email) VALUES (? , ?, ?)", (2, "Teste 2", "teste2@gmail.com"))
    conexao.commit()
except Exception as exc:
    print(f"Ops! Ocorreu um erro! {exc}")
    conexao.rollback