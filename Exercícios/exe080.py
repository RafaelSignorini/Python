valores = []
for a in range(0, 5):
    num = int(input('Insira um valor: '))
    if a == 0 and num > valores[-1]:
        valores.append(num)
    else:
        pos = 0
        while pos < len(valores):
            if num <= valores[pos]:
                valores.insert(pos, num)
                break
            pos += 1
print('-=-' * 30)
print(f'Os valores, em ordem crescente, são {valores}.')
# eu poderia ter usado o .sort(), mas era o desafio não usar
