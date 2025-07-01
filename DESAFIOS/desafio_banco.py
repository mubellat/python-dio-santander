saldo = 0
limite = 500
extrato = ""
lista_saques = []
lista_depositos = []
LIMITE_SAQUES = 3
contador_saque = 0

menu = '''
=== MENU ===
1 - Depósito
2 - Saque
3 - Extrato
0 - Sair
============

Escolha uma opção:
'''

opcao = int(input(menu))

while opcao != 0: # ao selecionar 0 encerra a operação
    while opcao < 0 or opcao > 3: # contorna possíveis erros de digitação ao selecionar opção no menu
        opcao = int(input(f"Opção inválida, tente novamente.\n{menu}"))
    if opcao == 1:
        deposito = float(input("Informe o valor que irá depositar: R$ "))
        while deposito <= 0:
            deposito = float(input("O valor não pode ser negativo, tente novamente digitando um valor válido: R$ "))
        saldo += deposito
        lista_depositos.append(deposito)
    elif opcao == 2:
        if saldo == 0:
            print("Saldo negativo. Não é possível realizar saques.")
        elif contador_saque < LIMITE_SAQUES:
            saque = float(input("Digite o valor a ser sacado: "))
            while saque > limite or saque <= 0:
                saque = float(input("Valor inválido ou excedeu o limite. Digite o valor do saque de R$ 500,00. Tente novamente: "))
            while saque > saldo:
                saque = float(input(f"O valor do saque excede o valor do seu saldo.\nSeu saldo: R$ {saldo} \nTente novamente: "))
            saldo -= saque
            lista_saques.append(saque)
            contador_saque += 1
        elif contador_saque >= LIMITE_SAQUES:
            print("Limite de saques diários alcançado.")
    elif opcao == 3:
        if not lista_depositos: # mensagem afirmando que não forma feito depósitos
            print("Não foram feitas movimentações de depósito.")
        else:
            print("DEPÓSITOS:")
            for i in lista_depositos: # uso de loop para listar depósitos incluídos em lista
                print(f"R$ {i:.2f}")
        if not lista_saques: # mensagem afirmando que não foi feito saques
            print("Não foram feitas movimentações de saque.")
        else:
            print("SAQUES:")
            for i in lista_saques: # uso de loop para listar saques incluídos em lista
                print(f"R$ {i:.2f}")
        print(f"Saldo total: R$ {saldo:.2f}")
    opcao = int(input(menu)) # retorna o menu a cada iteração

print("Operação encerrada.")