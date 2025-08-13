# dicionários tem diferencial de ter valor(pode ser mutável) e chave(chave imutável)

# diferentes formas de declarar dicionário:

pessoa = {"nome": "Murilo", "idade": 21}

pessoa = dict(nome="Murilo", idade=21)

pessoa["telefone"] = "8151-7604" # formas de incluir itens no dicionário

print(pessoa["nome"]) # forma de acessar um valor no dicionário

# exemplo de dicionário aninhado:

contatos = {
    "ssz.mu04@gmail.com" : {"nome": "Murilo", "telefone": "8151-7604"},
    "murilo@gmail.com" : {"nome": "Murillo", "telefone" : "2344-5657"},
}

contatos.setdefault(["ssz.mu04@gmail.com"]["idade": 21]) # adiciona chave se ela não existir no dicionário, se já existir retorna o valor já existente e não sobrepõe o novo valor

contatos["ssz.mu04@gmail.com"]["nome"] # forma de acessar

for chave in contatos: # acessando valores por loop
    print(chave, contatos[chave])

for chave, valor in contatos.items(): # outra forma alternativa
    print(chave, valor)

contatos.clear() # limpa todo o dicionário

contatos.copy() # faz cópia do dicionário

dict.fromkeys(["nome", "telefone"]) #  passa chaves e valores None indefinidos, cara queira parametrizar apenas as chaves momentâneamente

dict.fromkeys(["nome", "telefone"], "vazio") # aplica um valor padrão a todas as chaves, no caso "vazio"

contatos.get("chave") # verifica se a chave informada existe no dicionário



contatos.get("chave", {}) # retorna o valor informada cada a chave pedida não exista no dicionário

contatos.keys() # retorna lista com as chaves do dicionário

contatos.pop("ssz.mu04@gmail.com") # remove a chave indicada e retorna oque foi removido
contatos.pop("ssz.mu04@gmail.com", {}) # o segundo valor retorna se a chave não for encontrada

contatos.popitem() # remove itens em sequência, se estiver vazio retorna erro
 
contatos.update({"ssz.mu04@gmail.com": {"nome": "muliro"}}) # atualiza o dicionário com novos parâmetros passados

contatos.values() # retorna todos os valores sem especificar a chave

"ssz.mu04@gmail.com" in contatos # retorna verdadeiro ou falso, forma tradicional de verificação de chave

del contatos["ssz.mu04@gmail.com"]["nome"] # remove "nome" da chave "ssz.mu04@gmail.com"
del contatos["murilo@gmail.com"] # remove toda chave
del contatos # apaga todo o dicionário