soma = 0
cont = 0
for a in range(1, 501):
    if a % 3 == 0:
        print(a, ', ', end='')
        soma += a
        cont += 1
print('\nA soma de todos os {}{}{} valores é {}{}{}.'.format('\033[7;35m', cont, '\033[m', '\033[4;36m', soma, '\033[m'))
print('fim')
