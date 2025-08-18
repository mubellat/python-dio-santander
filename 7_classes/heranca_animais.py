# Classe base Animal
class Animal:
    def __init__(self, numero_patas):
        self.numero_patas = numero_patas

# Classe Mamífero que herda de Animal
class Mamifero(Animal):
    def __init__(self, cor_pelo, **kwargs):
        self.cor_pelo = cor_pelo
        # Chama o init da próxima classe na MRO com os argumentos restantes
        super().__init__(**kwargs)

    def __str__(self):
        return "Mamifero"

# Mixin que adiciona a funcionalidade de falar
class FalarMixin:
    def falar(self):
        return "OI ESTOU FALANDO"

# Classe Ave que também herda de Animal
class Ave(Animal):
    def __init__(self, cor_bico, **kwargs):
        self.cor_bico = cor_bico
        # Chama o init da próxima classe na MRO com os argumentos restantes
        super().__init__(**kwargs)

# Cachorro, Gato e Leão herdam de Mamífero diretamente
class Cachorro(Mamifero):
    pass

class Gato(Mamifero):
    pass

class Leao(Mamifero):
    pass

# Ornitorrinco herda de Mamífero, Ave e FalarMixin
class Ornitorrinco(Mamifero, Ave, FalarMixin):
    def __init__(self, cor_pelo, cor_bico, numero_patas):
        # Apenas para estudo: imprime a ordem de resolução de métodos
        print("MRO:", Ornitorrinco.__mro__)  # Tupla
        print("MRO:", Ornitorrinco.mro())    # Lista

        # Envia todos os parâmetros como kwargs para a cadeia de super().__init__
        super().__init__(cor_pelo=cor_pelo, cor_bico=cor_bico, numero_patas=numero_patas)

    def __str__(self):
        return "Ornitorrinco"

# Criação de um objeto Gato
gato = Gato(numero_patas=4, cor_pelo="amarelo")
print(gato)  # Vai imprimir "Mamifero" pois Gato herda de Mamifero que tem __str__

# Criação de um objeto Ornitorrinco
ornitorrinco = Ornitorrinco(numero_patas=2, cor_pelo="vermelho", cor_bico="laranja")
print(ornitorrinco)          # Vai imprimir "Ornitorrinco"
print(ornitorrinco.falar())  # Método herdado do FalarMixin
