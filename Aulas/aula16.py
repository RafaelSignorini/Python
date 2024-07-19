# Tuplas

# lanche = ('hamburguer', 'suco', 'pizza', 'pudim')     declarando os itens da tupla, sendo ela uma 
#                                                       variável composta imutável, seus elementos 
#                                                       serão permanentemente os mesmos

# criar uma tupla e tentar altera-lá em código não funciona:

# lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
# lanche = str(input('Insira mais um elemento à tupla: '))

# o código acima resulta em erro, pois tuplas não recebem valores externos ou adicionais após serem criadas

# escrever elementos de uma tupla:

# print(lanche[0])          hamburguer
# print(lanche[1])          suco
# print(lanche[2])          pizza
# print(lanche[3])          pudim

# print(lanche[0:2])        (hamburguer, suco, pizza)
# print(lanche[1:])         (suco, pizza, pudim)
# print(lanche[-1])         pudim

# print(len(lanche))        4
# for a in lanche:
#   print(a)                hamburguer
#                           suco
#                           pizza
#                           pudim

# Prática:

lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
print(lanche)
print(lanche[1])
print(lanche[3])
print(lanche[-2])
print(lanche[1:3])
print(lanche[:2])
for comida in lanche:
    print(f'Eu vou comer {comida} agora')
print('Comi tanto que virei o próximo matheus yan')

lanche = ('hamburguer', 'suco', 'pizza', 'pudim', 'batata frita')
for cont in range(0, len(lanche)):
    print(cont, lanche[cont])

print(sorted(lanche)) #             escreve os elementos da tupla em ordem alfabética

# extras:

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)
print(c.count(5))
print(c.index(8))

pessoa = ('Rafael', 17, 'homem', 54.5)
print(pessoa)
