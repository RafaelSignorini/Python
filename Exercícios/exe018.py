from math import radians, sin, cos, tan
angulo = float(input('Insira um ângulo: '))
seno = sin(radians(angulo))
print('O ângulo de {}° tem o seno de {:.2f}.'.format(angulo, seno))
cosseno = cos(radians(angulo))
print('O ângulo de {}° tem o cossendo de {:.2f}.'.format(angulo, cosseno))
tangente = tan(radians(angulo))
print('O ângulo de {}° tem a tangente de {:.2f}.'.format(angulo, tangente))
