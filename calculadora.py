# Calculadora simples em Python

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Divisão por zero não é permitida."

print("Escolha a operação:")
print("1. Soma")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

operacao = input("Digite o número da operação (1/2/3/4): ")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if operacao == '1':
    print(f"O resultado da soma é: {soma(num1, num2)}")
elif operacao == '2':
    print(f"O resultado da subtração é: {subtracao(num1, num2)}")
elif operacao == '3':
    print(f"O resultado da multiplicação é: {multiplicacao(num1, num2)}")
elif operacao == '4':
    print(f"O resultado da divisão é: {divisao(num1, num2)}")
else:
    print("Operação inválida.")
