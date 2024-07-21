num = (
    int(input('Insira o primeiro número: ')), 
    int(input('Insira o segundo número: ')), 
    int(input('Insira o terceiro número: ')), 
    int(input('Insira o quarto número: '))
)
print(f'Os números {num} foram registrados em uma tupla. ')
print(f'O primeiro número aparece {num.count(num[0])} vezes, ')
if 3 in num:
    print(f'O valor 3 foi digitado na posição {num.index(3) + 1} ')
else:
    print(f'O número 3 não foi registrado na tupla ')
print(f'O número {num[3]} é o quarto número da tupla, ')
print(f'Os números pares inseridos são: ', end='')
for a in num:
    if a % 2 == 0:
        print(a, end='')
