# Criar Lista indicando possível erro

item_0_lista = float(input('Digite um número qualquer: '))
item_1_lista = float(input('Digite um número qualquer: '))
item_2_lista = float(input('Digite um número qualquer: '))
item_3_lista = float(input('Digite um número qualquer: '))

lista = []

try:
    lista.append(item_0_lista)
    lista.append(item_1_lista)
    lista.append(item_2_lista)
    lista.append(item_3_lista)
except Exception as e:
    print('Erro: {}.'.format(e))
else:
    print(lista)
finally:
    print('Fim da execução da função.')
