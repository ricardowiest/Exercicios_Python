import math

print('\033[1:31:42m-\033[m'*40)
print(f'\033[3:33m{"Cálculo Fatorial":^40}\033[m')
print('\033[1:31:42m-\033[m'*40)

while True:
    try:
        num = int(input('\033[1:34mDigite um número para cálculo: \033[m'))
    except:
        print('Digito inválido, digite um número...')
        continue
    else:
        fat = math.factorial(num)
        '''fat = 1
        for c in range(num, 0, -1):
            fat *= c'''
        print(f'\033[1:35mRESULTADO: {fat}\033[m')
