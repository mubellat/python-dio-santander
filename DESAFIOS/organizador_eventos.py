# Dicionário que vai armazenar os temas como chaves e as listas de participantes como valores
eventos = {}

# Entrada do número de participantes
n = int(input("Quantidade de participantes: ").strip())  # Lê o número total de entradas

# Loop que roda 'n' vezes para coletar os dados dos participantes
for _ in range(n):
    # Lê a linha no formato "Nome, Tema"
    linha = input("Informe o nome e o tema para cada participante: ").strip()
    
    # Separa a string em duas partes: nome e tema
    nome, tema = linha.split(", ")
    
    # Verifica se o tema já está no dicionário
    if tema in eventos:
        # Se sim, adiciona o nome na lista já existente
        eventos[tema].append(nome)
    else:
        # Se não, cria uma nova chave com o tema e inicia a lista com o nome
        eventos[tema] = [nome]

# Imprime os grupos organizados por tema
for tema, participantes in eventos.items():
    print(f"{tema}: {', '.join(participantes)}")  # Junta os nomes separados por vírgula
