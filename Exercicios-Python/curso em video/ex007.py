n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))
media = (n1+n2)/2
print('A média das notas do aluno é igual a: {}'.format(media))
if media >= 7:
    print('APROVADO!')
else:
    print(f'REPROVADO! Faltam {7-media:.2f} para o aluno ser aprovado.')
    


