# polimorfismo: mesmo nome de função (mas assinaturas diferentes) sendo usado para tipos diferentes
# função len é um exemplo de polimorfismo, como se lê uma string e pode se ler uma lista

class Passaro:
    def voar(self):
        print("Voado...")

class Pardal(Passaro):
    def voar(self):
        print("Pardal voando...")

class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não pode voar")

class Aviao(Passaro):
    def voar(self):
        print("Avião está decolando...")

def plano_de_voo(obj):
    obj.voar()

plano_de_voo(Pardal())
plano_de_voo(Avestruz())
plano_de_voo(Aviao())