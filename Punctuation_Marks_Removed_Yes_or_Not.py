# Checar se os sinais de pontuação das palavras foram removidos

lista_tratada = ['Python', 'é', 'uma', 'linguagem', 'de', 'programação', 'poderosa', 'versátil',
                  'e', 'fácil', 'de', 'aprender', 'utilizada', 'em', 'diversos', 'campos', 'desde',
                  'análise', 'de', 'dados', 'até', 'inteligência', 'artificial']
lista_nao_tratada = ['Python', 'é', 'uma', 'linguagem', 'de', 'programação', 'poderosa,', 'versátil',
                  'e', 'fácil,', 'de', 'aprender', 'utilizada', 'em', 'diversos', 'campos,', 'desde',
                  'análise', 'de', 'dados', 'até', 'inteligência', 'artificial!']

# Checar se há pontuação nas palavras
def avalia_texto(lista: list):
    for i in lista:
        if (',' or '.' or '!' or '?') in i:
            raise ValueError('O texto apresenta pontuação na palavra {}'.format(i))
    return 'Texto já tratado.'

#Avaliar lista tratada
try:
    avaliacao = avalia_texto(lista_tratada)
except Exception as e:
    print('Erro: {}.'.format(e))
else:
    print(avaliacao)

#Avaliar lista não tratada
try:
    avaliacao = avalia_texto(lista_nao_tratada)
except Exception as e:
    print('Erro: {}.'.format(e))
else:
    print(avaliacao)
