from datetime import date
nome = str(input('Insira seu nome: \n'))
idade = int(input('Insira sua idade no final deste ano (após seu aniversário): \n'))
dataMes = 6
if idade == 18:
    print('Você está na idade para se alistar no exército.')
    if dataMes > date.today().month:
        print('Você ainda tem {}{}{} meses para se alistar.'.format('\033[33m', abs(date.today().month - dataMes), '\033[m'))
    elif dataMes < date.today().month:
        print('Você já deveria ter se alistado a {}{}{} meses.'.format('\033[33m', abs(date.today().month - dataMes), '\033[m'))
else:
    print('Você não precisa se alistar ao exército.')
