from decimal import Decimal

salario = float(input('Informe o valor do salário: '))
aumento = float(15/100 * salario)
salario_real = Decimal(salario)
aumento_real = Decimal(aumento)
print(f'Seu salário de R${salario_real:.2f} com 15% de aumento irá para R${salario_real + aumento_real:.2f}')
