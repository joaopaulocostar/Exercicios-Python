class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def se_for_triangulo(self):
        if self.lado1 + self.lado2 > self.lado3 and self.lado1 + self.lado3 > self.lado2 and self.lado2 + self.lado3 > self.lado1:
            return "É possivel formar um Triangulo!"
        else:
            return "Não é possível formar uma triangulo!"
    
    def tipo_de_triangulo(self):
        if self.se_for_triangulo() == "É possivel formar um Triangulo!":
            if self.lado1 == self.lado2 == self.lado3:
                return "Você pode formar uma triângulo EQUILÁTERO!"
            elif self.lado1 != self.lado2 != self.lado3 != self.lado1:
                return "Você pode formar um triângulo ESCALENO!"
            else:
                return "Você pode formar um trângulo ISÓSCELES!"
        else:
            return "Tente outros valores!"
        
try:         
    lado1= float(input("Informe o valor do primeiro lado: "))
    lado2= float(input('Informe o valor do segundo lado: '))
    lado3= float(input('Informe o valor do terceiro lado: '))
    triangulo = Triangulo(lado1, lado2, lado3)
    tipo = triangulo.tipo_de_triangulo()
    resultado = triangulo.se_for_triangulo()
    print(f'{resultado}')
    print(f'{tipo}')

except ValueError:
    print('Valor informado é Inválido!')





