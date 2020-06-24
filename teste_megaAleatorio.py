import random

m_jogo = list()
cont = 0
while cont < 6:
    jogo = random.randint(1,60)
    if not jogo in m_jogo:
        m_jogo.append(jogo)
        cont += 1
    m_jogo.sort()
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
    print(f'\033[1:31mResultado do teste {num}: {cont} tentativas.\033[m')
soma /= n
print (f'A média dos resultados foram: {soma}')
