from pacotes.pac import pacote
from time import sleep

lista = list()

with open('arquivo.txt') as arq:
    line = arq.readline().split(' , ')
    for c in line:
        lista.append(c)

pacote.cabecalho()
cont = 1
c = 0
for linha in lista:
    print(f'{cont:<5}', end=' ')
    print(f'{linha[c]:<18}')
    cont += 1
    c += 1
