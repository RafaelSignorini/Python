# Condicionais

# Exemplo:
tempo = int(input('Quantos anos seu carro tem? '))
if tempo >= 3:                                                          # verifica se a condição é verdadeira ou falsa
    print('Seu carro é velho. ')                                        # execução caso seja verdadeira
else:
    print('Seu carro é novo. ')                                         # execução caso contrário
print('Fim')

# AVISO: Identação é crucial

# Condições simplificadas (não recomendado)
tempo = int(input('Quantos anos seu carro tem? '))
print('Seu carro é novo' if tempo <= 3 else 'Seu carro é velho')        # simplifica em quantidade de linhas, porém dificulta a leitura e interpretação do código
print('Fim')

# Prática:
nome = str(input('Qual é o seu nome? '))
if nome == 'Rafael':
    print('Seu nome é um nome bíblico, sabia {}?'.format(nome))
print('Bom dia, {}.'.format(nome))

nota1 = float(input('Qual foi a sua primeira nota? '))
nota2 = float(input('Qual foi a sua segunda nota? '))
media = (nota1 + nota2) / 2
print('A média das suas notas foi de {:.1f} pontos.'.format(media))
if media >= 6:
    print('Sua média foi boa, muito bem.')
else:
    print('Sua nota não foi tão boa, mas não desista, minha criança.')
