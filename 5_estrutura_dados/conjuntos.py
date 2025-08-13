# set é uma coleção que possui apenas elementos únicos, sem elementos duplicados como listas e tuplas

lista = set([1, 2, 3, 4 ,2, 3, 4 ,5 , 6])
print(lista) # ignora itens duplicados

# não podemos usar índice em conjuntos, para isso precisamos fazer a conversão de conjunto para lista

nova_lista = list(lista) # conversão para lista

print(nova_lista[1]) # agora podemos usar índice

# com função enumerate podemos percorrer a lista para verificar o índice

for indice, numero in enumerate(lista):
    print(f"{indice}: {lista}")

conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}

conjunto_a.union(conjunto_b) # faz a união de dois cojuntos 

conjunto_a.intersection(conjunto_b) # retorna oque os dois conjuntos tem de igual 

print(conjunto_a.difference(conjunto_b)) # retorna oque tem de diferente de um conjunto para outro

conjunto_a.symmetric_difference(conjunto_b) # retorna todos os itens diferentes de ambos os conjuntos

print(conjunto_a.issubset(conjunto_b)) # verdadeiro pois tudo que tem no A tem no B
print(conjunto_b.issubset(conjunto_a)) # falso pois B tem 4 e 5 que não tem no A

print(conjunto_a.issuperset(conjunto_b)) # falso: B não é superset de B
print(conjunto_b.issuperset(conjunto_a)) # verdadeiro: tudo que tem em A tem em B

conjunto_a.isdisjoint(conjunto_b) # falso: define como verdadeiro se os conjuntos não tiverem itens em comum

conjunto_a.add(23) # adiciona item ao conjunto caso ele ainda não exista dentro dela

conjunto_a.clear() # limpa todo o conjunto

conjunto_a.copy() # gera uma cópi assim como listas

conjunto_b.discard(1) # descarta valor da lista (não o índice, o item)

conjunto_a.pop() # elimina valor da lista em pilha, ou passando o índice

conjunto_a.remove() # também elimina algum índice

len(conjunto_b) # ler tamanho do conjunto

3 in conjunto_b # verdadeiro: método para verificar se há algum item na lista