lista = []

lista.append(1) # incluindo item na lista

lista.clear() # exclui todos os itens da lista

lista.copy() # faz cópia de uma lista

cores = ["vermelho", "azul", "verde", "azul"]

cores.count("azul") # exibe quantas vezes determinado item aparece na lista

linguagens = ["python", "js", "c"]

linguagens.extend(["java", "csharp"]) # inclui mais de um item na lista, no caso incluiu outra lista na lista "linguagens"

print(linguagens.index("c")) # mostra o índice do item 

linguagens.pop() # lista funciona com estrutura pilha, pop() retira último elemento da pilha
linguagens.pop() # também pode indicar qual índice do item que deseja remover 

linguagens.remove("c") # remove item da lista informando o item e não o índice

linguagens.reverse() # inverte a lista, faz o espelhamento

# formas de ordenar lista usando sort()

linguagens.sort() # ordena em ordem alfabética
linguagens.sort(reverse=True) # em ordem alfabética espelhada
linguagens.sort(key=lambda x: len(x)) # ordena por tamanho
linguagens.sort(key=lambda x: len(x), reverse= True) # ordena em ordem decrescente

len(linguagens) # exibe tamanho da lista

sorted(linguagens, key=lambda x: len(x)) # função para ordenar igual o sort()


