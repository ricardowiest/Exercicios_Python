class conta_corrente(object):
    saldo = 0
    reserva = 0.10 * saldo

    def __init__(self, ID, saldo):
        self.id = ID
        self.saldo = saldo

    def deposito_conta(self, deposito):
        self.saldo += deposito

    def saque_conta(self, saque):
        if self.saldo >= saque:
            self.saldo -= saque
        else:
            print('\033[1:31mDesculpe, o saldo é insuficiente.\033[m')

    def mostra_saldo(self):
        print(f'Conta Corrente Nº{self.id} - Saldo total: \033[1:36m[R$ {self.saldo} ]\033[m')

def menu():
    print('-'*50)
    print(' '*15, '\033[1:31:40mBANCO DO POVO\033[m')
    print('-'*50)
    print()
    print('\033[1:32mOPÇÕES: \n  [ 1 - ABRIR / INFORMAR CONTA]\n  [ 2 - DEPOSITAR EM CONTA    ]\n  [ 3 - SAQUE EM CONTA        ]\n  [ 4 - MOSTRAR SALDO         ]\n  [ 5 -          SAIR         ]\033[m')
    print('-\033[m'*50)


while True:
    try:
        menu()
        esc = int(input('Sua opção: '))

    except:
        print('Sua opção foi inválida!')

    else:
        if not 1 <= esc <= 5:
            print('Opção Inválida!')
            continue
        if esc == 1:
            num = int(input('Digite o número da conta: '))
            val = float(input('Digite o depósito inicial R$ '))
            conta = conta_corrente(num, val)
        if esc == 2:
            dep = float(input('Digite o valor do depósito R$ '))
            conta.deposito_conta(dep)
        if esc == 3:
            saque = float(input('Digite o valor de saque R$'))
            conta.saque_conta(saque)
        if esc == 4:
            conta.mostra_saldo()
        if esc == 5:
            print('Até logo! Volte sempre...')
            break