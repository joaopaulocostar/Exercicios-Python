termo = int(input('Informe o primeiro termo: '))
razao = int(input('Informe o valor da razão: '))
final = termo + 10 * razao
for c in range(termo, final, razao):
    print(c)

