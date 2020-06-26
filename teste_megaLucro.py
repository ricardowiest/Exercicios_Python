import random

m_jogo = list()
cont = 0
while cont < 6:
    jogo = random.randint(1,60)
    if not jogo in m_jogo:
        m_jogo.append(jogo)
        cont += 1
    m_jogo.sort()
mega_sena = list(range(1,61))
soma = prequadra = prequina = custo = num = acumulado = 0 
premio = 1500000
while num <= 50063860:
    sorteados = []
    cont = quina = quadra = q = qu = quadra = 0
    mega_sort = mega_sena.copy()
    sorteados = []
    for c in range(6):
        num_sorteados = random.choice(mega_sort)
        sorteados.append(num_sorteados)
        mega_sort.remove(num_sorteados) 
    sorteados.sort()
    if m_jogo != sorteados:
        premio += (premio * 10) / 100
    else:
        acumulado += premio
        premio = 1500000
    for qui in sorteados:
        if qui in m_jogo:
            q +=1
        if q == 5:
            quina += 1
            prequina += (premio * 0.2) / 100
    for qua in sorteados:
        if qua in m_jogo:
            qu += 1
        if qu == 4:
            quadra += 1 
            prequadra += (premio * (1/15000)) / 100
    cont += 1
    soma += cont
    custo += 2.5
    num += 1 
print(f'\033[1:31mResultado do teste {num}: {cont} tentativas.\033[m')
print(f'Foram acertadas {quina} Quinas e {quadra} Quadras.')
print(f'O premio ganho acumulado da Mega em mais de 50 milhões de jogos foi de R${acumulado},00')
print(f'A Quina pagou o total de R${prequina},00 e a Quadra R${prequadra},00')
print(f'O custo total de jogos foi de R${custo}, descontando o total é de R${(acumulado) - (custo)}')
soma /= 50063860
print(f'A média dos resultados foram: {soma}')
