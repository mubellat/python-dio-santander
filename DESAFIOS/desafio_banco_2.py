saldo = 0
limite = 500
lista_saques = []
lista_depositos = []
LIMITE_SAQUES = 3
contador_saque = 0
usuarios = []
contas = []

def menu():
    menu = '''
    === MENU ===
    1 - Depósito
    2 - Saque
    3 - Extrato
    4 - Nova conta
    5 - Listar contas
    6 - Novo usuário
    0 - Sair
    ============

    Escolha uma opção:
    '''
    return int(input(menu))

def deposito():
    global saldo
    valor = float(input("Informe o valor que irá depositar: R$ "))
    while valor <= 0:
        valor = float(input("O valor não pode ser negativo, tente novamente: R$ "))
    saldo += valor
    lista_depositos.append(valor)
    print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")

def saque():
    global saldo, contador_saque
    if saldo == 0:
        print("Saldo zerado. Não é possível realizar saques.")
        return
    if contador_saque >= LIMITE_SAQUES:
        print("Limite de saques diários alcançado.")
        return

    valor = float(input("Digite o valor a ser sacado: R$ "))
    while valor > limite or valor <= 0:
        valor = float(input(f"Valor inválido. O limite é R$ {limite:.2f}. Tente novamente: R$ "))
    while valor > saldo:
        valor = float(input(f"O valor do saque excede o saldo.\nSaldo atual: R$ {saldo:.2f}\nTente novamente: R$ "))

    saldo -= valor
    lista_saques.append(valor)
    contador_saque += 1
    print(f"Saque de R$ {valor:.2f} realizado com sucesso.")

def extrato():
    print("\n=== EXTRATO ===")
    if not lista_depositos:
        print("Nenhum depósito realizado.")
    else:
        print("DEPÓSITOS:")
        for valor in lista_depositos:
            print(f"R$ {valor:.2f}")

    if not lista_saques:
        print("Nenhum saque realizado.")
    else:
        print("SAQUES:")
        for valor in lista_saques:
            print(f"R$ {valor:.2f}")

    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("================\n")

def cadastrar_usuario():
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf)
    if usuario:
        print("Já existe usuário com esse CPF.")
        return

    nome = input("Nome completo: ")
    data_nascimento = input("Data de nascimento (dd-mm-aaaa): ")
    endereco = input("Endereço (logradouro, nº - bairro - cidade/UF): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("Usuário cadastrado com sucesso.")

def filtrar_usuario(cpf):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta():
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf)
    if usuario:
        numero_conta = len(contas) + 1
        contas.append({"agencia": "0001", "numero_conta": numero_conta, "usuario": usuario})
        print(f"Conta criada com sucesso! Agência: 0001 Conta: {numero_conta}")
    else:
        print("Usuário não encontrado. Crie o usuário antes.")

def listar_contas():
    for conta in contas:
        linha = f"Agência: {conta['agencia']} | Conta: {conta['numero_conta']} | Titular: {conta['usuario']['nome']}"
        print(linha)

# Loop principal
while True:
    opcao = menu()

    if opcao == 1:
        deposito()
    elif opcao == 2:
        saque()
    elif opcao == 3:
        extrato()
    elif opcao == 4:
        criar_conta()
    elif opcao == 5:
        listar_contas()
    elif opcao == 6:
        cadastrar_usuario()
    elif opcao == 0:
        print("Operação encerrada.")
        break
    else:
        print("Opção inválida, tente novamente.")
