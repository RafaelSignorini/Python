from random import randint
from time import sleep
lista = []
jogos = []
print('-=-' * 10)
print(f'{"MEGA SENA":^30}')
print('-=-' * 10)
quantidade = int(input('Quantos jogos você quer que eu sorteie? '))
total = 1
while total <= quantidade:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
print('-=-' * 2, f'Sorteando {quantidade} jogos...', '-=-' * 2)
for i, l in enumerate(jogos):
    sleep(1)
    print(f'Jogo {i+1}: {l}')
print('-=-' * 2, ' < Boa sorte > ', '-=-' * 2)
