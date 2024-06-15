n1 = int(input('Insira um número: '))
n2 = int(input('Insira mais um número: '))
s = n1 + n2
print('A soma vale', s)
print('A soma vale {}'.format(s))

# int: números inteiros
# float: números com 8 casas decimais
# bool: recebe True ou False apenas
# str: texto

valor1 = int(input('Insira um valor: '))
valor2 = int(input('Insira outro valor: '))
soma = valor1 + valor2
print('A soma entre ', valor1, 'e', valor2, 'vale', soma)
print('A soma entre {} e {} vale {}'.format(valor1, valor2, soma))