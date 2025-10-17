nome = str(input('Informe seu nome completo: '))
print(f'Nome: {nome}')
nome = nome.strip().split()
print(f'Primeiro: {nome[0]}')
print(f'Último: {nome[-1]}')

