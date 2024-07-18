from random import randint
num = vit = escolha = soma = 0
while True:
    pc = randint(0, 10)
    escolha = int(input('Escolha entre par ou ímpar \n[ 0 ] Par \n[ 1 ] Ímpar\n'))
    if escolha < 0 or escolha > 1:
        print('Número inserido inválido, tente novamente.', end='')
        continue
    num = int(input('Insira um número entre 0 e 10: '))
    if num < 0 or num > 10:
        print('Número inserido inválido, tente novamente.', end='')
        continue
    elif num % 2 != escolha:
        print('Número inserido inválido, tente novamente.', end='')
    else:
        soma = num + pc
        if (escolha == 0 and soma % 2 == 0) or (escolha == 1 and soma % 2 != 0):
            print(f'Você venceu! A soma resultou em {soma}.')
            print(f'PC: {pc} \nUsuário: {num}')
            vit += 1
            continue
        else:
            print(f'Você perdeu. A soma resultou em {soma}.')
            print(f'PC: {pc} \nUsuário: {num}')
            print(f'Você terminou com {vit} vitórias.')
            break
print('O programa foi terminado.')
