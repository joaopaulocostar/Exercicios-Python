letra = str(input('Escreva uma frase: ')).strip()
letra = letra.upper()
print(f'A letra "A" aparece {letra.count('A')} vezes')
print(f'A letra "A" aparece pela primeira vez na posição {letra.find('A') + 1}')
print(f'A letra "A" aparece pela ultima vez na posição {letra.rfind('A') + 1}')



