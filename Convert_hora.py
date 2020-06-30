def convert(h, m):
    if 12 < h <= 24:
        hora = h - 12
        nom = 'PM'
        minu = m
    else:
        hora = h
        nom = 'AM'
        minu = m
    print(f'\033[1:32:41m{hora}:{m} {nom}\033[m')
    return


while True:
    print('-=' * 25)
    print('Conversor de HORAS 22:00 >>> 10:00 PM')
    print('-=' * 25)
    esc = int(input('[1] CONVERSÃO\n[2] SAIR\nESCOLHA: '))
    if esc == 1:
        hor = int(input('Digite a hora: '))
        minuto = int(input('Digite os minutos: '))
        convert(hor, minuto)
    elif esc == 2:
        print('\033[31:45mFinalizando...\033[m')
        break
    else:
        print('\033[2:32:40mERRO...Opção inválida\033[m')
