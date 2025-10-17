distancia = float(input('Informa a distancia da sua viagem em Km: '))
if distancia <= 200:
    valor = float(distancia * 0.50)
    print(f'Sua viagem custará R${valor:.2f}')
else:
    valor = float(distancia * 0.45)
    print(f'Por ser mais longa, sua viagem custará R${valor:.2f}')
