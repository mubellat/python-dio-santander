class Animal:  # Classe-base para animais
    def __init__(self, numero_patas):  # Construtor recebe o número de patas
        self.numero_patas = numero_patas  # Armazena o número de patas na instância


class Mamifero(Animal):  # Mamífero herda de Animal
    def __init__(self, cor_pelo, **kwargs):  # Recebe cor do pelo e repassa o restante via kwargs
        self.cor_pelo = cor_pelo  # Define o atributo específico de Mamífero
        super().__init__(**kwargs)  # Chama o próximo __init__ na MRO (ex.: Animal) com os argumentos restantes

    def __str__(self):  # Representação em string de um Mamífero
        return "Mamifero"  # Texto mostrado ao usar print(instancia)


class FalarMixin:  # Mixin que adiciona comportamento de "falar"
    def falar(self):  # Método extra, não interfere em __init__
        return "OI ESTOU FALANDO"  # Retorna a fala


class Ave(Animal):  # Ave herda de Animal
    def __init__(self, cor_bico, **kwargs):  # Recebe cor do bico e repassa o restante via kwargs
        self.cor_bico = cor_bico  # Define o atributo específico de Ave
        super().__init__(**kwargs)  # Chama o próximo __init__ na MRO com os argumentos restantes


class Cachorro(Mamifero):  # Cachorro é um Mamífero
    pass  # Sem alterações adicionais; usa o __init__ de Mamífero


class Gato(Mamifero):  # Gato é um Mamífero
    pass  # Sem alterações adicionais; usa o __init__ de Mamífero


class Leao(Mamifero):  # Leão é um Mamífero
    pass  # Sem alterações adicionais; usa o __init__ de Mamífero


class Ornitorrinco(Mamifero, Ave, FalarMixin):  # Ornitorrinco herda de Mamífero, Ave e do mixin Falar
    def __init__(self, cor_pelo, cor_bico, numero_patas):  # Construtor recebe todos os atributos necessários
        print(Ornitorrinco.__mro__)  # Mostra a tupla da ordem de resolução de métodos (MRO)
        print(Ornitorrinco.mro())    # Mostra a lista da MRO (mesma informação, outro formato)

        # Chamada cooperativa do super com argumentos NOMEADOS, para múltipla herança funcionar:
        # - Mamifero.__init__ consome cor_pelo e repassa cor_bico/numero_patas
        # - Ave.__init__ consome cor_bico e repassa numero_patas
        # - Animal.__init__ consome numero_patas
        super().__init__(cor_pelo=cor_pelo, cor_bico=cor_bico, numero_patas=numero_patas)

    def __str__(self):  # Representação em string do Ornitorrinco
        return "Ornitorrinco"  # Texto mostrado ao usar print(instancia)


gato = Gato(numero_patas=4, cor_pelo="amarelo")  # Cria um Gato (usa __init__ de Mamífero + Animal)
print(gato)  # Imprime "Mamifero" pois Gato herda o __str__ de Mamifero

ornitorrinco = Ornitorrinco(numero_patas=2, cor_pelo="vermelho", cor_bico="laranja")  # Instancia um Ornitorrinco
print(ornitorrinco)  # Imprime "Ornitorrinco" pelo __str__ definido na classe
print(ornitorrinco.falar())  # Chama método do mixin FalarMixin -> "OI ESTOU FALANDO"
