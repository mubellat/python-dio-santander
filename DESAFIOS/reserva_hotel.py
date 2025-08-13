def ler_quartos_disponiveis():
    """Lê os quartos disponíveis e retorna como conjunto (para busca rápida)."""
    return set(map(int, input().split()))

def ler_reservas_solicitadas():
    """Lê as reservas solicitadas e retorna como lista."""
    return list(map(int, input().split()))

def verificar_reservas(disponiveis, solicitadas):
    """Verifica quais reservas podem ser confirmadas e quais devem ser recusadas."""
    confirmadas = []
    recusadas = []
    for quarto in solicitadas:
        if quarto in disponiveis:
            confirmadas.append(quarto)
        else:
            recusadas.append(quarto)
    return confirmadas, recusadas

def exibir_resultado(confirmadas, recusadas):
    """Exibe o resultado no formato exigido."""
    print("Reservas confirmadas:", " ".join(map(str, confirmadas)))
    print("Reservas recusadas:", " ".join(map(str, recusadas)))

def processar_reservas():
    disponiveis = ler_quartos_disponiveis()
    solicitadas = ler_reservas_solicitadas()
    confirmadas, recusadas = verificar_reservas(disponiveis, solicitadas)
    exibir_resultado(confirmadas, recusadas)

# Chamada da função principal
processar_reservas()
