import math
angulo = int(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(angulo))
print(f'O seno do angulo {angulo} é igual a {seno:.2f}')
cosseno = math.cos(math.radians(angulo))
print(f'O cosseno do angulo {angulo} é igual a {cosseno:.2f}')
tangente = math.tan(math.radians(angulo))
print(f'A tangente do angulo {angulo} é igual a {tangente:.2f}')
