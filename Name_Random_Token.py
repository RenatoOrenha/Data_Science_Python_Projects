from random import randint
from math import remainder

num = randint(1000, 9998)
if remainder(num,2) == 0:
    nome = input('Qual o seu nome? ')
    print('Olá, {}, o seu token de acesso é {}! Seja bem-vindo(a)!'.format(nome, num))
else:
    print()



