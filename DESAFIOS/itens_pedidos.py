class Pedido:
    def __init__(self):
        self.itens = []

    # Método para adicionar o preço do item à lista
    def adicionar_item(self, preco):
        self.itens.append(preco)

    # Método para calcular o total dos itens
    def calcular_total(self):
        return sum(self.itens)

 
quantidade_pedidos = int(input().strip())
pedido = Pedido()

for _ in range(quantidade_pedidos):
    entrada = input().strip()
    nome, preco = entrada.rsplit(" ", 1)  # Separa nome do preço
    pedido.adicionar_item(float(preco))  # Adiciona preço convertido para float

# Imprime o total com 2 casas decimais
print(f"{pedido.calcular_total():.2f}")
