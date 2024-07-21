lista = []
for a in range(0, 9):
    num = int(input('Insira um valor: '))
    lista.append(num)
lista.sort(reverse = True)
print(f'A lista contém {len(lista)} números.')
print(f'Os números registrados na lista são: {lista}.')
if 5 in lista:
    print('O número 5 está na lista.')
else:
    print('O número 5 não está na lista.')
