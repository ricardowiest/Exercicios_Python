import random


def imprime_jogo(matriz):
    numeros = list(range(1,17))
    for cont in range(4):
        linha = []
        for cont in range(4):
            x = random.choice(numeros)
            linha.append(x)
            numeros.remove(x)
        matriz.append(linha)
        


matriz = []
imprime_jogo(matriz)
print(matriz)
