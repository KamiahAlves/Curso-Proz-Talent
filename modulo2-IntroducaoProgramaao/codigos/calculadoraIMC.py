# Problema: João precisa calcular seu Índice de Massa Corporal (IMC) para avaliar seu peso ideal. Sabendo que a fórmula para calcular o IMC é: peso ÷ altura², crie um programa que calcule e informe a classificação do IMC.
# usando apenas if e elif

# Solicita ao usuário que insira o peso e a altura
peso = float(input("Informe seu peso em quilogramas: "))
altura = float(input("Informe sua altura em metros: "))

# Calcula o IMC do João
imc = peso / (altura * altura)

# Verifica a classificação do IMC e  mostrar a ele
if imc < 18.5:
    print("IMC:", imc, "- Peso baixo (eutrofia)")
elif 18.5 <= imc < 25:
    print("IMC:", imc, "- Peso adequado (eutrofia)")
elif 25 <= imc < 30:
    print("IMC:", imc, "- Sobrepeso")
elif 30 <= imc < 35:
    print("IMC:", imc, "- Obesidade grau 1")
elif 35 <= imc < 40:
    print("IMC:", imc, "- Obesidade grau 2")
else:
    print("IMC:", imc, "- Obesidade extrema")

