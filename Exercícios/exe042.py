r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima formam um triângulo', end='')
    if r1 == r2 == r3:
        print('equilátero.')
    elif r1 != r2 != r3 != r1:
        print('escaleno.')
    else:
        print('isóceles.')
else:
    print('Os segmentos acima não podem formar um triângulo.')
