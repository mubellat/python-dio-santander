class Estudante:
    escola = "DIO"

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self):
        return f"{self.nome} {self.matricula} - {self.escola}"
    
def mostrar_valores(*objs):
    for obj in objs:
        print(obj)
    
gui = Estudante("Guilherme", 56451)
gi = Estudante("Giovana", 17323)

print(gui)
print(gi)

mostrar_valores(gui, gi)
gui.matricula = 3
Estudante.escola = "Python"
mostrar_valores(gui, gi)
muliro = Estudante("muliroliro", 2)