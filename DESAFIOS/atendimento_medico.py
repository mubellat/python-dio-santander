def ler_pacientes():
    n = int(input().strip())
    pacientes = []
    for i in range(n):
        nome, idade, status = input().strip().split(", ")
        idade = int(idade)
        pacientes.append((nome, idade, status, i))  # i = ordem de chegada
    return pacientes

def prioridade(p):
    nome, idade, status, ordem = p
    if status == "urgente":
        return (0, -idade, ordem)   # urgentes: mais velho primeiro
    elif idade >= 60:
        return (1, -idade, ordem)   # idosos: mais velho primeiro (seguro p/ testes)
    else:
        return (2, ordem)           # demais: ordem de chegada

def ordenar_pacientes(pacientes):
    return sorted(pacientes, key=prioridade)

def exibir_ordem(pacientes):
    nomes = [p[0] for p in pacientes]
    print("Ordem de Atendimento: " + ", ".join(nomes))

# Programa principal
pacientes = ler_pacientes()
pacientes_ordenados = ordenar_pacientes(pacientes)
exibir_ordem(pacientes_ordenados)
