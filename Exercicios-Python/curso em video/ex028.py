from random import choice
from time import sleep
lista = [0,1,2,3,4,5]
sorteio = choice(lista)
escolha = int(input('Escolha uma número de 0 a 5: '))
print('PROCESSANDO...')
sleep(3)
if escolha == sorteio:
    print('VOCÊ ACERTOU!!!!! :)')
else:
    print('VOCÊ ERROU!!! :(')


