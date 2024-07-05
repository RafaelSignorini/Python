frase = str(input('Insira uma frase qualquer para que o programa verifique quantas letras "a" há na frase e em que posições ela aparece: ')).lower().strip()
print('A letra A aparece {} vezes na frase.'.format(frase.count('a')))
print('A primeira letra A parece na posição {} e a última aparece na posição {}.'.format(frase.find('a') + 1, frase.rfind('a') + 1))
