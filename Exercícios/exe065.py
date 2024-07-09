num = -1
quantidade = soma = 0
while num != 0:
    num = int(input('Insira um número para o programa somar: '))
    if num != 0:
        soma += num
        quantidade += 1
print('O programa registrou {} números, cuja soma vale {} e a média é igual a {}.'.format(quantidade, soma, soma / quantidade))
