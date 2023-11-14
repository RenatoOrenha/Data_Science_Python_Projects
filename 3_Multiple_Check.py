# Checar múltiplos de 3 na lista

lista = [97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]

mult_3 = []

for i in range(len(lista)):
    if lista[i] % 3 == 0:
        mult_3.append(lista[i])
    else:
        print()

print(mult_3)