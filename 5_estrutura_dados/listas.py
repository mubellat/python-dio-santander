frutas = ["larnja", "maca", "uva"]
print(frutas)
print(frutas[-1]) # negativo puxa item de trás para frente
print(frutas[1]) # adicionar índice do objeto para puxar item específico

frutas_2 = []
print(frutas_2)

letras = list("python") # list() torna cada letra da palavra um elemento, usando valor iterável como strings
print(letras)
print(letras[2:]) # listagem começa depois dos 2 primeiros índices
print(letras[:2]) # exibe apenas os 2 primeiros índices, parâmetro define até onde vai a listagem
print(letras[1:3]) # começa no índice 1 e termina no 3
print(letras[::]) # imprime toda a lista
print(letras[::-1]) # imprime a lista ao contrário 

for i in letras: # loop é uma melhor forma para exibir os itens da lista
    print(i)

numeros = list(range(10)) # como um número não é iterável usamos range para decompor o número e torná-lo iterável
print(numeros)

carro = ["Ferrari" , "F8", 4200000, 2020, 2900, "São Paulo", True] # diversos tipos de variáveis diferentes
print(carro)

matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

print(matriz[0]) # irá imprimir primeira linha da matriz (ou primeira lista)
print(matriz[0][0]) # como batalha naval irá puxar indíce linha 0 da coluna indíce 0
print(matriz[0][-1]) # primeira linha e última coluna
print(matriz[-1][-1]) # última linha e última coluna


nomes = ['Ana', 'Bruno', 'Carlos'] 

for i, nome in enumerate(nomes): # enumerate é muito útil para identificarmos qual o índice de cada item da lista
    print(f"{i} - {nome}") # i = índice - nome = variável que está nesse índice


# gerando nova lista de uma lista já existente

numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    
quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2) # adiciono o item e modifico também

# forma one line de fazer

quadrado_2 = [numero **2 for numero in numeros]

print("\nMelhor forma de fazer isso: \n")

pares_2 = [numero for numero in numeros if numero % 2 == 0] # primeiro parâmetro é o item a ser retornado
