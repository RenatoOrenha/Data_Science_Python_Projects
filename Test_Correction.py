# Correção de Prova

gabarito = ['D', 'A', 'B', 'C', 'A']
testes_sem_ex = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'C', 'A'], ['D', 'B', 'A', 'C', 'A']]
testes_com_ex = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'E', 'A'], ['D', 'B', 'A', 'C', 'A']]

# Checar Válidade da Alternativa Escolhida
notas_estudante_1 = testes_com_ex[0]
notas_estudante_2 = testes_com_ex[1]
notas_estudante_3 = testes_com_ex[2]

for i in range(len(gabarito)):
    if notas_estudante_1[i] not in ['A', 'B', 'C', 'D']:
        print('A alternativa assinalada pelo estudante 1 na questão {} não é uma opção válida.'.format(i))
    elif notas_estudante_2[i] not in ['A', 'B', 'C', 'D']:
        print('A alternativa assinalada pelo estudante 2 na questão {} não é uma opção válida.'.format(i))
    elif notas_estudante_3[i] not in ['A', 'B', 'C', 'D']:
        print('A alternativa assinalada pelo estudante 3 na questão {} não é uma opção válida.'.format(i))
    else:
        print()

# Correção da Prova Válida do Estudante 1
nota_final_estudante_1 = 0

if testes_sem_ex[0][0] == 'D':
    nota_final_estudante_1 += 1
else:
    nota_final_estudante_1 += 0
if testes_sem_ex[0][1] == 'A':
    nota_final_estudante_1 += 1
else:
    nota_final_estudante_1 += 0
if testes_sem_ex[0][2] == 'B':
    nota_final_estudante_1 += 1
else:
    nota_final_estudante_1 += 0
if testes_sem_ex[0][3] == 'C':
    nota_final_estudante_1 += 1
else:
    nota_final_estudante_1 += 0
if testes_sem_ex[0][4] == 'A':
    nota_final_estudante_1 += 1
else:
    nota_final_estudante_1 += 0

# Correção da Prova Válida do Estudante 2
nota_final_estudante_2 = 0

if testes_sem_ex[1][0] == 'D':
    nota_final_estudante_2 += 1
else:
    nota_final_estudante_2 += 0
if testes_sem_ex[1][1] == 'A':
    nota_final_estudante_2 += 1
else:
    nota_final_estudante_2 += 0
if testes_sem_ex[1][2] == 'B':
    nota_final_estudante_2 += 1
else:
    nota_final_estudante_2 += 0
if testes_sem_ex[1][3] == 'C':
    nota_final_estudante_2 += 1
else:
    nota_final_estudante_2 += 0
if testes_sem_ex[1][4] == 'A':
    nota_final_estudante_2 += 1
else:
    nota_final_estudante_2 += 0

#Correção da Prova Válida do Estudante 3
nota_final_estudante_3 = 0

if testes_sem_ex[2][0] == 'D':
    nota_final_estudante_3 += 1
else:
    nota_final_estudante_3 += 0
if testes_sem_ex[2][1] == 'A':
    nota_final_estudante_3 += 1
else:
    nota_final_estudante_3 += 0
if testes_sem_ex[2][2] == 'B':
    nota_final_estudante_3 += 1
else:
    nota_final_estudante_3 += 0
if testes_sem_ex[2][3] == 'C':
    nota_final_estudante_3 += 1
else:
    nota_final_estudante_3 += 0
if testes_sem_ex[2][4] == 'A':
    nota_final_estudante_3 += 1
else:
    nota_final_estudante_3 += 0

print('As notas válidas dos estudantes foram: {:.1f}, {:.1f} e {:.1f}.'.format(nota_final_estudante_1, nota_final_estudante_2, nota_final_estudante_3))
