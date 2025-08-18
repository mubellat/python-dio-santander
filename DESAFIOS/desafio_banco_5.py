from abc import ABC, abstractmethod
from datetime import datetime


def log_transacao(func):
    def wrapper(self, conta):
        # Verifica limite diário
        if conta.historico.transacoes_do_dia() >= 10:
            msg = f"{datetime.now()} | ⚠️ Limite diário de 10 transações atingido."
            print(msg)
            with open("log.txt", "a", encoding="utf-8") as f:
                f.write(msg + "\n")
            return False

        resultado = func(self, conta)

        # Monta mensagem de log
        log_msg = (
            f"{datetime.now()} | Função: {func.__name__} | "
            f"Args: valor={self.valor}, conta={conta.numero} | "
            f"Retorno: {resultado}"
        )

        # Exibe no console e salva no log
        print(log_msg)
        with open("log.txt", "a", encoding="utf-8") as f:
            f.write(log_msg + "\n")

        if resultado:  # só registra se for sucesso
            tipo = self.__class__.__name__
            conta.historico.adicionar_transacao(tipo, self.valor)

        return resultado
    return wrapper


class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, tipo, valor):
        horario = datetime.now()
        self.transacoes.append({
            "tipo": tipo,
            "valor": valor,
            "horario": horario
        })

    def exibir(self):
        for t in self.transacoes:
            print(f"[{t['horario'].strftime('%Y-%m-%d %H:%M:%S')}] {t['tipo']} de R$ {t['valor']:.2f}")

    def gerar_transacoes(self, tipo=None):
        for t in self.transacoes:
            if tipo is None or tipo in t["tipo"]:
                yield f"[{t['horario'].strftime('%Y-%m-%d %H:%M:%S')}] {t['tipo']} de R$ {t['valor']:.2f}"

    def transacoes_do_dia(self):
        """Conta transações realizadas hoje."""
        hoje = datetime.now().date()
        return sum(1 for t in self.transacoes if t["horario"].date() == hoje)


class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome, cpf, data_nascimento, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento


class Conta:
    def __init__(self, numero, cliente):
        self.saldo = 0.0
        self.numero = numero
        self.agencia = "0001"
        self.cliente = cliente
        self.historico = Historico()

    def __str__(self):
        return f"Agência: {self.agencia} | Conta: {self.numero} | Titular: {self.cliente.nome} | Saldo: R$ {self.saldo:.2f}"

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente.")
            return False
        if valor <= 0:
            print("Valor inválido.")
            return False
        self.saldo -= valor
        print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        return True

    def depositar(self, valor):
        if valor <= 0:
            print("Valor inválido para depósito.")
            return False
        self.saldo += valor
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        return True


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques
        self.numero_saques = 0

    def sacar(self, valor):
        if self.numero_saques >= self.limite_saques:
            print("Limite de saques diários alcançado.")
            return False
        if valor > self.limite:
            print("Valor excede o limite permitido.")
            return False
        sucesso = super().sacar(valor)
        if sucesso:
            self.numero_saques += 1
        return sucesso


class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass


class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor

    @log_transacao
    def registrar(self, conta):
        return conta.depositar(self.valor)


class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    @log_transacao
    def registrar(self, conta):
        return conta.sacar(self.valor)


class Banco:
    def __init__(self):
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def __iter__(self):
        for conta in self.contas:
            yield (conta.numero, conta.saldo)


if __name__ == "__main__":
    banco = Banco()

    cliente1 = PessoaFisica("João Silva", "12345678900", "01-01-1990", "Rua A, 123")
    conta1 = ContaCorrente.nova_conta(cliente1, 1)
    cliente1.adicionar_conta(conta1)
    banco.adicionar_conta(conta1)

    # Testando algumas operações
    deposito = Deposito(200)
    cliente1.realizar_transacao(conta1, deposito)

    saque = Saque(50)
    cliente1.realizar_transacao(conta1, saque)

    print("\n=== Histórico de Transações ===")
    conta1.historico.exibir()

    print("\n=== Gerador: Apenas Saques ===")
    for t in conta1.historico.gerar_transacoes("Saque"):
        print(t)

    print("\n=== Iterador: Contas do Banco ===")
    for numero, saldo in banco:
        print(f"Conta {numero} | Saldo: R$ {saldo:.2f}")
