
# ATIVIDADE 3 - Lógica Imperativa

- Elabore um algoritmo que possa descobrir, através de perguntas e respostas, em qual área de um restaurante uma pessoa ou grupo de pessoas precisa ser alocada.
- O restaurante tem três áreas: térreo, 1ro andar, e área externa.
- Clientes fumantes ou com animais de estimação precisam ser alocadas na área externa.
- Grupos de 5 ou mais precisam ser alocados no 1º andar, pois não dá para juntar mesas no térreo.
- Qualquer outro grupo de pessoas pode ser alocado no térreo.

## Resposta

Aproveitando que estamos vendo sobre o comando "SE" fiz um algoritmo que confere o tamanho do grupo e os dados pedidos na atividade (fumantes e animais de estimação) para determinar a área mais apropriada para eles no restaurante.

O uso de estruturas condicionais permite que o algoritmo faça escolhas com base nas informações fornecidas pelo usuário e forneça uma resposta adequada. Assim, a gente consegue validar todas as opções independente do cliente

```

var
    quantidadePessoas, fumante, animaisEstimacao: inteiro

inicio
    escreva("Quantas pessoas estão no grupo? ")
    leia(quantidadePessoas)

    escreva("Algum membro do grupo é fumante? (1 para Sim, 0 para Não) ")
    leia(fumante)

    escreva("Algum membro do grupo tem animais de estimação? (1 para Sim, 0 para Não) ")
    leia(animaisEstimacao)

    se quantidadePessoas >= 5 então
        escreva("O grupo deve ser alocado no 1º andar.")
    senão se fumante = 1 ou animaisEstimacao = 1 então
        escreva("O grupo deve ser alocado na área externa.")
    senão
        escreva("O grupo pode ser alocado no térreo.")
    fimse
fimalgoritmo

```
