import random


def cria_jogo(matriz):
    numeros = list(range(1,17))
    print('-'*15)
    for cont in range(4):
        linha = []
        for cont in range(4):
            x = random.choice(numeros)
            linha.append(x)
            numeros.remove(x)
        print(f'{linha}')
        matriz.append(linha)
    print('-'*15)


def muda_jogo(posicao1, posicao2, matriz):
    print('-' * 15)
    peca1 = matriz[posicao1][posicao1]
    peca2 = matriz[posicao2 // 10][posicao2 % 10]
    matriz[posicao1 // 10][posicao1 % 10] = peca2
    matriz[posicao2 // 10][posicao2 % 10] = peca1
    for cont in range(4):
        linha = matriz[cont]
        print(linha)
    print('-' * 15)


matriz = []
cria_jogo(matriz)

while True:
    linha = int(input('Digite a linha que deseja selecionar: '))
    coluna = int(input('Digite a coluna que deseja selecionar: '))
    muda_jogo(linha, coluna, matriz)
    