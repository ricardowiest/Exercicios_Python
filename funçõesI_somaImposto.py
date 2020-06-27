def somaImposto(nomeImposto, taxaImposto, custo):
    saldoLiquido = (custo * taxaImposto) / 100
    return f'O imposto {nomeImposto} com saldo bruto {custo} terá alicota de {taxaImposto}: R${saldoLiquido}'


lista = list()
print('\033[1:31:40mPROGRAMA PARA CALCULO DE IMPOSTOS\033[m')
while True:
    esc = int(input('Escola uma opção: \n[1] Cadastrar\n[2] Excluir\n[3] Ver todos\n[4] Sair')
    if esc == 1:
        imposto = str(input('Digite qual imposto deseja incluir: '))
        valor = float(input('Qual o valor liquido antes do imposto: R$'))
        alicota = float(input('Qual a taxa da referido imposto: '))
        somaImposto(imposto, alicota, valor)
        lista.append(somaImposto)
    elif esc == 2:
        lista.pop
    elif esc == 3:
        for c in lista:
            print(f'{c}\n')
    elif esc == 4:
        print('Finalizando...')
        break
    else:
        print('OPÇÃO INVALIDA.')
