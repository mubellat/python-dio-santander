texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS: # parãmetro upper converte a letra para maiúscula
        print(letra, end="") # parâmetro end faz com que impressa tudo na mesma linha
else:
    print() # quebra de linha
    print("Executa no final do laço!")