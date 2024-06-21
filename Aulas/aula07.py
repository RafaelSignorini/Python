# +                                 adição
# -                                 subtração
# *                                 multiplicação
# /                                 divisão
# **                                potência
# //                                divisão inteira
# %                                 resto da divisão

# Exemplos:

# 5 + 2 == 7                        '=' realiza o recebimento de um valor, 
# 5 - 2 == 3                        independente do tipo da variável
# 5 * 2 == 10                       enquanto '==' compara o valor e 
# 5 / 2 == 2.5                      verifica se é verdadeiro (True) ou 
# 5 ** 2 == 25                      falso (False)

# 5 // 2 == 2                       (mostra por quanto 
#                                   o número pode ser 
#                                   dividido sem 
#                                   resultar em decimal)

# 5 % 2 == 1                        (mostra o resto da
#                                   divisão decimal)

# Ordem de precedência:

# 1. ()
# 2. **
# 3. *, /, //, %
# 4. +, -

# Mais exemplos:

# 5 + 3 * 2 == 11
# 3 * 5 + 4 ** 2 == 31
# 3 * (5 + 4) ** 2 == 243

# 18 % 2 == 0
# 122 % 3 == 2
# 4 ** 3 == 64
# pow(4, 3) == 64   (alternativa)
# 81 ** (1/2) == 9  (alternativa)
# 25 ** (1/2) == 5
# 127 ** (1/3) == 5.026...

# Multiplicando strings:

# 'Oi' * 5 == 'OiOiOiOiOi'          (dentro da função interna print())

nome = input('Qual é o seu nome? ')
print('Olá {}, tudo bem?'.format(nome))
n1 = int(input('Insira um valor: '))
n2 = int(input('Insira outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A equações possíveis são {}, {}, {}, {} e {}'.format(s, m, d, di, e))
