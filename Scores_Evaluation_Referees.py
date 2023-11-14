# Notas e avaliação dos Jurados

Jur_1 = float(input('Digite a nota do skatista: '))
Jur_2 = float(input('Digite a nota do skatista: '))
Jur_3 = float(input('Digite a nota do skatista: '))
Jur_4 = float(input('Digite a nota do skatista: '))
Jur_5 = float(input('Digite a nota do skatista: '))

Lista_Notas = [Jur_1, Jur_2, Jur_3, Jur_4, Jur_5]

maior = max(Lista_Notas)

menor = min(Lista_Notas)

Lista_Notas.remove(maior)

Lista_Notas.remove(menor)

media = sum(Lista_Notas) / 3

print(media)


