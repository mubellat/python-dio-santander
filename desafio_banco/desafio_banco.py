saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    menu = '''
        === MENU ===
        1 - Depósito
        2 - Saque
        3 - Extrato
        0 - Sair
        ============

        Escolha uma opção:
        '''

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Erro: Não é permitido depositar um valor negativo ou zero.")

    elif opcao == "2":
        if numero_saques >= LIMITE_SAQUES:
            print("Erro: Número máximo de saques diários atingido.")
            continue

        valor = float(input("Informe o valor do saque: "))

        if valor <= 0:
            print("Erro: Valor de saque deve ser positivo.")
        elif valor > saldo:
            print("Erro: Saldo insuficiente para saque.")
        elif valor > limite:
            print(f"Erro: O limite máximo por saque é R$ {limite:.2f}.")
        else:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")

    elif opcao == "3":
        print("\n=== EXTRATO ===")
        print(extrato if extrato else "Nenhuma movimentação realizada.")
        print(f"Saldo atual: R$ {saldo:.2f}")
        print(f"Número de saques realizados hoje: {numero_saques}/{LIMITE_SAQUES}")

    elif opcao == "0":
        print("Saindo... Obrigado por usar o sistema bancário!")
        break

    else:
        print("Opção inválida! Tente novamente.")
