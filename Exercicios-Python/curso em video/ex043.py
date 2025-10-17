class Imc:
    def __init__(self, altura, peso):
        self.altura = altura
        self.peso = peso
    
    def calculador(self):
        imc= self.peso / (self.altura ** 2)
        return imc
    
    def nivel(self):
        if self.calculador() < 18.5:
            return "Abaixo do Peso!"
        elif self.calculador() < 25:
            return "Peso Ideal!"
        elif self.calculador() < 30:
            return "Sobrepeso!"
        elif self.calculador() < 40:
            return "Obesidade!"
        elif self.calculador() >= 40:
            return "Obesidade Mórbida!"

    

try:

    altura = float(input('Informe a sua altura em METROS: '))
    peso = float(input('Informe o seu peso em KG: '))
    imc = Imc(altura, peso)
    print(f'Seu IMC é de {imc.calculador():.1f}')
    print(f'{imc.nivel()}')

except ValueError:
    print('Valor informado está inválido!')


