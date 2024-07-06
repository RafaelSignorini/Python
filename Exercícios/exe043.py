peso = float(input('Insira o seu peso (Kg): '))
altura = float(input('Insira a sua altura (m): '))
imc = peso / (altura ** 2)
print('Seu IMC é de {:.1f}, '.format(imc), end='')
if imc < 18.5:
    print('você está abaixo do peso.')
elif imc >= 18.5 and imc < 25:
    print('você está com o peso ideal.')
elif imc >= 25 and imc < 30:
    print('você está com sobrepeso.')
elif imc >= 30 and imc < 40:
    print('você está com obesidade.')
else:
    print('você está com obesidade mórbida.')
