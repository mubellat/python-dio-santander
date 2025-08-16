# herança: uma classe filha herda características e comportamentos de uma classe pai/base

# herança simples: herda apenas de uma classe pai/base
# herança múltipla: não são todas linguagens que usam esse conceito, pode herdar de várias classes como class C(A, B):

class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando o motor...")

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado

    def esta_carregado(self): # existe apenas na classe Caminhao
        print(f"{"Sim," if self.carregado else "Não"} estou carregado")
    
    def __str__(self):
        return super().__str__(), self.cor

moto = Motocicleta("preto", "ABC-1234", 2) # nao funciona por nao especificar os atributos mesmo que nao seja especificado na classe, porém como é herança de uma classe pai eu preciso especificar os atributos que tem na classe que ela herda
moto.ligar_motor()

carro = Carro("Branco", "ABD", 4)
caminhao = Caminhao("roxo", "GFD", 8, True)
caminhao.ligar_motor()
caminhao.esta_carregado()
print(caminhao)