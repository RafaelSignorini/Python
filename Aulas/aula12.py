# Condições aninhadas
nome = str(input('Insira seu nome: '))
if nome.lower() == 'stéfany':
    print('Seu nome é muito lindo. ', end='')
elif nome.lower() == 'rafael':
    print('Você tem um nome de burguês safado. ', end='')
elif nome.lower() == 'lula':
    print('Faz o L carai. ', end='')
else:
    print('Não sei nenhuma curiosidade sobre seu nome. ', end='')
print('Prazer em te conhecer, {}.'.format(nome.lower().capitalize()))
