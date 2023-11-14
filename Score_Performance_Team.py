# Pontuação e aproveitamento do time

gols_marcados = [2, 1, 3, 1, 0]
gols_sofridos =    [1, 2, 2, 1, 3]

pontos_final = 0

for i in range(len(gols_marcados)):
    if gols_marcados[i] > gols_sofridos[i]:
        pontos_final += 3
    elif gols_marcados[i] == gols_sofridos[i]:
        pontos_final += 1

pontos_max = 5*3

aprov = (pontos_final / pontos_max) * 100

print('A pontuação do time foi de {} e seu aproveitamento foi de {:.2f}%.'.format(pontos_final, aprov))