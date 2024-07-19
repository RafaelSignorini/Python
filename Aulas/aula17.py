# Listas

# listas são tuplas MUTÁVEIS

# lanche = ['hamburguer', 'suco', 'pizza', 'pudim']                 declarando os itens da lista, sendo ela uma 
#                                                                   variável composta mutável, seus elementos 
#                                                                   são alteráveis durante o processo do código, 
#                                                                   ao contrário de tuplas

# lanche[3] = 'picolé'
# lanche == ['hamburguer', 'suco', 'pizza', 'picolé']               o quarto valor da variável composta 'lanche'
#                                                                   foi alterada de 'pudim' para 'picolé'

# lanche.append('bolacha')                                          adiciona valores na lista (sim, é bolacha, 
#                                                                   não biscoito)

# lanche.insert(0, 'cachorro quente')                               adiciona um valor na primeira posição, 
#                                                                   "empurando" os outros valores para as 
#                                                                   casas sucessoras

# del lanche[3]                                                     deleta o elemento na casa no parâmetro 
#                                                                   determinado 
# lenche.pop(3)                                                     geralmente utilizada apenas para deletar o 
#                                                                   último valor da lista, porém especificar 
#                                                                   um elemento também funciona

# lanche.remove('pizza')                                            deleta o elemento com o mesmo valor escrito 
#                                                                   dentro dos parâmetros, reposicionando os 
#                                                                   elementos sucessores

# if 'pizza' in lanche:
#   lanche.remove('pizza')

# valores = list(range(4, 11))                                      cria uma variável chamada "valores", 
#                                                                   determina que é uma lista e define o início 
#                                                                   no elemento 4 e seu último elemento como o 
#                                                                   antecessor de 11

# valores = [8, 2, 5, 4, 9, 3, 0]
# valores.sort()                                                    organiza os valores em ordem crescente
# valores == [0, 2, 3, 4, 5, 8, 9]
# valores.sort(reverse=True)                                        organiza os valores em ordem decrescente
# valores == [9, 8, 5, 4, 3, 2, 0]
# len(valores) == 7

# Prática:
num = [2, 5, 9, 1]
print(num)
num[2] = 3
print(num)
num.append(7)
print(num)
num.sort()
print(num)
num.sort(reverse=True)
print(num)
num.insert(2, 0)
print(num)
num.pop()
print(num)
num.pop(2)
print(num)
num.remove(2)
if 4 in num:
    num.remove(4)
else:
    print('Não há o número 4 na lista.')
print(num)
print(f'Essa lista tem {len(num)} elementos.')

valores = []
valores.append(5)
valores.append(9)
valores.append(4)
for c, v in enumerate(valores):
    print(f'O valor {v} está na posição {c}.')

values = list()
for cont in range(0, 5):
    values.append(int(input('Insira um valor na lista: ')))
print(f'Os valores asseguir foram digitados na lista: {values}.')

# Ligação entre listas (cuidado):

a = [2, 3, 4, 7]
b = a #                     dessa forma, se cria uma ligação entre as listas, 
#                           dessa forma, qualquer alteração feita em qualquer 
#                           uma das listas, afeta todas as listas ligadas
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
a = [2, 3, 4, 7]
b = a[:] #                  enquanto dessa forma, a lista {b} apenas recebe os 
#                           mesmos valores da lista {a}, não criando uma 
#                           ligação entre elas, evitando conflitos
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
