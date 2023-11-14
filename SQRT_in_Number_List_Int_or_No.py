# Checar se a raiz quadrada dos números na lista são inteiros ou não

from random import  choice
from math import sqrt

num = [2, 8, 15, 23, 91, 112, 256]

teste1 = sqrt(num[0])
teste2 = sqrt(num[1])
teste3 = sqrt(num[2])
teste4 = sqrt(num[3])
teste5 = sqrt(num[4])
teste6 = sqrt(num[5])
teste7 = sqrt(num[6])

teste1_2 = teste1 // 1
teste2_2 = teste2 // 1
teste3_2 = teste3 // 1
teste4_2 = teste4 // 1
teste5_2 = teste5 // 1
teste6_2 = teste6 // 1
teste7_2 = teste7 // 1

if teste1 == teste1_2:
    print('A raiz quadrada de {} é um número inteiro!'.format(num[0]))
else:
    print('A raiz quadrada de {} não é um número inteiro!'.format(num[0]))

if teste2 == teste2_2:
    print('A raiz quadrada de {} é um número inteiro!'.format(num[1]))
else:
    print('A raiz quadrada de {} não é um número inteiro!'.format(num[1]))

if teste3 == teste3_2:
    print('A raiz quadrada de {} é um número inteiro!'.format(num[2]))
else:
    print('A raiz quadrada de {} não é um número inteiro!'.format(num[2]))

if teste4 == teste4_2:
    print('A raiz quadrada de {} é um número inteiro!'.format(num[3]))
else:
    print('A raiz quadrada de {} não é um número inteiro!'.format(num[3]))

if teste5 == teste5_2:
    print('A raiz quadrada de {} é um número inteiro!'.format(num[4]))
else:
    print('A raiz quadrada de {} não é um número inteiro!'.format(num[4]))

if teste6 == teste6_2:
    print('A raiz quadrada de {} é um número inteiro!'.format(num[5]))
else:
    print('A raiz quadrada de {} não é um número inteiro!'.format(num[5]))

if teste7 == teste7_2:
    print('A raiz quadrada de {} é um número inteiro!'.format(num[6]))
else:
    print('A raiz quadrada de {} não é um número inteiro!'.format(num[6]))
