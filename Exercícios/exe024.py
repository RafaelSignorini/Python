cidade = str(input('Insira o nome de sua cidade para que o sistema verifique se ela contém a palavra "Santo" no nome: ')).strip()
print(cidade[:5].lower() == 'santo')
