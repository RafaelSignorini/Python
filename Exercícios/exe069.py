maiores = totalHomens = totalMulheres20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'fm':
        sexo = str(input('Sexo [M/F]: ')).strip().lower()[0]
    if idade >= 18:
        maiores += 1
    if sexo == 'm':
        totalHomens += 1
    if sexo == 'f' and idade < 20:
        totalMulheres20 += 1
    resposta = ' '
    while resposta not in 'sn':
        resposta = str(input('Continuar? [S/N]: ')).strip().lower()[0]
    if resposta == 'n':
        break
print(f'Temos, ao todo, {maiores} maiores de idade, ', end='')
print(f'{totalHomens} homens no total, ', end='')
print(f'e {totalMulheres20} mulheres com menos de 20 anos.')
print('fim')
