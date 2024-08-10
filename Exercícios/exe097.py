def escreva(msg):
    print('-=-'*10)
    print(f'{msg:^30}')
    print('-=-'*10)


escreva(msg = str(input('Texto: ')).strip().capitalize())
