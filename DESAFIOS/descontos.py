# Dicionário com os valores de desconto
print('''
    "DESCONTO10": 0.10,
    "DESCONTO20": 0.20,
    "SEM_DESCONTO": 0.00, 
''')

# Entrada do usuário
preco = float(input("Informe o preço do produto: R$ ").strip())

while preco < 0:
    preco = float(input("Valor de produto inválido. Tente novamente.\nDigite o valor do produto: R$ "))

cupom = input("Digite o código do cupom de desconto: ").strip().upper()

# aplique o desconto se o cupom for válido:
novo_preco = 0

if cupom == "DESCONTO10":
    novo_preco = preco - (preco * 0.10)
    print(f"Você ganhou desconto de 10%!\nValor final do produto: R$ {novo_preco:.2f}")
elif cupom == "DESCONTO20":
    novo_preco = preco - (preco * 0.20)
    print(f"Você ganhou desconto de 20%!\nValor final do produto: R$ {novo_preco:.2f}")
else:
    print(f"Cupom inválido!\nSem desconto no valor final do produto.\nValor final: R$ {preco:.2f}")

