# Rotulagem do nível de glicemia juntando listas

glicemia = [129, 82, 60, 97, 101, 65, 62, 167, 87, 53, 58, 92, 66, 120, 109, 62, 86, 96, 103, 88, 155, 52, 89, 73]

# Glicose igual ou inferior a 70: 'Hipoglicemia'
# Glicose entre 70 a 99: 'Normal'
# Glicose entre 100 e 125: 'Alterada'
# Glicose superior a 125: 'Diabetes'

rotulo = ['Hipoglicemia' if glic <= 70 else 'Normal' if  glic > 70 and glic < 99 else 'Alterada' if glic > 100 and glic < 125 else 'Diabetes' if glic > 125 else 'no' for glic in glicemia]

glicemias = list(zip(rotulo, glicemia))

print(glicemias)