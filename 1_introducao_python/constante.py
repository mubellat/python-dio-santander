nome, idade = ("Murilo", 21)

print(f"Olá, meu nome é {nome} e eu tenho {idade} anos de idade!")
print("Olá, meu nome é",nome,"e eu tenho",idade,"anos de idade!")

# constante é uma variável que tem um valor fixo até o final do programa
# não tem como declarar constante em python mas por convenção variáveis declaradas toda em maiusculos sao definidas como CONSTANTES

#exemplos

print("Diretório do programa:")
CAMINHO = r"C:\Users\MULIRO\Documents\python_dio\1_introdução_linguagem" # o R declara uma string bruta para usar \ nos blocos ( como por exemplo \n serve para pular linhas)
print(f"O caminho do programa: {CAMINHO}")  # f no inicio do texto para expecificar variável dentro do texto

print("---------------------------------------------------------------")

ESTADOS = ["SP","GO","PA"]

print(f"Eu sou do estado de {ESTADOS[1]}")

print(ESTADOS)