# Notas do Estudante

N1 = float(input('Digite a nota: '))
N2 = float(input('Digite a nota: '))
N3 = float(input('Digite a nota: '))
N4 = float(input('Digite a nota: '))

Lista_Notas = [N1, N2, N3, N4]

maior = max(Lista_Notas)

menor = min(Lista_Notas)

media = sum(Lista_Notas) / 4
if media >= 6:
    situacao = 'aprovado'
else:
    situacao = 'reprovado'

print('O(a) estudante obteve uma média de {:.1f}, com a sua maior nota de {:.1f} pontos e a menor nota de {:.1f} pontos e foi {}.'.format(media, maior, menor, situacao))