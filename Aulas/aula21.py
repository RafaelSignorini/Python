# funções parte 2

# a função 'help()' mostra todas as funcionalidades de uma função interna do python
# por exemplo: help(print)
# o código acima mostrará todas as funcionalidades de 'print()'

# print(input.__doc__) é outra variação do mesmo código

# docstrings

# def contador(i, f, p):
#    c = i
#    while c <= f:
#        print(f'c',end='..')
#        c += p
#    print('fim')


# contador(2, 10, 2)

def contador(i, f, p):
    """
    -> Faz uma contagem e mostra o processo na tela
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    Função criada por Senhor Ini, também conhecido como FMO Comuna
    """
    c = i
    while c <= f:
        print(f'c',end='..')
        c += p
    print('fim')


help(contador)

# parâmetros opcionais

# def somar(a=0, b=0, c=0):
#     """
#     Faz a soma de 3 valores e apresenta o resultado na tela
#     a ==> primeiro valor
#     b ==> segundo valor
#     c ==> terceiro valor
#     Função criada por fmocomuna
#     """
#     s = a + b + c
#     print(f'A soma vale {s}')
# 
# 
# somar(3, 2, 5)
# help(somar)

# importante: variáveis criadas fora de funções funcionam em todo o código
# enquanto variáveis criadas dentro de funções apenas funcionam nos confinamentos
# das funções, o nome de cada uma, respectivamente, são variável global e 
# variável local

# caso haja uma variável local e outra global com nomes iguais, a função sempre
# vai se basear na variável local, a não ser que a função tenha uma linha  de 
# código contendo 'global {nome da variável}' para definir que a variável a ser
# usada será a variável global, sem criar outra variável local

def teste(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f'"a" dentro da função vale {a}')
    print(f'"b" dentro da função vale {b}')
    print(f'"c" dentro da função vale {c}')


a = 5
teste(a)
print(f'"a" fora da função vale {a}')

# retorno de valores - return

def somar(a=0, b=0, c=0):
    """
    Faz a soma de 3 valores e apresenta o resultado na tela
    a ==> primeiro valor
    b ==> segundo valor
    c ==> terceiro valor
    Função criada por fmocomuna
    """
    s = a + b + c
    return s


r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(6)

print(f'Os resultados das somas são {r1}, {r2} e {r3}')

# Prática:

