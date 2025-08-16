# metodo classe: ligados a classe e nao ao objeto
# metodo estatico: nao recebe primeiro argumento, nao modifica a classe

class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome 
        self.idade = idade

    @classmethod
    def criar_apartir_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2022 - ano
        return cls(nome, idade)
    
    @staticmethod
    def e_maior_de_idade(idade):
        return idade > 17

# p = Pessoa("Muliro", 20)

p2 = Pessoa.criar_apartir_data_nascimento(1994, 3, 20, "Muliro")
print(p2)

print(Pessoa.e_maior_de_idade(18))
print(Pessoa.e_maior_de_idade(15))