# Calculo do preço da área do gramado

import  math

Preco = 25

r = float(input('Qual o raio da área circular do gramado? '))

area = (math.pi * pow(r, 2))

Preco_Final = area * Preco

print('O preço final é igual a {:.2f}'.format(Preco_Final))