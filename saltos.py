lista = list()

try:
    nome = str(input('\033[1:31:41mNome do Atleta:\033[m '))
    print('-'*20)
    for c in range(1, 6):
        salto = float(input(f'\033[1:31:40mDigite altura do {c}º:\033[m '))
        lista.append(salto)
    lista.sort(reverse=True)
    med = 0
    for c in lista[1:4]:
        med = sum(lista) - max(lista) - min(lista)
        media = med / 3
except ValueError:
    print('Erro...')

else:
    print('-'*20)
    print('RESULTADO FINAL')
    print(f'Atleta: {nome}')
    print(f'Saltos: {lista}')
    print(f'Média de Saltos: {media}m.')
