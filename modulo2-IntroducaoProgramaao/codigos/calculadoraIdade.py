import datetime

def calcular_idade(ano_nascimento):
    ano_atual = datetime.datetime.now().year
    idade = ano_atual - ano_nascimento
    return idade

while True:
    nome_completo = input("Digite seu nome completo: ")
    
    while True:
        try:
            ano_nascimento = int(input("Digite o ano de nascimento (1922-2021): "))
            if 1922 <= ano_nascimento <= 2021:
                break
            else:
                print("Ano de nascimento fora do intervalo permitido. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número válido para o ano de nascimento.")

    idade = calcular_idade(ano_nascimento)

    print(f"Nome: {nome_completo}")
    print(f"Idade em 2022: {idade} anos")

    continuar = input("Deseja calcular a idade de outra pessoa? (S/N): ").strip().lower()
    if continuar != 's':
        break
