from math import hypot
cateto = float(input('Informe o comprimento do cateto oposto: '))
adjacente = float(input('Informe o comprimento do cateto adjacente: '))
hipotenusa = hypot(cateto, adjacente)
print(f'O comprimento da Hipotenusa é igual a: {hipotenusa:.2f}')


