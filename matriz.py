import random


def init_matriz(matriz):
    lista = list(range(16))
    for c in range(4):
        linha = []
        for c in range(4):
            x = random.choice(lista)
            linha.append(x)
            lista.remove(x)
        matriz.append(linha)



matriz = []
init_matriz(matriz)
print(matriz)
    