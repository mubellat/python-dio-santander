def meu_decorador(funcao):
    def envelope():
        print("Faz algo antes de exercutar a funcao.")
        funcao()
        print("Faz algo depois de executar a funcao.")

    return envelope

@meu_decorador
def ola_mundo():
    print("Olá mundo!")

# ola_mundo = meu_decorador(ola_mundo)
ola_mundo()