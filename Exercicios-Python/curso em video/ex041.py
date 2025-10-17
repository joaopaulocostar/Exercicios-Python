from datetime import datetime
class Categoria:

    def __init__(self, ano):
        self.ano = ano
    
    def _calculadora_idade(self):
        hoje = datetime.today()
        ano = hoje.year
        idade =  ano - self.ano
        return idade
    
    def categoria_natacao(self):
        idade_final = self._calculadora_idade()
        if idade_final <= 9:
            return 'MIRIM'
        elif idade_final > 9 and idade_final <= 14:
            return 'INFANTIL'
        elif idade_final > 14 and idade_final <= 19:
            return 'JUNIOR'
        elif idade_final == 20:
            return 'SÊNIOR'
        else:
            return 'MASTER'
try:
    idade = int(input('Qual o seu ano de nascimento? '))
    resultado = Categoria(idade)
    anos = resultado._calculadora_idade()
    print(f'Você possui {anos} anos!')
    categoria = resultado.categoria_natacao()
    print(f'Sua categoria é {categoria}!')

except ValueError:
    print('Valor informado inválido! Informe o ano de nascimento corretamente!')


