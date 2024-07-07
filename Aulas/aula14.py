# Laço de repetição while (amo)
# laço preferível pois não se limita a situações aonde é necessário saber um fim específico da condição da repetição

# enquanto {condição} == True:
#   acao
# acao2

# while True:
#   acao
# acao2

# código de repetição com condições:

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

c = 0
while c < 10:
    print(c)
    c += 1
print('fim')

# condição semi-infinita:

n = -1
while n != 0:
    n = int(input('Insira um valor: '))
print('fim')

# contador de pares:
num = -1
par = impar = 0
while num != 0:
    num = int(input('Insira um número: '))
    if num % 2 == 0 and num != 0:
        par += 1
    else:
        impar += 1
print('O total de números pares registrados foi {} enquanto de ímpares foi {}.'.format(par, impar))
