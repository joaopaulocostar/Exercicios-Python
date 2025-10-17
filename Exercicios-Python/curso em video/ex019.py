import random
a1 = str(input('Informe o nome do aluno: '))
a2 = str(input('Informe o nome do aluno: '))
a3 = str(input('Informe o nome do aluno: '))
a4 = str(input('Informe o nome do aluno: '))
lista = [a1,a2,a3,a4]
print(f'O aluno sorteado foi = {random.choice(lista)}')




