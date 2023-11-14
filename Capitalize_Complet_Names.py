# Nomes completos capitalizados

nomes = ["joão", "MaRia", "JOSÉ"]
sobrenomes = ["SILVA", "souza", "Tavares"]

nomes_capitalizados = [nome.capitalize() for nome in nomes]

sobrenomes_capitalizados = [sobrenome.capitalize() for sobrenome in sobrenomes]

nome = list(map(lambda x: x, nomes_capitalizados))

sobrenome = list(map(lambda y: y, sobrenomes_capitalizados))

print('Nome Completo: {} {}.'.format(nomes_capitalizados[0], sobrenomes_capitalizados[0]))
print('Nome Completo: {} {}.'.format(nomes_capitalizados[1], sobrenomes_capitalizados[1]))
print('Nome Completo: {} {}.'.format(nomes_capitalizados[2], sobrenomes_capitalizados[2]))
