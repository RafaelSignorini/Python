cont = (
    'time1', 'time2', 'time3', 'chapeco', 'time5', 
    'time6', 'time7', 'time8', 'time9', 'time10', 
    'time11', 'time12', 'time13', 'time14', 'time15', 
    'time16', 'time17', 'time18', 'time19', 'time20'
)
print(f'Os primeiros 5 times colocados são \033[36m{cont[:5]}\033[m')
print(f'Os últimos 4 times colocados são \033[31m{cont[-4:]}\033[m')
print(f'Times em ordem alfabética: \033[35m{sorted(cont)}\033[m')
print(f'O \033[32mChapecoense\033[m está na posição {cont.index("chapeco") + 1}')
