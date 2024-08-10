def contador(i, f, p):
    while True:
        print(f'De {i} até {f}, indo de {p} em {p}, temos: ')
        for a in range(i, f+1, p):
            print(f'{a}')
        print(f'De {f} até {i}, indo de {p*2} em {p*2}, temos: ')
        for a in range(f, i, p*-2):
            print(f'{a}')
        print(f'De {i*-1} até {f*3}, indo de {p*5} em {p*5}, temos: ')
        for a in range(i*-1, (f+1)*3, p*5):
            print(f'{a}')
        break
    print('fim')


contador(i = int(input('Início: ')), f = int(input('Fim: ')), p = int(input('Passo: ')))
