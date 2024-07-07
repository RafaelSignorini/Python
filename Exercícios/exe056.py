somaIdade = 0
mediaIdade = 0
maiorIdadeHomem = 0
maisVelho = ''
mulheresVinte = 0
for a in range(1, 5):
    print('-' * 5, '{}ª pessoa'.format(a), '-' * 5)
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().lower()
    somaIdade += idade
    if sexo == 'm' and maiorIdadeHomem == 0 and maisVelho == '':
        maiorIdadeHomem = idade
        maisVelho = nome
    elif sexo == 'f' and idade < 20:
        mulheresVinte += 1
mediaIdade = somaIdade / 4
print('A média de idade do grupo é de {} anos.'.format(mediaIdade))
print('{} é o homem mais velho com {} anos.'.format(maisVelho, maiorIdadeHomem))
print('Um total de {} mulheres tem menos de 20 anos.'.format(mulheresVinte))
