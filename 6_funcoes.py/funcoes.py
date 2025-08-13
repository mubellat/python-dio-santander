def exibir_mensagem():
    print("OLá Mundo!")

def exibir_mensagem_2(nome): # essa função tem o argumento nome, caso não seja declarado ao chamar a função qual será o nome irá retornar um erro
    print(f"Seja bem vindo {nome}!")

def exibir_mensagem_3(nome="Anônimo"):
    print(f"Seja bem vindo {nome}!")

# formas de chamar a função

exibir_mensagem()
exibir_mensagem_2(nome="Murilo")
exibir_mensagem_3()
exibir_mensagem_3(nome="Chappie")

def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor

calcular_total([10, 20, 34])
retorna_antecessor_e_sucessor(10)

def salvar_carro(marca, modelo, ano, placa):
    # salva carro no banco de dados...
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

salvar_carro("Fiat", "Palio", 1999, "ABC-1234")
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234") # argumento nomeado é mais seguro e útil, pois evita erros como declarar fora de ordem e definir marca como modelo por exemplo
salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"}) # dois asteriscos declara o argumento como dicionário
# um asterisco apenas retorna como tupla

def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_poema("Zen of Python", "Beautiful is better than ugly.", autor="Tim Peters", ano=1999)
