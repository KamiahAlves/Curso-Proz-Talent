# Atividade 

Faça uma função calculadora de dois números com três parâmetros: os dois primeiros serão os números da operação e o terceiro será a entrada que definirá a operação a ser executada. Considera a seguinte definição:
1. Soma
2. Subtração
3. Multiplicação
4. Divisão

Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.

# Resposta

````
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
````

## Se quiser rodar o código completo

🖥️▶️ Google Colab https://colab.research.google.com/drive/1NvjboHRGj7lB2U2_tlWDq9wXAW2_eICX?usp=sharing
