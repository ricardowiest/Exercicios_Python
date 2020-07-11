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


def muda_jogo(posicao1L, posicao1C, posicao2L, posicao2C, matriz):
    print('-' * 15)
    peca1 = matriz[posicao1L][posicao1C]
    peca2 = matriz[posicao2L][posicao2C]
    matriz[posicao1L][posicao1C] = peca2
    matriz[posicao2L][posicao2C] = peca1
    for cont in range(4):
        linha = matriz[cont]
        print(linha)
    print('-' * 15)


matriz = []
cria_jogo(matriz)

while True:
    linhaPeca = int(input('Digite a linha da peça que deseja selecionar: [0 a 3] '))
    colunaPeca = int(input('Digite a coluna da peça que deseja selecionar: [0 a 3] '))
    linhaTroca = int(input('Digite a linha da peça a ser trocada: [0 a 3] '))
    colunaTroca = int(input('Digite a coluna da peça a ser trocada: [0 a 3] '))
    muda_jogo(linhaPeca, colunaPeca, linhaTroca, colunaTroca, matriz)
    