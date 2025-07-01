# Entrada do usuário
email = str(input("Digite seu email: "))
email_valido = True

# verifique as regras do e-mail:
if len(email) == 0:
    print("Campo vazio.")
    email_valido = False
elif not("@" in email):
    print("Não contém domínio.")
    email_valido = False
elif email[0] == "@" or email[-1] == "@":
    print("Não deve conter @ no final e nem no início do email.")
    email_valido = False
elif email[-4:] != ".com" and email[-7:] == ".com.br": # compara 4 últimos caracteres ou os 7 últimos também
    print("Formatação de domínio incorreta.")
    email_valido = False
elif " " in email:
    print("Não deve conter espaços.")
    email_valido = False

if email_valido:
    print("EMAIL VÁLIDO!")
else:
    print("EMAIL INVÁLIDO!")



