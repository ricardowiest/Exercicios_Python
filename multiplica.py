def multi(*lista_):
    total_multi = 1
    for c in lista_:
        total_multi *= c
    return total_multi


def soma(*lista_):
    total_soma = 0
    for c in lista_:
        total_soma = sum(c)
    return total_soma

lista = list()
esc = 'S'
while esc == 'S':
    esc = ''
    num = int(input('Digite um número para equações: '))
    lista.append(num)
    while True:
        esc = str(input('Deseja Continuar? [S/N]: ')).upper().strip()[0]
        if esc in 'NS':
            break
        elif esc not in 'SN':
            print('Erro, opção inválida.')
print(f'As equações com de todos os números foram: \nMultipliação: {multi(lista)} \nSoma: {soma(lista)}')
