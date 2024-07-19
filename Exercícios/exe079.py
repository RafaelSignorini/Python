valores = []
while True:
    num = int(input('Insira um número novo na lista: '))
    if num in valores:
        print(f'{num} já está na lista, números repetidos não são adicionados. ')
        continue
    else:
        valores.append(num)
    resp = str(input('Continuar? [s/n] ')).strip().lower()[0]
    if resp in 'sn' and resp == 'n':
            break
    if resp not in 'sn':
        print('Resposta inserida inválida, tente novamente.')
        continue
print(f'Os valores registrados são: {valores.sort()}.')
