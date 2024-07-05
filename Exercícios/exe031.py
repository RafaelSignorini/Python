distancia = float(input('Insira a distância de sua viagem: '))
if distancia > 200:
    print('O preço da viagem será de {:.2f} reais.'.format(distancia * 0.45))
else:
    print('O preço da viagem será de {:.2f} reais.'.format(distancia * 0.5))
