# funções
def linha():
    print('-=-' * 15)


linha()
print(f'{"Sistema de alunos":^45}')
linha()
linha()
print(f'{"Cadastro de funcionários":^45}')
linha()
linha()
print(f'{"Erro no sistema":^45}')
linha()

def mensagem(msg):
    print('-=-' * 15)
    print(msg)
    print('-=-' * 15)


mensagem('Sistema de alunos')
mensagem('Cadastro de funcionários')
mensagem('Erro no sistema')

# Prática:
a = 4
b = 5
c = a + b
print(c)

a = 8
b = 9
c = a + b
print(c)

a = 2
b = 1
c = a + b
print(c)

def soma(a, b):
    c = a + b
    print(c)


soma(4, 5)
soma(8, 9)
soma(2, 1)

def soma2(a, b):
    print(f'A = {a} e B = {b}')
    c = a + b
    print(f'A soma de A + B = {c}')


soma2(a=7, b=5)
soma2(b=7, a=5)
soma2(a=9, b=2)
soma2(b=9, a=2)

def contador(*num):
    for n in num:
        print(f'{n}',end=', ')
    print('fim')
    print(f'Os valores registrados foram: {num}, ao todo são {len(num)} números.')


contador(5, 7, 3, 1, 4)
contador(8, 4, 7)
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [7, 2, 5, 0, 4]
print(valores)
dobra(valores)
print(valores)

def soma3(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


soma3(5, 2)
soma3(2, 9, 4)

