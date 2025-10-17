from decimal import Decimal
metro = Decimal(input('Escreva o valor em metros: '))
centimetros = Decimal(metro*100)
milimetros = Decimal(metro*1000)
print(' {} Metros:\n Em Centimetros {};\n Em Milimetros {}; '.format(metro,centimetros,milimetros))