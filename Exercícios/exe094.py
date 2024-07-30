galera = []
pessoa = {}
while True:
    pessoa['nome'] = str(input('Nome: ')).strip().capitalize()
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor escreva apenas sexo masculino (M) ou feminino (F).')
    pessoa['idade'] = int(input('Idade: '))

print(pessoa)
# código interminado, tarde demais pra continuar
