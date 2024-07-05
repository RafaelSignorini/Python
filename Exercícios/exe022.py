nome = str(input('Insira seu nome: ')).strip()
print('Seu nome em maiúsculas é {} e em minúsculas é {}.'.format(nome.upper(), nome.lower()))
print('Há {} letras no seu nome.'.format(len(nome) - nome.count(' ')))

# Primeiro modo de mostrar o primeiro nome:
print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))

# Segundo modo de mostrar o primeiro nome:
separa = nome.split()
print('Seu primeiro nome tem {} letras.'.format(len(separa[0])))
