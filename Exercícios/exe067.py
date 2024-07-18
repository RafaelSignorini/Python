while True:
    num = int(input('Insira um número para saber sua tabuada: '))
    if num <= 0:
        break
    for a in range (1, 11):
        print(f'{num} x {a} = {num * a}')
print('O programa foi terminado.')
