velocidade = int(input('Informe a velocidade do carro: '))
multa = float(velocidade - 80)
if velocidade > 80:
    print('VOCÊ FOI MULTADO!!!')
    print(f'Sua multa é no valor de R${multa * 7.00:.2f}')
else:
    print('PODE SEGUIR! TENHA UMA BOA VIAGEM!!')

