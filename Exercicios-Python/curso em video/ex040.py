class NotaMedia:
    def __init__(self, nota1, nota2):
        self.nota1= nota1
        self.nota2= nota2
    
    def _media(self):
        media = float((self.nota1 + self.nota2) / 2)
        return media
    
    def aprovado(self):
        nota_media = self._media()
        if nota_media < 5:
            return 'REPROVADO!!'
        elif nota_media >= 5 and nota_media <= 6.9:
            return 'RECUPERAÇÃO!!'
        elif nota_media >= 7:
            return "APROVADO!!" 

try:
    num1 = float(input('Informe a primeira nota: '))
    num2 = float(input('Informe a segunda nota: '))
    resultado = NotaMedia(num1, num2)
    final= resultado._media()
    aprovado = resultado.aprovado()
    print(f'A média entre {num1} e {num2} é igual á: {final}')
    print(f'Você foi {aprovado}')

except ValueError:
    print('Valor informado inválido! Por favor, informe apenas números!')



