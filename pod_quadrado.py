class quadrado():
    def __init__(self, l):
        self.lado = l


    def muda(self, l):
        l = int(input('Digite o novo tamanho do lado do quadrado: '))
        self.lado = l


    def retorna_valor(self):
        try:
            print(f'\033[1:31mO lado do quadrado mede {self.lado}cm\nO valor total de área é {self.area}cm\033[m')
        except:
            print('Não houve ainda calculo de área.')
            op = input('Deseja calcular? [S/N]: ')
            if op == 'S':
                l.calcula(l)
            else:
                print('Não é possível continuar...')
        else:
            return


    def calcula(self, l):
        l = self.lado
        self.area = l ** 2


l = int(input('Digite o valor do lado do quadrado: '))
l = quadrado(l)
while True:
    try:
        esc = int(input('Digite a opção escolhida: \n[1] - mudar o tamanho do lado\n[2] - Mostrar valor\n[3] - Calcular o valor\n[4] Sair\nOPÇÃO: '))
    except:
        print('Opção inválida!')
        continue
    else:
        if esc == 1:
            l.muda(l)
        elif esc == 2:
            l.retorna_valor()
        elif esc == 3:
            l.calcula(l)
        else:
            print('Até logo!')
            break
