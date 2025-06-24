numero_um = int(input("Digite um número:"))
numero_dois = int(input("Digite outro número:"))

numero_um = float(numero_um) #conversão do tipo inteiro para float
numero_dois = float(numero_dois)

divisao = numero_um / numero_dois

print(f"A divisão dos número é igual a: {divisao}")

print("------------------------------------------------")

print(numero_um // numero_dois) # duas barras para exibir resultado inteiro da divisão

print("----------------------------------------------")

numero = 234.55
print(numero)
print(type(numero)) # usando parametro type é exibido o tipo da variavel