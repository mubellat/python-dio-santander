from pathlib import Path

try:
    file = open("non_existent_file.txt", "r")
except FileNotFoundError as exc:
    print("Arquivo não encontrado.")
    print(exc)

ROOT_PATH = Path(__file__).parent

try:
    arquivo = open(ROOT_PATH / "novo-diretorio")
except IsADirectoryError as exc:
    print(f"Não foi possível abrir o arquivo: {exc}")
except IOError as exc:
    print(f"Erro ao abrir o arquivo {exc}")
except Exception as exc:
    print(f"Algum problema ocorreu ao tentar abrir o arquivo: {exc}")