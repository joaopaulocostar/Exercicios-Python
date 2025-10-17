from datetime import date
hoje = date.today()
ano = hoje.year
idade = int(input('Informe o seu ano de nascimento: '))
idade_atual = ano - idade
print(f'Você possui {idade_atual} anos')

if idade_atual < 18:
    print('Você ainda vai se alistar!')
    print(f'Faltam {18 - idade_atual} anos para se alistar!')
elif idade_atual > 18:
    print('Já passou da hora de se alistar!')
    print(f'Você deveria ter se alistado a {idade_atual - 18} anos!')
else:
    print('Está na hora de se alistar!')

