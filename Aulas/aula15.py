# Interrompendo laços de repetição while

# while True:
#   if {condicao1} == True:
#       acao
#   elif {condicao1} != True and {condicao2} == True:
#       acao2
#   else:
#       acao3
#       break;                      essa quebra faz com que a condição do laço de
#                                   repetição se quebre, assim parando o laço
# acao

# Prática:
cont = 0
while True:
    if cont <= 10:
        print(cont,'-> ', end='')
        cont += 1
    else:
        break
print('fim')

num = -1
soma = 0
while True:
    if num != 0:
        num = int(input('Insira um número: '))
        soma += num
    else:
        break
print('A soma de todos os números inseridos é {}.'.format(soma))

# extras:
# atualização do Python, fstrings
# a partir do python 3.65

nome = 'rafael'
idade = 17
print(f'Olá, {nome}, você tem {idade} anos.')
