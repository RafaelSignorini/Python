alunos = []
while True:
    nome  = str(input('Nome de alune: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [s/n]: ')).strip().lower()[0]
    if resp == 'n':
        break
print('-=-' * 15)
print(f'{"#":<4}{"Nome":<10}{"Média":>8}')
print('-=-' * 15)
for i, a in enumerate(alunos):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-=-' * 15)
    opcao = int(input('Mostrar as notas de qual alune? ("-1" para interromper o programa)'))
    if opcao == -1:
        break
    if opcao in len(alunos)-1:
        print(f'Notas de {alunos[opcao][0]} são {alunos[opcao][1]}.')
print('Você terminou o programa.')
