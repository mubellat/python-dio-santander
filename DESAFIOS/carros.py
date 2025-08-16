from datetime import datetime

# Classe Veiculo com atributos marca, modelo e ano
class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    # Método para verificar se o veículo é antigo
    def verificar_antiguidade(self):
        ano_atual = datetime.now().year
        idade = ano_atual - self.ano
        if idade > 20:
            return "Veículo antigo"
        else:
            return "Veículo novo"

# Entrada direta
marca = input().strip()
modelo = input().strip()
ano = int(input().strip())

# Instanciando o objeto e verificando a antiguidade
veiculo = Veiculo(marca, modelo, ano)
print(veiculo.verificar_antiguidade())
