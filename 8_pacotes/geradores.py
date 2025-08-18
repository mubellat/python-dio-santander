# gerador é um tipo de gerador que economiza memória da máquina, inves de retornar valores usando return usamos o "yield"

def meu_gerador(numeros: list[int]):
    for numero in numeros:
        yield numero * 2

for i in meu_gerador(numeros = [1, 2, 3]):
    print(i)