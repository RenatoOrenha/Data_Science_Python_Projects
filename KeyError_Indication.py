# Indicação de KeyError

idades = {'Júlia': 16, 'Carol': 23, 'Alberto': 19, 'Roberta': 17}

try:
    nome = input('Digite um nome: ')
    nome = idades[nome]
except KeyError as e:
    print('Nome não encontrado.')
else:
    print(nome)