# Lista que vai armazenar tuplas com os nomes e preços dos produtos
carrinho = []

# Variável para armazenar o valor total da compra
total = 0.0

# Entrada da quantidade de itens que o usuário vai digitar
n = int(input("Informe quantos itens tem sua compra: ").strip())  # .strip() remove espaços em branco

for _ in range(n):
    linha = input("Informe o nome e preço do produto: ").strip()  # Lê a linha contendo nome e preço do produto
    
    # Encontra a posição do último espaço da linha (entre nome e preço)
    posicao_espaco = linha.rfind(" ")
    
    # Separa o nome do produto (tudo antes do último espaço)
    nome_produto = linha[:posicao_espaco]
    
    # Separa o preço do produto (tudo após o último espaço) e converte para float
    preco_produto = float(linha[posicao_espaco + 1:])
    
    # Adiciona o produto e seu preço à lista do carrinho como uma tupla (nome, preço)
    carrinho.append((nome_produto, preco_produto))
    
    # Soma o preço ao total da compra
    total += preco_produto

# Imprime todos os produtos com seus respectivos preços
for nome, preco in carrinho:
    print(f"{nome}: R${preco:.2f}")  # Mostra o preço com duas casas decimais

# Imprime o valor total da compra formatado corretamente
print("\n---------------------")
print(f"Total: R${total:.2f}")
