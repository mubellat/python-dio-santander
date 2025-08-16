from abc import ABC

class ControleRemoto(ABC):

    def ligar(self):
        pass
    def desligar(self):
        pass

class ControleTv(ControleRemoto):
    def ligar(self):
        print("Ligando a TV...")
    def desligar(self):
        print("Desligando a TV...")
        print("Desligado")

    @property
    def marca(self):
        return "LG"

class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando o Ar...")
        print("20°")
    def desligar(self):
        print("Desligando o ar...")
        print("Ar ligado")

    @property
    def marca(self):
        return "panasonic"
    
controle = ControleTv()
controle.ligar()
controle.desligar()
