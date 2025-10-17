base_de_conversão = str(input('Informe qual a base de conversão (Binário, Octal ou Hexadecimal):')).strip().lower()
if base_de_conversão == "binario" or base_de_conversão == "binário":
    numero = int(input('Informe o valor a ser convertido para binário: '))
    binario = bin(numero)
    print(f"O valor {numero} em binário é igual a {binario[2:]}")
elif base_de_conversão == "octal":
    numero = int(input('Informe o valor a ser convertido para Octal: '))
    octal = oct(numero)
    print(f'O valor {numero} convertido para Octal é igual a {octal[2:]}')
elif base_de_conversão == "hexadecimal" or base_de_conversão == "decimal":
    tipo_de_numero = str(input('Seu número está em Binário ou Octal? ')).strip().lower()
    if tipo_de_numero == "binario" or tipo_de_numero == "binário":
        numero = str(input('Informe o valor em binário: '))
        decimal = int(numero, 2)
        print(f'O número binário: {numero}, em Hexadecimal é igual á: {decimal[2:]}')
    elif tipo_de_numero == "octal":
        numero = str(input('Informe o valor em Octal: '))
        decimal = int(numero, 8)
        print(f'O valor Octal:{numero} em Hexadecimal é igual á: {decimal[2:]}')
    else:
        print('Entrada não reconhecida! Tente novamente!')
else:
    print('Entrada não reconhecida! Tente novamente!')       

