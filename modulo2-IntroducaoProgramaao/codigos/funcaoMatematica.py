# para o usuario informar os numeros

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = int(input("Escolha a operação (1 - Soma, 2 - Subtração, 3 - Multiplicação, 4 - Divisão): "))

# funcao para fazer as contas matematicas

def calculadora(numero1, numero2, operacao):
    if operacao == 1:
        return numero1 + numero2
    elif operacao == 2:
        return numero1 - numero2
    elif operacao == 3:
        return numero1 * numero2
    elif operacao == 4 and numero2 != 0:
        return numero1 / numero2
    else:
        return 0


# salvar o resultado da função em uma variavel

resultado = calculadora(num1, num2, operacao)

# a condição pedida no caso seja um numero que não exista

if resultado != 0:
    print("Resultado da operação:", resultado)
else:
    print("Operação não reconhecida ou divisão por zero.")
