curso = "Curso de Python"
nome_curso = curso
saldo, limite = 200, 200

print(curso is nome_curso) # verificar se as duas variáveis ocupam mesmo endereço de memória (consequentemente o mesmo valor)

print(curso is not  nome_curso)

print(saldo is limite)