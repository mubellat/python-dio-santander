file = open("example.txt", "r")
print(file.readline()) # retorna todo conteudo do arquivo em uma string, ler linha por linha
file.close()

print(file.readlines()) # ler todo o arquivo e retorna em uma lista em que cada elemento é uma linha
