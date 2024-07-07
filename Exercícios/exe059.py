operacao = -1
while operacao != 0:
    num1 = float(input('Insira o primeiro valor da equação: '))
    num2 = float(input('Insira o segundo valor da equação: '))
    print('[ 1 ] Soma ')
    print('[ 2 ] Substração ')
    print('[ 3 ] Multiplicação ')
    print('[ 4 ] Divisão ')
    print('[ 0 ] Sair ')
    operacao = int(input('Insira qual das operações acima deseja realizar: '))
    if operacao == 1:
        print('{} + {} = {}'.format(num1, num2, num1 + num2))
    elif operacao == 2:
        print('{} - {} = {}'.format(num1, num2, num1 - num2))
    elif operacao == 3:
        print('{} x {} = {}'.format(num1, num2, num1 * num2))
    elif operacao == 4:
        print('{} / {} = {}'.format(num1, num2, num1 / num2))
    elif operacao == 0:
        break
    else:
        print('Operação inválida, tente novamente.')
print('O programa foi terminado.')
