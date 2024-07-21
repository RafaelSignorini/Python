dados = []
pessoas = []
maior = menor = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior = meior = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    resp = str(input('Continuar? [s/n]: ')).strip().lower()[0]
    if resp not in 's':
        break
print('-=-' * 20)
print(f'Os dados registrados são: {pessoas}')
print(f'Você registrou {len(pessoas)} pessoas.')
print(f'O maior peso registrado foi de {maior}kg.')
print('As pessoas com pesos altos foram', end='')
for p in pessoas:
    if p[1] > 85:
        print(f'{p[0]}', end=', ')
print(f'O menor peso registrado foi de {menor}kg.')
print('As pessoas com pesos baixos foram', end='')
for p in pessoas:
    if p[1] < 55:
        print(f'{p[0]}', end=', ')
