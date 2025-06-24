nome = str(input("Informe seu nome: "))
idade = int(input("Informe sua idade: "))
cidade = str(input("Informe sua cidade: "))

print(f"Seu nome é {nome}, você tem {idade} anos e mora em {cidade} !")

print("===============================================")

# parâmetros para saídas

print(nome, idade, cidade, end="...\n") # termina a execucao do print com o parametro passado, no casotres pontos
print(nome, idade, cidade, sep="#") # passa o parametro entre as variaveis