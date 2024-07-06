nota1 = float(input('Insira sua primeira nota: '))
nota2 = float(input('Insira sua segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5:
    print('Você está reprovado com a média de {:.1f} pontos.'.format(media))
elif media >= 5 and media < 7:
    print('Você está de recuperação com a média de {:.1f} pontos.'.format(media))
elif media >= 7:
    print('Você está aprovado com a média de {:.1f} pontos.'.format(media))
else:
    print('Erro, tente novamente.')
