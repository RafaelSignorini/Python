soma = 0
for a in range(1, 501):
    if a % 3 == 0:
        print(a, ', ', end='')
        soma += a
print('\nA soma de todos estes valores é {}{}{}.'.format('\033[4;36m', soma, '\033[m'))
print('fim')
