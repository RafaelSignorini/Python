from random import randint
pc = randint(0, 10)
num = int(input('O código gerou um número aleatório entre 0 e 10, tente adivinhar: '))
while num != pc:
    num = int(input('Você errou, tente novamente: '))
print('Você acertou, jovem.')
