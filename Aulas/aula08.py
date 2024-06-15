# Funcionalidade import:

# import {library name}
# from {library name} import {library element}

# Exemplos:

# import math               (importa toda a biblioteca math)
# from math import sqrt     (importa apenas a raiz da biblioteca math)

# Elementos da bibioleta math:

# ceil
# floor
# trunc
# pow
# sqrt
# factorial

from math import sqrt
num = int(input('Insira um número: '))
raiz = sqrt(num)
print(raiz)

import math
n = int(input('Insira mais um número: '))
root = math.sqrt(n)
print(root)

import random
numero = random.randint(0, 100)
print(numero)
