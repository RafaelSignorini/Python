total = mil = cont = menor = 0
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    cont += 1
    if cont == 1 or preco < menor:
        menor = preco
    total += preco
    if preco >= 1000:
        mil += 1
    resposta = ' '
    while resposta not in 'sn':
        resposta = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
    if resposta == 'n':
        break
print(f'O preço total da compra foi de {total:.2f} reais.')
print(f'{mil} produtos custaram mais do que R$1000,00.')
print('fim')
