# Dicionários

# dados = {}
# dados = {'nome':"Rafael",'idade':17}                  cria chaves 'nome' e 'idade' e registra os valores definidos
# dados['sexo'] = 'M'                                   cria um único chaves e adiciona seu valor registrado

# del dados['idade']                                    deleta o chaves e seu valor registrado

# filme = {
#      'titulo':"Star Wars",
#      'ano':1977,
#      'diretor':"George Lucas"
# }

# print(filme.values()) == "Star Wars", 1977, "George Lucas"
# print(filme.keys()) == 'titulo', 'ano', 'diretor'
# print(filme.items()) == 'titulo':"Star Wars", 'ano':1977, 'diretor':"George Lucas"

# values são os valores inseridos nas chaves
# keys são as chaves criadas como índex dos valores a serem armazenados no dicionário
# items são ambos os valores e as chaves

# for k, v in filme.items():
#   print(f'O {k} é {v}')                               1ª repetição: O título é Star Wars
#                                                       2ª repetição: O ano é 1977
#                                                       3ª repetição: O diretor é George Lucas

# mistura de dicionários e listas:

filme1 = {
    'titulo':"Star Wars",
    'ano':1977,
    'diretor':"George Lucas"
}
filme2 = {
    'titulo':"Vingadores",
    'ano':2012,
    'diretor':"Joss Whedon"
}
filme3 = {
    'titulo':"Matrix",
    'ano':1999,
    'diretor':"Irmãs Machowski"
}
locadora = [filme1, filme2, filme3]

# Prática:
pessoa = {'nome':"Rafael", 'idade':17, 'sexo':"M", 'peso':55.5}
print(pessoa['nome'])
print(pessoa['idade'])
print(pessoa['sexo'])
print(pessoa['peso'])
print(f'{pessoa["nome"]} tem {pessoa["idade"]} anos, é do sexo {pessoa["sexo"]} e pesa {pessoa["peso"]} quilos.')

for k, v in pessoa.items():
    print(f'{k} = {v}')

print(pessoa)
pessoa['nome'] = "Raul"
pessoa['idade'] = 18
pessoa['peso'] = 75.5
print(pessoa)

brasil = []
estado1 = {'nome':"São Paulo", 'sigla':"SP"}
estado2 = {'nome':"Rio de Janeiro", 'sigla':"RJ"}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[0]['nome'], end=', ')
print(brasil[0]['sigla'])
print(brasil[1]['nome'], end=', ')
print(brasil[1]['sigla'])

brasil.clear()

estado = {}
brasil = []
for a in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla: '))
    brasil.append(estado.copy())
print(brasil)
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')
