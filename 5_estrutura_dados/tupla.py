# tuplas diferente da lista são imutáveis, ou seja, inalterável

frutas = ("laranja", "uva", "pera",) # tuplas são declaradas usando parênteses, e além disso é conveniente colocar uma vírgula no final do elemento para não haver erro por parte do interpretador python

letras = tuple("python") # declarando com a função tuple

numeros = tuple([1, 2, 3, 4]) # uma lista dentro de uma tupla para evitar que a lista seja modificada

frutas[0] # acesso de tupla é igual a lista

# mesmo conceito de matriz com listas, agora usando tuplas

matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c")
)

print(matriz[0]) 
print(matriz[0][0]) 
print(matriz[0][-1]) 
print(matriz[-1][-1])

# lógica de fatiamento também é igual

letras = ("p", "y", "t", "h", "o", "n") 
print(letras)
print(letras[2:]) 
print(letras[:2]) 
print(letras[1:3])
print(letras[::])
print(letras[::-1])

# métodos da classe tuple

letras.count("p") # lista quantos itens iguais tem na tupla

letras.index("p") # acessar o índice

len(letras) # lista quantos itens tem na tupla

