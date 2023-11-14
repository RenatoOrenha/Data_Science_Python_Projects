# Divisão de Valores e possíveis erros

pressoes = [60, 120, 140, 160, 180]
temperaturas = [10, 25, 30, 35, 40]

p_t = []

try:
    if len(pressoes) != len(temperaturas):
        raise ValueError('As listas apresntam tamanhos diferentes.')
    for i in range(len(temperaturas)):
        if temperaturas[i] == 0:
            raise ZeroDivisionError('Valor da temperatura tem que ser diferente de zero.')
    for i in range(len(temperaturas)):
        divide_colunas = round(pressoes[i] / temperaturas[i], 1)
        p_t.append(divide_colunas)
finally:
    print(p_t)
