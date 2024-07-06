preco = float(input('Qual é o preço do empréstimo da casa? '))
salario = float(input('E qual é o seu salário? '))
tempo = int(input('Insira o tempo, \033[33mem meses\033[m, no qual o pagamento será feito: '))
if salario < 0:
    print('Valor inserido inválido. Tente novamente.')
elif salario * 0.3 < preco / tempo:
    print('O empréstimo de {}R${:.2f}{} não pode ser realizado pois excede {}30 por cento{} do valor de seu salário.'.format('\033[32m', preco, '\033[m', '\033[31m', '\033[m'))
elif salario * 0.3 >= preco / tempo:
    mensal = preco / tempo
    print('Você terá que pagar {}R${:.2f}{} mensais '.format('\033[32m', mensal, '\033[m'), end='')
    print('para que seu empréstimo de {}R${:.2f}{} '.format('\033[7;32m', preco, '\033[m'), end='')
    print('seja pago no final de {}{}{} meses.'.format('\033[33m', tempo, '\033[m'))
else:
    print('Algo de errado ocorreu com o programa, tente novamente.')
