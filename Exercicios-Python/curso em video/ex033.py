n1 = int(input('Informe um número: '))
n2 = int(input('Informe mais um número: '))
n3 = int(input('Informe outro número: '))
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
elif n3 < n1 and n3 < n2:
    menor = n3
maior = n2
if n1 > n2 and n1 > n3:
    maior = n1
elif n3 > n2 and n3 > n2:
    maior = n3
print(f'O menor número é {menor}')
print(f'O maior número é {maior}')




'''if n1 > n2 and n2 > n3:
    print(f"O maior número é {n1}")
    print( f"O menor número é {n3}")
elif n2 > n1 and n1 > n3:
    print(f'O maior número é {n2}')
    print(f'O menor número é {n3}')
elif n3 > n2 and n2 > n1:
    print(f'O maior número é {n3}')
    print(f'O menor número é {n1}')
elif n2 >n3 and n3 > n1:
    print(f'O maior número é {n2}')
    print(f'O menor número é {n1}')
elif n3 > n1 and n1 > n2:
    print(f'O maior número é {n3}')
    print(f'O menor número é {n2}')
elif n1 > n3 and n3 > n2:
    print(f'O maior número é {n1}')
    print(f'O menor número é {n2}')'''



