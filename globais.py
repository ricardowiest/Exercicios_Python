contas = []
depositos = []
saldo = 0


def main():
    opc = bool(int(input('[1] Criar conta\n[0] Fechar programa\nSua opção: ')))
    while opc:
        criaConta()
        ver_saldo()
        opc = bool(int(input('[1] Criar conta\n[0] Fechar programa\nSua opção: ')))
        if opc == 0:
            break


def criaConta():
    global contas, depositos, saldo
    num_conta = int(input('Digite um número de conta: '))

    while num_conta in contas:
        print('Conta já existente, digite novamente.')
        num_conta = int(input('Digite um número de conta: '))
    contas.append(num_conta)
    deposito = float(input('Digite o valor do primeiro depósito. R$'))
    while deposito<=0:
        print('Valor inválido.')
        deposito = float(input('Digite o valor do primeiro depósito.'))
    depositos.append(deposito)
    saldo += deposito


def ver_saldo():
    global saldo
    op = bool(int(input('Deseja ver saldo do banco? [1-SIM 2-NAO] ')))
    if op:
        print(f'O saldo do banco Ricardo Bank é R${saldo:.2f}')
    

main()