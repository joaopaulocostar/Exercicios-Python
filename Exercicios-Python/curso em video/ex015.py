km = float(input('Informe a quantidade de Km rodados: '))
dias = int(input('Informe a quantidade de dias alugados: '))
preco = ((dias * 60) + (km * 0.15))
print(f'O valor total foi de R${preco:.2f}')
