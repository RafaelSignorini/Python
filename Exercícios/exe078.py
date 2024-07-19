valores = []
posicaoMaior = posicaoMenor = 0
for a in range(0, 5):
    valores.append(int(input('Insira um valor na lista: ')))
    if a == 0:
        maior = valores[0]
        menor = valores[0]
    elif a > 0 and valores[-1] > maior:
        maior = valores[-1]
        posicaoMaior = a
    elif a > 0 and valores[-1] < menor:
        menor = valores[-1]
        posicaoMenor = a
print(f'Os valores registrados na lista foram: {valores}')
print(f'O maior valor registrado foi {maior} e está na posição {posicaoMaior + 1}.')
print(f'O menor valor registrado foi {menor} e está na posição {posicaoMenor + 1}.')
