a = float(input('Informe o valor da primeira reta: '))
b = float(input('Informe o valo da segunda reta: '))
c = float(input('Informe o valor da terceira reta: '))
if a + b > c and a + c > b and b + c > a:
    print('É possível formar um triângulo!!')
else:
    print('Não é possível formar um triângulo!!')


