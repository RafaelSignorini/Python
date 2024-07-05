a = int(input('Insira um valor inteiro: '))
maior = a
menor = a
b = int(input('Insira mais um valor, por favor: '))
if b > maior:
    maior = b
if b < menor:
    menor = b
c = int(input('Insira o terceiro e último valor: '))
if c > maior:
    maior = c
if c < menor:
    menor = c
print('Dos valores providenciados, o maior é {} e o menor é {}.'.format(maior, menor))
