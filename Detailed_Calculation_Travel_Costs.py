# Cálculo detalhado do custo das viagens

Cidade_inicial = "Recife"
Cidades_Destino = ["Salvador", "Fortaleza", "Natal",  "Aracaju"]

Diaria = 150
# Consumo de Gasolina (km / L)
Carro = 14
# Preço da Gasolina (R$ / L)
Gasolina = 5

Gastos_Passeio = [200, 400, 250, 300]
Distancias = [850, 800, 300, 550]

N_dias = int(input('Digite o número de dias hospedados no hotel: '))
Gasto_Hotel = N_dias * 150

Gastos_Gasolina = list(map(lambda x: 2 * x * (5/14), Distancias))

Gastos_Passeio_Final = list(map(lambda x: x * N_dias, Gastos_Passeio))

Cidade_Destino = input('Qual a cidade de destino? ')

Gastos_Total_Salvador = Gasto_Hotel + Gastos_Gasolina[0] + Gastos_Passeio_Final[0]
Gastos_Total_Fortaleza = Gasto_Hotel + Gastos_Gasolina[1] + Gastos_Passeio_Final[1]
Gastos_Total_Natal = Gasto_Hotel + Gastos_Gasolina[2] + Gastos_Passeio_Final[2]
Gastos_Total_Aracaju = Gasto_Hotel + Gastos_Gasolina[3] + Gastos_Passeio_Final[3]

if Cidade_Destino == Cidades_Destino[0]:
    print('Com base nos gastos definidos, uma viagem de {:.0f} dias para Salvador saindo de Recife custaria {:.2f} reais.'.format(N_dias,Gastos_Total_Salvador))
elif Cidade_Destino == Cidades_Destino[1]:
    print('Com base nos gastos definidos, uma viagem de {:.0f} dias para Fortaleza saindo de Recife custaria {:.2f} reais.'.format(
            N_dias, Gastos_Total_Fortaleza))
elif Cidade_Destino == Cidades_Destino[2]:
    print('Com base nos gastos definidos, uma viagem de {:.0f} dias para Natal saindo de Recife custaria {:.2f} reais.'.format(
            N_dias, Gastos_Total_Natal))
elif Cidade_Destino == Cidades_Destino[3]:
    print('Com base nos gastos definidos, uma viagem de {:.0f} dias para Aracaju saindo de Recife custaria {:.2f} reais.'.format(
            N_dias, Gastos_Total_Aracaju))