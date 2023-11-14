# Soma de items de listas com indicação de erro

lista1 = [4,6,7,9,'A']
lista2 = [-4,'E',8,7,9]

lista3 = []

try:
    for i in range(len(lista1)):
        valor = lista1[i] + lista2[i]
        lista3.append((lista1[i], lista2[i], valor))
except TypeError as e1:
    print('A lista deve conter somente números.')
except IndexError as e2:
    print('A quantidade de elementos em cada lista é diferente.')
else:
    print(lista3)

