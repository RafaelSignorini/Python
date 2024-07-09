print('-=-' * 20)
print('Gerador de PA 2.0')
print('-=-' * 20)
primeiro = int(input('Primeiro termo da PA: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    cont += 1
print('fim')
