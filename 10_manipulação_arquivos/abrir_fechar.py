# manipulação de arquivos

file = open("example.txt", "r") # abrir o arquivo para leitura
file = open("example.txt", "w") # abrir o arquivo para gravação
file = open("example.txt", "a") # abrir o arquivo para anexar

file.close() # essencial sempre fechar o arquivo após abrir 

try:
    with open("arquivo.txt", "w", encoding="utf-8") as arquivo: # garante o fechamento do arquivo mesmo com ocorrência de algum erro
        print(arquivo.read())
except IOError:
    print("Arquivo não encontrado.")  