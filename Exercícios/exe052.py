num = int(input('Insira um número: '))
total = 0
for i in range(1, num + 1):
    if num % i == 0:
        print('\033[33m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(i), end='')
print('\n\033[mO número {} é divisível {} vezes'.format(num, total))
if total == 2:
    print('Por isso, {} é primo'.format(num))
elif total == 1:
    print('O número 1 é primo')
else:
    print('Por isso, {} não é primo'.format(num))
