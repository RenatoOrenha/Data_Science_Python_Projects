# Somar elementos de uma lista

lista_de_listas = [[4,6,5,9], [1,0,7,2], [3,4,1,8]]

def soma(lista):
    calculo = sum(lista)
    return calculo

somas = [round(soma(lista), 1) for lista in lista_de_listas]

print(somas)