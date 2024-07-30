jogador = {}
partidas = []
jogador['nome'] = str(input('Nome do Jogador: ')).strip().capitalize()
total = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for a in range(0, total):
    partidas.append(int(input(f'Quantos gols foram feitos na {a+1}ª partida? ')))
print(jogador)
print(partidas)
