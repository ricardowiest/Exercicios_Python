def main():
    arquivo = open("usuarios.txt", 'r')

    linha = arquivo.readline()

    espaçoTotal = 0
    usuarios = []

    while linha != '':
        separado = linha.split()
        removeEspaços(separado)

        espaçoTotal += int(separado[1])

        usuarios.append(separado)

        linha = arquivo.readline()

    arquivo.close()

    espaçoTotal /= (1024 ** 2)

    geraRelatorio(usuarios, espaçoTotal)


def removeEspaços(splited):
    while splited.count('') != 0:
        splited.remove('')


def geraRelatorio(usuarios, espaçoTotal):
    relatorio = open('relatorio.txt', 'w')

    CalculaEspaçoUtilizado(usuarios)
    porc = CalculaPorcentagem(usuarios, espaçoTotal)

    relatorio.write('ACME Inc.               Uso do espaço em disco pelos usuários\n')
    relatorio.write(72 * '-' + '\n')
    relatorio.write('Nr.  Usuário        Espaço utilizado     % do uso\n')
    maior = EspaçosASeremColocados(usuarios)

    relatorio.write('\n')

    for i in range(len(usuarios)):
        linha = '%i' % (i + 1)
        linha += (5 - len(linha)) * ' '

        linha += usuarios[i][0] + (15 - len(usuarios[i][0])) * ' '

        num = "%.2f" % usuarios[i][1]
        espaço_inicio = (maior - len(num)) * ' '
        num += ' MB'
        espaço_fim = (23 - len(espaço_inicio) - len(num)) * ' '
        linha += espaço_inicio + num + espaço_fim

        porcentagem = "%.2f" % porc[i]
        espaço_inicio = (5 - len(porcentagem)) * ' '
        linha += espaço_inicio + porcentagem + "%"

        relatorio.writelines(linha + '\n')

    relatorio.write('\n')
    relatorio.write('Espaço total ocupado: %.2f' % espaçoTotal + '\n')
    relatorio.write('Espaço médio ocupado: %.2f' % (espaçoTotal / len(usuarios)) + '\n')
    relatorio.close()


def CalculaEspaçoUtilizado(usuarios):
    for i in range(len(usuarios)):
        usuarios[i][1] = float(usuarios[i][1]) / (1024 ** 2)


def CalculaPorcentagem(usuarios, espaçoTotal):
    porc = []
    for usuario in usuarios:
        porc.append(100 * usuario[1] / espaçoTotal)

    return porc


def EspaçosASeremColocados(usuarios):
    maior_string = 0
    for usuario in usuarios:
        if len("%.2f" % usuario[1]) > maior_string:
            maior_string = len("%.2f" % usuario[1])

    return maior_string


main()
