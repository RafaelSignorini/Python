maior = 0
menor = 0
for a in range(1, 6):
    peso = float(input('Insira o peso da pessoa: '))
    if maior == 0 and menor == 0:
        maior = peso
        menor = peso
    elif peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print('O maior peso registrado foi {:.1f}kg e o menor peso registrado foi {:.1f}kg.'.format(maior, menor))
