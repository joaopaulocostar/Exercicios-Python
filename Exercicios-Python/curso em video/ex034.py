salario = float(input('Informe o valor do salário R$: '))
if salario > 1250:
    aumento = float(salario + ((10/100) * salario))
    print(f'Seu novo salário com 10% de aumento será de {aumento:.2f}')
else:
    aumento = float(salario + ((15/100) * salario))
    print(f'Seu novo salário com 15% de aumento será de {aumento:.2f}')
    