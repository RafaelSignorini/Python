from random import randint
pc = randint(0, 2)

if pc == 0:
    adversario = 'pedra'
elif pc == 1:
    adversario = 'papel'
else:
    adversario = 'tesoura'

u = int(input('Pedra (0), papel (1) ou tesoura (2)? \n'))

if u == 0:
    usuario = 'pedra'
elif u == 1:
    usuario = 'papel'
else:
    usuario = 'tesoura'

if pc == u:
    print('Empate\n\nPC: {}{}{}\nUsuário: {}{}{}'.format('\033[34m', adversario, '\033[m', '\033[35m', usuario, '\033[m'))
elif (pc == 0 and u == 1) or (pc == 1 and u == 2) or (pc == 2 and u == 0):
    print('O Usuário venceu\n\nPC: {}{}{}\nUsuário: {}{}{}'.format('\033[34m', adversario, '\033[m', '\033[35m', usuario, '\033[m'))
elif u < 0 or u > 2:
    print('O valor "{}" não é válido, por favor tente novamente.'.format(u))
else:
    print('O PC venceu\n\nPC: {}{}{}\nUsuário: {}{}{}'.format('\033[34m', adversario, '\033[m', '\033[35m', usuario, '\033[m'))
