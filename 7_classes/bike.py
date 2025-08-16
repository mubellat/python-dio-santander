class Bicicleta:
    def __init__(self, cor, modelo, ano, valor, marcha = 1): # atributos da bicicleta
        self.cor = cor # self é a instancia de cada atributo, não obrigatoriamente tem q ser nomeado assim mas por conveniência usamos self
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.marcha = marcha

    def buzinar(self): # mnétodos de uma classe são similares a funções com necessidade de passar pelo menos um argumento que seria o self
        print("Pim Plim...")

    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada!")

    def correr(self):
        print("Vrummmmmmm...")

    def trocar_marcha(self, numero_marcha): # se passa só o argumento numero_marcha funcionaria normalmente, mas ele estaria no lugar do self e por isso não ia listar o numero_marcha passsado
        print("Trocando marcha...")
        _self = self # para usar a refenrencia internamente

        def _trocar_marcha():
            if numero_marcha > _self.marcha:
                print("Marcha trocada...")
            else:
                print("Não foi possível trocar a marcha...")

    def get_cor(self):
        return self.cor
    
    ''' def __str__(self): # método para exibir a instância
        return f"Bicicleta: cor = {self.cor}, modelo = {self.modelo}, ano = {self.ano}, valor = {self.valor}"
        '''
    
    def __str__(self): # melhor forma de instanciar o objeto
        return f"{self.__class__.__name__}: {", ".join([f"{chave} = {valor}" for chave, valor in self.__dict__.items()])}"

caloi = Bicicleta("vermelha", "caloi", 2022, 600) # definidos os atributos da bicicleta
caloi.buzinar()
caloi.correr()
caloi.parar()
print(caloi.cor, caloi.ano, caloi.modelo, caloi.valor)

gts = Bicicleta("verde", "gts", 2024, 1000)
gts.buzinar()
print(gts.get_cor())
print(gts) # modo para exibir a instância(não convencional pois não é intuitivo)