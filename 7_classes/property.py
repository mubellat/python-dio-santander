class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self._nome = nome
        self.ano_nascimento = ano_nascimento

    @property
    def nome(self):
        return self._nome
    
    @property
    def idade(self):
        _ano_atual = 2022
        return _ano_atual - self.ano_nascimento
    
    def get_nome(self):
        return self._nome
    
    def get_idade(self):
        return 2022 - self._ano_nascimento
    
pessoa = Pessoa("Guilherme", 1994)
print(f"Nome: {pessoa.nome} \tIdade: {pessoa.idade}")
print(f"Nome: {pessoa.get_nome()} \tIdade: {pessoa.get_idade()}")