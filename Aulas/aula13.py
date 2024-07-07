# Laço de repetição 'for' (odeio)

# laço c no intervalo(1, 10)        'intervalo' define os parâmetros de
#                                   repetição do código

#   ação                            essa ação vai ser repetida de acordo
#                                   com os parâmetros do intervalo

# ação2                             essa ação não está dentro do laço de
#                                   repetição [for], portanto não é repetida

# código de repetição:

# for c in range(1, 10):
#   acao
# acao2

# código de repetição com 3 ações:

# for c in range(1, 10):
#   acao
#   acao2
# acao                              por haver uma quebra de padrão, por mais
# acao3                             que a primeira ação seja colocada dentro
#                                   do laço de repetição, ela ainda é
#                                   relizada, porém como excessão dos
#                                   parâmetros do laço nas linhas seguintes

# código de repetição com 3 ações e condição interna:

# for c in range(1, 10):
#   if {condição} == True:          a primeira ação do laço de repetição é
#       acao3                       verificada por uma condição, dessa forma
#   acao                            o código executa caso for verdadeira,
#   acao2                           se não segue com o reso do código
# acao
# acao3

# Prática:

for c in range(0, 6):
    print('Oi', c) #                escreve 'Oi' e o número da repetição
print('FIM')

# repetição invertida (regressiva):
for i in range(0, 6, -1): #         escreve o valor [i] de forma regressiva,
    print(i) #                      ou descrescente
print('FIM')

for m in range(0, 7, 2): #          define que apenas escreverá um a cada dois
    print(m) #                      valores a partir do primeiro
print('FIM')

# código interativo:

num = int(input('Insira um valor para o laço de repetição utilizar como parâmetro: '))
for n in range(0, num + 1):
    print(n)
print('FIM')

i = int(input('Insira o valor inicial para o laço de repetição: '))
f = int(input('Insira o valor final para o laço de repetição: '))
p = int(input('Insira o passo que deve ser feito pelo laço de repetição: '))
for a in range(i, f + 1, p):
    print(a)
print('FIM')

soma = 0
for s in range(0, 3):
    d = int(input('Insira um número inteiro: '))
    soma += d
print('A soma dos valores é {}.'.format(soma))
print('FIM')


