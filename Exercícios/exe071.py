valor = int(input('Insira o valor que quer sacar: '))
total = valor
cinquenta = 0
vinte = 0
dez = 0
um = 0
cont = 0
while True:
    if total > 0 and total >= 50:
        while total >= 50:
            total -= 50
            cinquenta += 1
    print(f'Um total de {cinquenta} cédulas de 50 reais foram sacadas. ')

    if total > 0 and total >= 20:
        while total >= 20:
            total -= 20
            vinte += 1
    print(f'Um total de {vinte} cédulas de 20 reais foram sacadas. ')

    if total > 0 and total >= 10:
        while total >= 10:
            total -= 10
            dez += 1
    print(f'Um total de {dez} cédulas de 10 reais foram sacadas. ')

    if total > 0 and total >= 1:
        while total >= 1:
            total -= 1
            um += 1
    print(f'Um total de {um} cédulas de 1 reais foram sacadas. ')
    break
print('Você terminou o programa. ')
