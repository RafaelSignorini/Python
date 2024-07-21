cont = (
    'zero', 'um', 'dois', 'três', 'quatro', 
    'cinco', 'seis', 'sete', 'oito', 'nove', 
    'dez', 'onze', 'doze', 'treze', 'quatorze', 
    'quinze', 'dezesseis', 'dezessete', 'dezoito', 
    'dezenove', 'vinte'
)
while True:
    num = int(input('Insira um número entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Erro, tente novamente.', end='')
print(f'Você digitou o número {cont[num]}')
