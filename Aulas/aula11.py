# Cores no terminal

# Prefixo '\033['
# Infixos:  1º: style
#           2º: text
#           3º: background
# Sufixo 'm'

# Códigos para style:
# 0     padrão
# 1     bold
# 4     underline
# 7     invert back

# Códigos para text:
# 30    branco
# 31    vermelho
# 32    verde
# 33    amarelo
# 34    azul
# 35    lilás
# 36    ciano
# 37    cinza

# Códigos para back:
# 40    branco
# 41    vermelho
# 42    verde
# 43    amarelo
# 44    azul
# 45    lilás
# 46    ciano
# 47    cinza

print('\033[0;30;41mTeste\033[m')
print('\033[4;33;44mTeste\033[m')
print('\033[1;35;43mTeste\033[m')
print('\033[30;42mTeste\033[m')
print('\033[mTeste\033[m')
print('\033[7;30mTeste\033[m')

# Prática
print('\033[1;31;43mOlá, Mundo!\033[m')
print('\033[4;30;45mOlá, Mundo!\033[m')
print('\033[30mOlá, Mundo!\033[m')
print('\033[7;30mOlá, Mundo!\033[m')
print('\033[33;44mOlá, Mundo!\033[m')
print('\033[7;33;44mOlá, Mundo!\033[m')

# Exemplos com valores:
a = 4
b = 5
print('Os valores são \033[1;31;44m{}\033[m e \033[1;36;42m{}\033[m.'.format(a, b))

nome = 'Rafael'
print('Prazer em te conhecer, {}{}{}.'.format('\033[4;31m', nome, '\033[m'))
