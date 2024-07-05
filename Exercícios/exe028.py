from random import randint
from time import sleep
computador = randint(0, 5)
print('-=-' * 20)
print('Olá, eu sou o computador, meu programa me faz pensar em um número de 0 a 5, tente adivinhar qual é.')
print('-=-' * 20)
jogador = int(input('Por favor, adivinhe o número que pensei: '))
print('Processando...')
sleep(3)
if jogador == computador:
    print('Parabéns, você acertou.')
else:
    print('Sinto muito, o número que pensei era {}.'.format(computador))
