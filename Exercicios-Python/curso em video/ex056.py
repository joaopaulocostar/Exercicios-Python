total_pessoas = []
for c in range(0,4):
   nome = str(input('Informe o seu nome: '))
   idade = int(input('Informe a sua idade: '))
   sexo = str(input('Informe o seu sexo: ')).strip().lower()
   pessoas = {
    'nome': nome,
    'idade': idade,
    'sexo': sexo
}
   total_pessoas.append(pessoas)

idade_masculino = 0
contadorM = 0
idade_feminino = 0
contadorF = 0
for pessoas in total_pessoas:
    if pessoas['sexo'] == "m":
        idade_masculino += pessoas['idade']
        contadorM += 1
    elif pessoas['sexo'] == "f":
        idade_feminino += pessoas['idade']
        contadorF += 1

if contadorM > 0:
    media_m = idade_masculino / contadorM
    print(f"A média de idade do sexo masculino é de {media_m}")
if contadorF > 0:
    media_f = idade_feminino / contadorF
    print(f"A média de idade do sexo feminino é de {media_f}")


