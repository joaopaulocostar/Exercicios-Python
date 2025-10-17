largura = float(input('Informe a largura da parede: '))
altura = float(input('Informe a altura da parede: '))

def area_parede(largura, altura):
    area_quadrada = largura*altura
    return area_quadrada

def tinta(area_quadrada):
    area_de_tinta = area_quadrada/2
    return area_de_tinta

area_total = area_parede(largura,altura)
tinta_total = tinta(area_total)

print(f'A sua parede possui {area_total:.2f}m2, que exigirá {tinta_total:.2f} litros de tinta!')



