def potencia(base, exp):
    pot = base ** exp
    return pot

a = potencia (5, 6)
print(a)


def soma(n1, n2, n3):
    return n1+n2+n3


print(soma(10, 33, 15))


def OpMat(n1, n2):
    soma = n1 + n2
    return soma, n1 * n2

a, b = OpMat(2, 3)
print(a)
print(b)


from random import randint

def dado():
    num = randint(1,6)
    print(num)


dado()
