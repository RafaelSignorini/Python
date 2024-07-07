termo = int(input('Insira um termo: '))
razao = int(input('Insira a razão: '))
decimo = termo + (10 - 1) * razao
for i in range(termo, decimo + razao, razao):
    print('{} '.format(i), end=' -> ')
print('Já deu né tanso')
