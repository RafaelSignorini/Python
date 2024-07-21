# Listas parte 2

# dados = list()
# dados.append('Rafael')
# dados.append(17)

# pessoas = []
# pessoas.append(dados[:])                                      recebe os dados da lista {dados} sem criar uma 
#                                                               ligação entre as listas, criando assim uma 
#                                                               lista dentro de outra

# pessoas = [['Rafael', 17], ['Raul', 18], ['zarinha', 0]]

# print(pessoas[0][0]) == 'Rafael'
# print(pessoas[1][1]) == 18
# print(pessoas[2][0]) == 'zarinha'
# print(pessoas[1]) == ['Raul', 18]

# Prática:

teste = list()
teste.append('Rafael')
teste.append(17)
galera = list()
galera.append(teste[:])
print(galera)
teste[0] = 'Raul'
teste[1] = 18
galera.append(teste[:])
print(galera)
galera.clear()

pessoas = list(
    ['Rafael', 17], 
    ['Zarinha', 0], 
    ['João', 45], 
    ['Ian', 32]
)
print(pessoas)
print(pessoas[0][0])
print(pessoas[2][1])
for pessoa in pessoas:
    print(f'{pessoa[0]} tem {pessoa[1]} anos de idade.')
pessoas.clear()

maiores = menores = 0
dados = list()
for a in range(0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])
    dados.clear()
print(galera)
for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade.')
        maiores += 1
    else:
        print(f'{p[0]} é menor de idade.')
        menores += 1
galera.clear()
print(f'Neste grupo, há {maiores} maiores de idade enquanto há {menores} menores de idade.')
