time = []
jogador = {}
partidas = []

while True:
    jogador.clear()    
    jogador['nome'] = str(input('Nome do Jogador: ')).strip().capitalize()
    total = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for a in range(0, total):
        partidas.append(int(input(f'   Quantos gols foram feitos na {a+1}ª partida? ')))
    jogador['gols de cada partida'] = partidas[:]
    jogador['total de gols'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Continuar? [S/N]: ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Utilize apenas sim (S) ou não (N).')
    if resp == 'N':
        break
print('-=-' * 10)
print('cod ',end='')
for i in jogador.keys():
    print(f'{i:<15}',end='')
print('-=-' * 10)
for k, v in enumerate(time):
    print(f'{k:>4}',end='')
    for d in v.values():
        print(f'{str(d):<15}',end='')
    print()
print('-=-' * 10)
while True:
    busca = int(input('Mostrar dados de qual jogador? (0 para parar): '))
    if busca == 0:
        break
    if busca > len(time):
        print(f'ERRO! Não existe jogador com código {busca}.')
    else:
        print(f' == Levantamento do jogador {time[busca+1]["nome"]}:')
        for i, g in enumerate(time[busca+1]['gols']):
            print(f'    No jogo {i+1} fez {g} gols')
    print('-=-' * 10)
print('O programa foi terminado.')
