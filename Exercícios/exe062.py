print('Gerador de PA')
print('-=-' * 10)

primeiro = int(input('Insira o primeiro termo da PA: '))
razao = int(input('Insira o valor da razão: '))
cont = 1
termo = primeiro
extras = int(input('Insira a quantidade de termos que deseja ver: '))
total = 0
while extras != 0:
    total = total + extras
    while cont <= total:
        print('{} '.format(termo), end='-> ')
        termo += razao
        cont += 1
    print('Pausa ')
    extras = int(input('\nCaso desejar mais termos da mesma progressão, insira a quantidade de termos que gostaria de ver: '))
print('No total {} termos foram gerados. '.format(total), '\nVocê terminou o programa. ')
