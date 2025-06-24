opcao = int(input("Informe uma opção: [1] Sacar \n[2] Extrato: "))

if opcao == 1:
    valor = float(input("Informe a quantia para o saque: "))
elif opcao == 2: # elif é equivalente a else if
    print("Exibindo o extrato...")
else:
    sys.exit("Opção Inválida!")

MAIOR_IDADE = 18 # tudo maiúsculo para definir como constante

idade = int(input("Informe a idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade pode tirar CNH!")
elif idade < 0:
    print("Idade inválida!")
else:
    print("Menor de idade não pode tirar CNH!") 