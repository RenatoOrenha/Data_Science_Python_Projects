# Selecionar o terceiro elemento de cada lista de tuplas

lista_de_tuplas = [('Pedro', 1.74, 81), ('Júlia', 1.65, 67), ('Otávio', 1.81, 83)]

lista = [lista[2] for lista in lista_de_tuplas]

print(lista)