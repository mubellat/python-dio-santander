import os
import shutil
from pathlib import Path

ROOT_PATH = Path(__file__) # busca caminho do arquivo atual
print(ROOT_PATH.parent) # inclui dentro do diretorio do arquivo atual

# os.mkdir(ROOT_PATH / "novo-diretorio") # cria novo arquivo

arquivo = open("novo-arquivo.txt")

arquivo.close()

os.rename(ROOT_PATH / "novo.txt", ROOT_PATH / "alterado.txt") # renomeando arquivo

os.remove(ROOT_PATH / "alterado.txt") # removendo arquivo

shutil.move(ROOT_PATH / "novo.txt", ROOT_PATH / "novo-diretorio" / "novo.txt") # movendo arquivo de diretorio