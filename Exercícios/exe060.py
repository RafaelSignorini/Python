# Primeiro modo
from math import factorial
num = int(input('Insira um valor para saber sua fatorial: '))
fac = factorial(num)
print('O fatorial de {} é {}.'.format(num, fac))

# Segundo modo
numero = int(input('Insira um número para saber sua fatorial: '))
cont = numero
f = 1
print('O valor de {}! = '.format(numero), end='')
while cont > 0:
    print('{} '.format(cont), end='')
    if cont > 1:
        print('x ', end='')
    else:
        print('= ', end='')
    f *= cont
    cont -= 1
print(f)
print('O fatorial de {} é {}.'.format(numero, f))
