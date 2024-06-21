# Manipulação de texto

frase = 'Curso em Vídeo Python'

# Fatiamento:

# frase[9] == 'V'                                           indica o valor na posição [9]

# frase[9:13] == 'Víde'                                     exclui o último valor da colchete

# frase[9:21] == 'Vídeo Python'                             apersar de não existir a casa [21],
#                                                           o Python vai representar da casa [9]
#                                                           até a [20] sem erro algum

# frase[9:21:2] == 'VdoPto'                                 o terceiro número indica de quantas 
#                                                           em quantas casas o Python vai
#                                                           mostrar dos valores no índice

# frase[:5] == 'Curso'                                      oculta tudo a partir da casa [5]

# frase[15:] == 'Python'                                    oculta tudo antes da casa [15]

# frase[9::3] == 'VePh'                                     caso não haja valor entre os dois ':',
#                                                           significa que o valor no meio é
#                                                           indefinido, ou seja, até o final
#                                                           neste caso, enquanto o valor 3
#                                                           significa que ira pular de 3 em 3
#                                                           casas no índice

# len(frase) == 21                                          apresenta a quantidade de caracteres
#                                                           em uma variável de texto

# frase.count('o') == 3                                     conta a quantidade de valores iguais
#                                                           ao que é representado dentro dos
#                                                           parênteses, neste caso, 3 "o"s

# frase.count('o', 0, 13) == 1                              conta a quantidade de valores iguais
#                                                           ao que é representado dentro dos
#                                                           parênteses porém com fatiamento
#                                                           exclusivo ao último valor, ou seja,
#                                                           do índice 0 até antes de 13 (no caso
#                                                           12) ele conta a quantidade de "o"s,
#                                                           ou seja, 1

# frase.find('deo') == 11                                   procura e indica a posição da parte
#                                                           que indica os parâmetros de procura

# frase.find('Android') == -1                               indica que não há a parte procurada
#                                                           dentro da variável

# 'Curso' in frase == True                                  retorna de se é verdade ou não a
#                                                           existência de certo texto no parâmetro

# frase.replace('Python', 'Android')                        procura e substitui o primeiro valor
#                                                           do parâmetro pelo segundo valor

# frase.upper() == 'CURSO EM VÍDEO PYTHON'                  coloca todas as letras em maiúsculas

# frase.lower() == 'curso em vídeo python'                  coloca todas as letras em minúsculas

# frase.capitalize() == 'Curso em vídeo python'             coloca a primeira letra da string
#                                                           em maiúscula

# frase.title() == 'Curso Em Vídeo Python'                  coloca a primeira letra de cada
#                                                           palavra da string em maiúscula

# frase = '   aprenda python   '

# frase.strip() == 'aprenda python'                         corta todos os espaços inúteis antes
#                                                           ou depois de qualquer letra que não
#                                                           esteja no meio de outros caracteres

# frase.lstrip() == 'aprenda python   '                     corta apenas os espaços à esquerda de
#                                                           caracteres

# frase.rstrip() == '   aprenda python'                     corta apenas os espaços à direita de
#                                                           caracteres

# frase.split() == 'Curso', 'em', 'Vídeo', 'Python'         separa todas as palavras na string
#                                                           baseado no posicionamento de cada
#                                                           espaço existente

# '-'.join(frase) == 'Curso-em-Vídeo-Python'                substitui os espaços por o que estiver
#                                                           dentro das aspas antes do .join()

# Prática:

print(frase)
print(frase[3])             # s
print(frase[3:13])          # so em Víde
print(frase[:13])           # Curso em Víde
print(frase[13:])           # o Python
print(frase[1:15])          # urso em Vídeo
print(frase[1:15:2])        # us mVdo
print(frase[1::2])          # us mVdoPto
print(frase[::2])           # Croe íe yhn

# texto de múltiplas linhas:

print('''bom dia fdp
como vai
arrombado''')

# também serve de comentário fora da função print()

# Importante: letras maiúsculas e minúsculas não são a mesma coisa em texto
