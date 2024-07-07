from datetime import date
maiores = 0
for a in range(0, 7):
    ano = int(input('Insira seu ano de nascimento: '))
    if date.today().year - ano >= 18:
        maiores += 1
print('No total há {}{}{} maiores de idade neste grupo.'.format('\033[7;34m', maiores, '\033[m'))
