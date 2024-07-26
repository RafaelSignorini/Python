from random import randint
jogadores = {}
jogadores['jogador1'] = randint(1, 10)
primeiro = jogadores['jogador1']
jogadores['jogador2'] = randint(1, 10)
if jogadores['jogador2'] > primeiro:
    primeiro = jogadores['jogador2']
    segundo = jogadores['jogador1']
else:
    segundo = jogadores['jogador2']
jogadores['jogador3'] = randint(1, 10)
if jogadores['jogador3'] > primeiro:
    terceiro = segundo
    segundo = primeiro
    primeiro = jogadores['jogador3']
elif jogadores['jogador3'] > segundo:
    terceiro = segundo
    segundo = jogadores['jogador3']
else:
    terceiro = jogadores['jogador3']
jogadores['jogador4'] = randint(1, 10)
if jogadores['jogador4'] > primeiro:
    quarto = terceiro
    terceiro = segundo
    segundo = primeiro
    primeiro = jogadores['jogador4']
elif jogadores['jogador4'] > segundo:
    quarto = terceiro
    terceiro = segundo
    segundo = jogadores['jogador4']
elif jogadores['jogador4'] > terceiro:
    quarto = terceiro
    terceiro = jogadores['jogador4']
else:
    quarto = jogadores['jogador4']
for j in jogadores.items():
    print(f'O {jogadores[j]} tirou {jogadores[j]}')