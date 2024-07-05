# Primeiro modo (mais específico, recomendado)
velocidade = float(input('Qual era a velocidade que você estava enquanto dirigia? '))
if velocidade <= 80:
    print('Sem problemas, tenha um bom dia.')
else:
    multa = (velocidade - 80) * 7
    print('Você estava a {}km/h, você terá que pagar uma multa de {:.2f} reais.'.format(velocidade, multa))

# Segundo modo (mais simples)
velocidade = float(input('Qual era a velocidade que você estava enquanto dirigia? '))
if velocidade > 80:
    print('Você estava a {}km/h, você terá que pagar uma multa de {:.2f} reais.'.format(velocidade, multa))
print('Tenha um bom dia.')
