num = list()
pares = list()
impares = list()
for a in range(0, 7):
    num.append(int(input('Insira um número: ')))
for a, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print('-=-' * 30)
print(f'A lista completa é: {num}.')
print(f'A lista de números pares é {pares}.')
print(f'A lista de números ímpares é {impares}.')
