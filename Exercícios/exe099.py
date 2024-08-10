from random import randint
from time import sleep
def func():
    maior = 0
    quant = randint(1, 6)
    for a in range(0, quant):
        num = randint(0, 9)
        if num > maior:
            maior = num
        print(num,end=' ')
    print(f'\nO maior valor gerado foi {maior}.')


vezes = randint(0, 3)
cont = 0
while True:
    if cont >= vezes:
        break
    func()
    cont += 1
