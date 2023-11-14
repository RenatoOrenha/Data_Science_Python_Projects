# Sorteando um número inteiro

from random import randint

n = int(input('Digite um número inteiro: '))

num = randint(1, n)

print('O número sorteado foi {:.0f}'.format(num))