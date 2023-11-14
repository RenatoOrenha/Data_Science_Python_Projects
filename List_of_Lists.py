# Elaboração de Lista de Listas

id = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
quantidades = [15, 12, 1, 15, 2, 11, 2, 12, 2, 4]
precos = [93.0, 102.0, 18.0, 41.0, 122.0, 14.0, 71.0, 48.0, 14.0, 144.0]

total = [round((quantidade * preco), 1) for quantidade, preco in zip(quantidades, precos)]

cabeçalho = ['id', 'quantidade', 'preco', 'total']

informations = [(id[i], quantidades[i], precos[i], total[i]) for i in range(len(id))]

all = [cabeçalho, informations]

print(all)

