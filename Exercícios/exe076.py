'''compras = (str(input('Nome do primeiro produto: ')), float(input('Preço do primeiro produto: ')), 
           str(input('Nome do segundo produto: ')), float(input('Preço do segundo produto: ')), 
           str(input('Nome do terceiro produto: ')), float(input('Preço do terceiro produto: ')), 
           str(input('Nome do quarto produto: ')), float(input('Preço do quarto produto: ')))'''
compras = ('lápis', 1.75, 
           'borracha', 2, 
           'caderno', 15.9, 
           'estojo', 25)
print('-=-' * 15)
print(f'{"Preços":^45}')
print('-=-' * 15)
for a in range(0, len(compras)):
    if a % 2 == 0:
        print(f'{compras[a]:.<30}', end='')
    else:
        print(f'R${compras[a]:>10.2f}')
print('-=-' * 15)
