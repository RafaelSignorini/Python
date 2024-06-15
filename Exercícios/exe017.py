import math
co = float(input('Insira o comprimento do cateto oposto: '))
ca = float(input('Insira o comprimento do cateto adjacente: '))
hi = math.hypot(co, ca)
print('O cateto oposto medindo {}, e o cateto adjacente medindo {} geram uma hipotenusa medindo {}.'.format(co, ca, hi))
