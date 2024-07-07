sexo = ''
while sexo.lower() != 'm' and sexo.lower() != 'f':
    sexo = str(input('Insira seu sexo [M/F]: ')).lower()
print('Seu sexo foi registrado como \033[4;32m{}\033[m.'.format(sexo.upper()))
