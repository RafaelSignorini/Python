num = soma = cont = 0
while num != 999:
    num = int(input('Insira um valor para [num], insira o valor "999" para parar o programa: '))
    if num != 999:
        soma += num
        cont += 1
print('Você digitou {} números e a soma deles é {}.'.format(cont, soma))
