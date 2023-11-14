# Selecionar palavras com pelo menos 5 caracteres de uma dada frase

Frase = input('Digite uma frase: ')

frase_tratada = Frase.replace(",", " ").replace(".", " ").replace("!",  " ").replace("?", " ").split()

filtro = list(filter(lambda x: len(x) >= 5, frase_tratada))

print(filtro)