num = soma = 0
while True:
    num = int(input('Insira um valor: '))
    if num != 999:
        soma += num
    else:
        break
print(f'A soma dos valores inseridos é {soma}.')
