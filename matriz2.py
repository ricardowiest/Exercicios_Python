def init_matriz(l, c, matriz):
    for k in range(1, l+1):
        linha = []
        for d in range(1, c+1):
            num = int(input(f'Digite o elemento {k}-{d} da matriz: '))
            linha.append(num)
        matriz.append(linha)

def change_elemento(a1, a2, matriz):
    element1 = matriz[a1//10][a1%10]
    element2 = matriz[a2//10][a2%10]
    matriz[a1//10][a1%10] = element2
    matriz[a2//10][a2%10] = element1


matriz = []
l = int(input('Digite um número de linhas para a matriz: '))
c = int(input('Digite um número de colunas para a matriz: '))
init_matriz(l, c, matriz)
print(matriz)

a1 = int(input('Digite a posição do elemento 1: '))
a2 = int(input('Digite a posição do elemento 2: '))
change_elemento(a1, a2, matriz)
print(matriz)

