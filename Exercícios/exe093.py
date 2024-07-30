jogador = {}
partidas = []
jogador['nome'] = str(input('Nome do Jogador: ')).strip().capitalize()
total = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for a in range(0, total):
    partidas.append(int(input(f'Quantos gols foram feitos na {a+1}ª partida? ')))
jogador['gols de cada partida'] = partidas[:]
jogador['total de gols'] = sum(partidas)
print('-=-' * 10)
print(jogador)
print('-=-' * 10)
for k, v in jogador.items():
    print(f'{k} = {v}')
print('-=-' * 10)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols de cada partida"])} partidas.')
for i, v in enumerate(partidas):
    print(f'Na {i+1}ª partida fez {v} gols.')
print(f'Foi um total de {jogador["total de gols"]} gols em todas as partidas.')
