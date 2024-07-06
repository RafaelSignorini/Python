num = int(input('Insira um número inteiro: '))
conversor = int(input('Escolha para que formato converter o valor inserido: \n[ 1 ] Binário \n[ 2 ] Octal \n[ 3 ] Hexadecimal '))
if conversor == 1:
    print('{} convertido para binário é igual a {}.'.format(num, bin(num)[2:]))
elif conversor == 2:
    print('{} convertido para octal é igual a {}.'.format(num, oct(num)[2:]))
elif conversor == 3:
    print('{} convertido para hexadecimal é igual a {}.'.format(num, hex(num)[2:]))
else:
    print('Erro')
