galera = []
pessoa = {}
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: ')).strip().capitalize()
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor escreva apenas sexo masculino (M) ou feminino (F).')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Continuar? [S/N]: ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Por favor escreva apenas sim (S) ou não (N).')
    if resp == 'N':
        break
print('-=-' * 10)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'B) A média de idade é {media:5.2f} anos.')
print('C) As pessoas de sexo feminino cadastradas foram',end=', ')
for p in galera:
    if p['sexo'] == 'F':
        print(p['nome'], end='')
print()
print('D) Lista de pessoas que estão acima da média:',end='')
for p in galera:
    if p['idade'] >= media:
        print('     ')
        for k, v in p.items():
            print(f'{k} = {v}',end='')
        print()
print('-=- ENCERRADO -=-')
