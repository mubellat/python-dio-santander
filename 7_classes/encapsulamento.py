# encapsulamento: agrupa dados e métodos em uma unidade para evitar a modificação acidental de parâmetros que deviam ser imutáveis, isso inclui proteção de acesso para a modificação de dados
# exemplo: no banco o usuario pode alterar seu saldo mas somente passando pelos metodos de sacar e depositar, nao consegue alterar diretamente 

# variavel privada: usamos o underline para especificar que só pode ser manipulada dentro de sua classe (isso é apenas uma convenção) 

class Conta:
    def __init__(self, numero_agencia, saldo = 0):
        self._saldo = saldo
        self.numero_agencia = numero_agencia

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        self._saldo -= valor

    def mostrar_saldo(self):
        return self._saldo

conta = Conta("0001", 100)
conta.depositar(100)
print(conta._saldo)
print(conta.mostrar_saldo())