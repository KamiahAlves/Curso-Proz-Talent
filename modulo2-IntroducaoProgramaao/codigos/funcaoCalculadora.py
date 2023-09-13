def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: Divisão por zero"
    return a / b

while True:
    print("Selecione a operação:")
    print("1: Soma")
    print("2: Subtração")
    print("3: Multiplicação")
    print("4: Divisão")
    print("0: Sair")

    opcao = input("Digite o número da operação desejada: ")

    if opcao == '0':
        print("Encerrando a calculadora.")
        break
    elif opcao not in ['1', '2', '3', '4']:
        print("Essa opção não existe. Por favor, escolha uma opção válida.")
        continue

    num1 = float(input("Digite o primeiro valor: "))
    num2 = float(input("Digite o segundo valor: "))

    if opcao == '1':
        resultado = soma(num1, num2)
        print(f"Resultado: {resultado}")
    elif opcao == '2':
        resultado = subtracao(num1, num2)
        print(f"Resultado: {resultado}")
    elif opcao == '3':
        resultado = multiplicacao(num1, num2)
        print(f"Resultado: {resultado}")
    elif opcao == '4':
        resultado = divisao(num1, num2)
        print(f"Resultado: {resultado}")
