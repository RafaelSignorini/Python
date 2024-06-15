km = int(input('Insira quantos quilometros foram rodados com esse carro: '))
dias = int(input('Por quantos dias o carro foi alugado? '))
valor = km * 0.15 + dias * 60
print('O valor final do aluguel é de {} reais.'.format(valor))
