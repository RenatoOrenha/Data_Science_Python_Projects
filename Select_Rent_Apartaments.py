# Selecionar alugel de apartamentos

aluguel = [('Apartamento', 1700), ('Apartamento', 1400), ('Casa', 2150), ('Apartamento', 1900), ('Casa', 1100)]

apt = [apt[1] for apt in aluguel if apt[0] == 'Apartamento']

print(apt)