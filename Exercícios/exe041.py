idade = int(input('Insira a sua idade: \n'))
if idade > 0 and idade <= 9:
    print('Você estará na categoria Mirim.')
elif idade > 9 and idade <= 14:
    print('Você estará na categoria Infantil.')
elif idade > 14 and idade <= 19:
    print('Você estará na categoria Junior.')
elif idade > 19 and idade <= 24:
    print('Você estará na categoria Senior.')
elif idade > 24:
    print('Você estará na categoria Mestre.')
else:
    print('Algo de errado não está certo, tente novamente;')
