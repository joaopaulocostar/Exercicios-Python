class MaiorMenor:
    def __init__(self, peso):
        self.peso = peso

    def maior(self):
        peso_do_usuario = self.peso
        maior = max(peso_do_usuario)
        return maior
    
    def menor(self):
        peso_do_usuario = self.peso
        menor = min(peso_do_usuario)
        return menor
    
todos_os_pesos = []
for c in range(0,5):
    pesos = float(input("Informe um peso: "))
    todos_os_pesos.append(pesos)
pesos = MaiorMenor(todos_os_pesos)

print("*=" * 20)
print(f"O maior peso é o {pesos.maior()}")
print(f"O menor peso é o {pesos.menor()}")


