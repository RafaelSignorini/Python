num1 = int(input('Insira um número inteiro: '))
num2 = int(input('Insira mais um número inteiro: '))
if num1 > num2:
    print('O maior número é {}{}{}.'.format('\033[36m', num1, '\033[m'))
elif num1 < num2:
    print('O maior número é {}{}{}.'.format('\033[34m', num2, '\033[m'))
else:
    print('Ambos {}{}{} e {}{}{} têm o mesmo valor, não há número maior.'.format('\033[35m', num1, '\033[m', '\033[32m', num2, '\033[m'))
