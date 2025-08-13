def criar_carro(modelo, ano, placa, /, marca, motor, combustivel): # antes da barra se define parâmetro por posição obrigatoriamente, após a barra opcional tanto por chave quanto por posição
    # caso fosse "def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):" seria obrigatório após o asterisco ser declarado por chave
    print(modelo, ano, placa, marca, motor, combustivel)


criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # válido

criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # inválido

def somar(a, b):
    return a + b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação {a} + {b} = {resultado}")

exibir_resultado(10, 10, somar)

# uso de variáveis de escopo global(fora da função)
# NÃO É UMA BOA PRÁTICA

salario = 2000

def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario

salario_bonus(500)