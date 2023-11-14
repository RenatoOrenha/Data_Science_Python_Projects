# Contagem do número de estados em uma lista

estados = ['SP', 'ES', 'MG', 'MG', 'SP', 'MG', 'ES', 'ES', 'ES', 'SP', 'SP', 'MG', 'ES', 'SP', 'RJ', 'MG', 'RJ', 'SP', 'MG', 'SP', 'ES', 'SP', 'MG']

count_SP = 0
count_RJ = 0
count_MG = 0
count_ES = 0

for i in range(len(estados)):
    if estados[i] == 'SP':
        count_SP = count_SP + 1
    else:
        'no'

for i in range(len(estados)):
    if estados[i] == 'MG':
        count_MG = count_MG + 1
    else:
        'no'

for i in range(len(estados)):
    if estados[i] == 'RJ':
        count_RJ = count_RJ + 1
    else:
        'no'

for i in range(len(estados)):
    if estados[i] == 'ES':
        count_ES = count_ES + 1
    else:
        'no'

valores = [count_SP, count_MG, count_RJ, count_ES]

all = {'SP': count_SP, 'RJ': count_RJ, 'ES': count_ES, 'MG': count_MG}

print(all)