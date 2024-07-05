salario = float(input('Qual é o valor de seu salário? '))
if salario <= 1250:
    aumento = salario * 0.15
else:
    aumento = salario * 0.1
print('Seu salário receberá um aumento de {:.2f} reais, totalizando {:.2f} reais mensais.'.format(aumento, salario + aumento))
