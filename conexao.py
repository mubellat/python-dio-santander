import sqlite3
from pathlib import Path

ROOT_PATH = Path("/home/muliro/python-dio-santander/conexao.py").parent

conexao = sqlite3.connect(ROOT_PATH / "meu_banco.sqlite")
cursor = conexao.cursor()

# cursor.execute("CREATE TABLE clientes(id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))")

def criar_tabeca(conexao, cursor):
    cursor.execute(
        "CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, none VARCHAR(100), email VARCHAR(150))"
    )
    conexao.commmit()

def inserir_registro(conexao, cursor, nome, email):
    data = (nome, email)
    cursor.execute(f"INSERT INTO clientes (nome, email) VALUES (?, ?);", data)
    conexao.commit()

def atualizar_registro(conexao, cursor, nome, email, id):
    data = (nome, email, id)
    cursor.execute("UPDATE clientes SET nome=?, email=? WHERE id=?", data)
    conexao.commit()

atualizar_registro(conexao, cursor, "Muliroliro", "murilo@gmail.com", 1)

def excluir_registro(conexao, cursor, id):
    data = (id,)
    cursor.execute("DELETE FROM clientes WHERE id=?", data)
    conexao.commit()

excluir_registro(conexao, cursor, 1)

def inserir_muitos(conexao, cursos, dados):
    cursor.executemany("INSERT INTO clientes (nome, email) VALUES (?, ?)", dados)
    conexao.commit()

dados = [
    ("Guilherme", "guilherme@gmail.com"),
    ("Chappie", "chappie@gmail.com"),
    ("Melanie", "melanie@gmail.com")
]
inserir_muitos(conexao, cursor, dados)