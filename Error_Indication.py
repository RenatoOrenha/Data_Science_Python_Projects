# Indicar erro

num_1 = float(input('Digite um número qualquer: '))
num_2 = float(input('Digite outro número qualquer: '))

try:
    print(num_1 / num_2)
except Exception as error:
    print('Erro: {}.'.format(error))



