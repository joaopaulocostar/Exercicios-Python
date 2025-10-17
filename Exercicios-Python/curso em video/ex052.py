numero = int(input("Informe um número: "))
primo = True
if numero <= 1:
    primo = False
elif numero == 2:
    primo = True
else:
    for c in range(2, numero):
        if numero % c == 0:
            primo = False
if primo:
    print('É primo!')
else:
    print('Não é primo!')
