def calcular(operacao):
    def somar(a, b):
        return a + b
    
    def subtrair(a, b):
        return a - b
    
    def multi(a, b):
        return a * b
    
    def div(a, b):
        return a / b
    
    match operacao:
        case "+":
            return somar
        case "-":
            return subtrair
        case "/":
            return div
        case "*":
            return multi 
    
resultado = calcular("+")(1, 3)
print(resultado)