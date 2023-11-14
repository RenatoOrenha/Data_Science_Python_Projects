# Resumir lista de funcionários por estado

funcionarios = [('SP', 16), ('ES', 8), ('MG', 9), ('MG', 6), ('SP', 10), ('MG', 4), ('ES',9), ('ES', 7), ('ES', 12), ('SP', 7), ('SP', 11), ('MG',8), ('ES',8), ('SP',9), ('RJ', 13), ('MG', 5), ('RJ', 9), ('SP', 12), ('MG', 10), ('SP', 7), ('ES', 14), ('SP', 10), ('MG', 12)]

count_SP = 0
count_MG = 0
count_ES = 0
count_RJ = 0

lista_valores_SP = []
lista_valores_MG = []
lista_valores_RJ = []
lista_valores_ES = []

for i in range(len(funcionarios)):
    if funcionarios[i][0] == 'SP':
        count_SP = count_SP + funcionarios[i][1]
        valor = funcionarios[i][1]
        lista_valores_SP.append(valor)
    else:
        'no'

for i in range(len(funcionarios)):
    if funcionarios[i][0] == 'RJ':
        count_RJ = count_RJ + funcionarios[i][1]
        valor = funcionarios[i][1]
        lista_valores_RJ.append(valor)
    else:
        'no'

for i in range(len(funcionarios)):
    if funcionarios[i][0] == 'MG':
        count_MG = count_MG + funcionarios[i][1]
        valor = funcionarios[i][1]
        lista_valores_MG.append(valor)
    else:
        'no'

for i in range(len(funcionarios)):
    if funcionarios[i][0] == 'ES':
        count_ES = count_ES + funcionarios[i][1]
        valor = funcionarios[i][1]
        lista_valores_ES.append(valor)
    else:
        'no'

valores = [count_SP, count_RJ, count_MG, count_ES]

all = {'SP': count_SP, 'MG': count_MG, 'RJ': count_RJ, 'ES': count_ES}

all_lista = {'SP': lista_valores_SP, 'MG': lista_valores_MG, 'RJ': lista_valores_RJ, 'ES': lista_valores_ES}

print(all)

print(all_lista)