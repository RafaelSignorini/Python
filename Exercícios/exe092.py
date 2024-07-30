from datetime import datetime
dados = {}
dados['nome'] = str(input('Nome: ')).strip().capitalize()
nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 caso não tenha): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print('-=-' * 20)
for k, v in dados.items():
    print(f' - {k} = {v}')
