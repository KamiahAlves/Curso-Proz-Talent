# ▶️ Aula 5 - ao vivo

## Aprendendo Estruturas de Repetição em Python

Neste arquivo, você encontrará informações sobre estruturas de repetição em Python, explicadas de forma simples para iniciantes.

## Estruturas de Repetição em Python

### Loop "for"

Um loop "for" é usado quando você sabe quantas vezes deseja repetir um conjunto de instruções. Ele é frequentemente usado para iterar através de sequências.

Exemplo de loop "for" para imprimir números de 1 a 5:

```
for i in range(1, 6):
    print(i)
```

### Loop "while"

Um loop "while" é usado quando você não sabe quantas vezes deseja repetir um conjunto de instruções, e a repetição continua até que uma condição seja falsa.

Exemplo de loop "while" para imprimir números pares até 10:

```
numero = 2
while numero <= 10:
    print(numero)
    numero += 2
```

## Exemplos do Dia a Dia

### 1. Lista de Compras

Um loop "for" pode ser usado para iterar através de uma lista de compras e imprimir cada item:

```
lista_de_compras = ["maçãs", "bananas", "leite", "pão", "ovos"]

for item in lista_de_compras:
    print("Comprar:", item)
```

### 2. Pesquisa de Satisfação

Um loop "while" pode ser usado para solicitar entrada do usuário até que uma resposta válida seja dada:

```
resposta = ""
while resposta != "sim" and resposta != "não":
    resposta = input("Você está satisfeito com nosso serviço? (sim/não): ")

print("Obrigado por responder!")
```

## Dicas Extras

### O que faz o `range()`?

A função `range()` é usada para gerar uma sequência de números em um intervalo específico. Ela é comumente usada em loops "for". A sintaxe básica é:

```
range(início, fim, passo)
```

- `início`: Valor inicial da sequência (inclusive).
- `fim`: Valor final da sequência (exclusivo).
- `passo` (opcional): Incremento entre os números na sequência (padrão é 1).

### Usando Listas

As listas são estruturas de dados importantes em Python. Você pode criar, acessar, adicionar e modificar elementos em listas. Aqui está um exemplo de criação de uma lista:

```
minha_lista = [1, 2, 3, 4, 5]
```

Você pode acessar elementos por índice, adicionar elementos com `append()` e muito mais.

### Usando `continue` e `break`, ambos são usadas para controlar o fluxo de execução dentro de loops.

**1. `continue`:**

A palavra-chave `continue` é usada em loops (como "for" ou "while") para pular a iteração atual e passar para a próxima iteração. Em outras palavras, quando o Python encontra a instrução `continue`, ele interrompe a execução do bloco de código atual no loop e avança para a próxima iteração do loop. O `continue` é útil quando você deseja ignorar parte do código em uma iteração específica e continuar com o próximo ciclo.

Aqui está um exemplo de como o `continue` funciona em um loop "for":

```
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
```

Neste exemplo, quando `i` é igual a 3, o `continue` é acionado, e o número 3 não é impresso. O loop continua com os valores restantes (1, 2, 4, 5).

**2. `break`:**

A palavra-chave `break` é usada para sair imediatamente de um loop, independentemente da condição que controla o loop. Quando o Python encontra a instrução `break`, ele encerra a execução do loop e continua com o código após o loop.

Aqui está um exemplo de como o `break` funciona em um loop "while":

```
numero = 1
while numero <= 5:
    if numero == 3:
        break
    print(numero)
    numero += 1
```

Neste exemplo, quando `numero` se torna igual a 3, o `break` é acionado, e o loop "while" é encerrado imediatamente. O resultado impresso será apenas os números 1 e 2.

**Dicas:**

- Use `continue` quando você deseja pular uma iteração específica e continuar com o próximo ciclo.
- Use `break` quando você deseja sair completamente de um loop antes de atingir a condição de parada normal.


# 🔗 Link com as atividades da aula

👩‍🏫 **atividades:** https://colab.research.google.com/drive/1190ZhtyzMV7uK0-g95oO5fSLLdomCm1n?usp=sharing

💻 **para treinar:** https://studio.code.org/s/course4/lessons/9/levels/1



