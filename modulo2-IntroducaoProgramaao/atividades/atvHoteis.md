# Desenvolvimento 

Precisamos imprimir um número para cada andar de um hotel de 20 andares. Porém, o dono do hotel é supersticioso e optou por não ter um 13ro andar.

Escreva um código que imprima todos os números exceto o número 13.
Escreva mais dois códigos que resolvam o mesmo problema, mas dessa vez usando os outros dois tipos de laços de repetição aprendidos.

Como desafio, imprima eles em ordem decrescente (20, 19, 18...)

# Resposta

Este repositório contém três abordagens para resolver o problema acima.

## Usando um loop for

```
for andar in range(1, 21):
    if andar != 13:
        print(andar)
```

## Usando um loop while

```
andar = 1
while andar <= 20:
    if andar != 13:
        print(andar)
    andar += 1
```

## Usando um loop for com break

```
andares = list(range(1, 21))
andares.remove(13)

for andar in range(20, 0, -1):
    if andar == 13:
        continue
    print(andar)
```
