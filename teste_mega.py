import random

m_jogo = list()
for c in range (1,7):
    jogo = int(input('Digite 6 números para seu jogo: '))
    m_jogo.append(jogo)
n = int(input('Quantos jogos deseja: '))
mega_sena = list(range(1,61))
soma = 0 
for num in range(n):
    sorteados = []
    cont = 0
    while m_jogo != sorteados:
        mega_sort = mega_sena.copy()
        sorteados = []
        for c in range(6):
            num_sorteados = random.choice(mega_sort)
            sorteados.append(num_sorteados)
            mega_sort.remove(num_sorteados)
        sorteados.sort()
        cont += 1
    soma += cont
    print(f'Resultado do teste {num}: {cont} tentativas.')
soma /= n
print (f'A média dos resultados foram: {soma}')
