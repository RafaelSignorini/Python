soma = 0
for a in range(0, 6):
    num = int(input('Insira um valor: '))
    if num % 2 == 0:
        soma += num
print('A soma de todos os números pares inseridos é {}{}{}.'.format('\033[1;34m', soma, '\033[m'))
print('fim')
