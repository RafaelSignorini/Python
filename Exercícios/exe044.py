print('{:=^40}'.format(' Reis Informática '))
valor = float(input('Insira o valor a ser pago: \n'))
pagamento = int(input('FORMAS DE PAGAMENTO: \n\n[ 1 ] para à vista com cheque / dinheiro (-10%) \n[ 2 ] para à vista no cartão (-5%) \n[ 3 ] para 2x no cartão (preço normal) \n[ 4 ] para 3x ou mais (20% de juros simples) \n\n'))
if pagamento == 1:
    print('O valor final ficou de R${}{:.2f}{} com {}{}{} de desconto.'.format('\033[32m', valor * 0.9, '\033[m', '\033[33m', '10%', '\033[m'))
elif pagamento == 2:
    print('O valor final ficou de R${}{:.2f}{} com {}{}{} de desconto.'.format('\033[32m', valor * 0.95, '\033[m', '\033[33m', '5%', '\033[m'))
elif pagamento == 3:
    print('O valor final ficou de R${}{:.2f}{} em {}{}{}.'.format('\033[32m', valor, '\033[m', '\033[31m', '2 parcelas', '\033[m'))
    print('Cada parcela vale R${}{:.2f}{}.'.format('\033[32m', valor / 2, '\033[m'))
elif pagamento == 4:
    parcelas = int(input('Insira a quantidade de vezes que deseja parcelar: '))
    print('O valor final ficou de R${}{:.2f}{} em {}{} parcelas{} com {}{}{} de juros.'.format('\033[32m', valor * 1.2, '\033[m', '\033[31m', parcelas, '\033[m', '\033[33m', '20% de juros', '\033[m'))
    print('Cada parcela vale R${}{:.2f}{}.'.format('\033[32m', (valor * 1.2) / parcelas, '\033[m'))
else:
    print('Valor inserido inválido, tente novamente.')
