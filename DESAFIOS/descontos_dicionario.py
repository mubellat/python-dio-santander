# Dicionário com os valores de desconto
descontos = {
    "DESCONTO10": 0.10,
    "DESCONTO20": 0.20,
    "SEM_DESCONTO": 0.00, 
}

# Entrada do usuário
preco = float(input("Informe o valor do produto: ").strip())

while preco < 0:
    preco = float(input("Não pode ser valor negativo.\nTente novamente, digite o valor do produto: "))

cupom = input("Digite o cupom de desconto: ").strip().upper()

# aplique o desconto se o cupom for válido:
if cupom in descontos:
    desconto = descontos[cupom]
    novo_preco = preco - (preco * desconto)
    print(f"Preço com desconto: R$ {novo_preco:.2f}")
else:
    print(f"CUPOM INVÁLIDO!\nPreço final: {preco:.2f}")