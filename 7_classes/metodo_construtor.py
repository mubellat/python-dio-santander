class Cachorro:
    def __init__(self, nome, cor, acordado=True): # sempre usar init quando uma nova instância de classe é criada
        print("Inicializando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self): # remover instancia da classe, não muito usado pois python tem sistema de gerenciamento de memória
        print("Removendo a instância da classe.")

    def falar(self):
        print("auauaua")


def criar_cachorro():
    c = Cachorro("Zeus", "branco e preto", False)
    print(c.nome)

c = Cachorro("Chappie", "amarelo")
c.falar()

del c # forçando remoção

criar_cachorro()