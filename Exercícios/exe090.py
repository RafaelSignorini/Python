info = {}
info['nome'] = str(input('Nome: ')).strip().capitalize()
info['media'] = float(input('Media: '))
if info['media'] < 0 or info['media']> 10:
    print(f'Erro. O valor {info["media"]} não é válido, tente novamente. ')
elif info['media'] >= 7:
    info['situacao'] = 'aprovado'
else:
    info['situacao'] = 'reprovado'
print(f'A média de {info["nome"]} é {info["media"]} e a situação é {info["situacao"]}.')
