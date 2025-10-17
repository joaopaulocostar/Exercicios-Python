class financiamento:

    def __init__(self, valor_casa, salario,  anos):
        self.valor_casa = valor_casa
        self.anos = anos
        self.salario = salario
        self.mensalidade = anos * 12

    

    def calcular(self):
        prestacao_mensal = self.valor_casa / self.mensalidade
        percentual = 30/100 * self.salario
        if prestacao_mensal <= percentual:
            print(f'Financiamento aprovando!! Sua mensalidade é de R${prestacao_mensal:.2f} em {self.mensalidade} vezes.')
        else:
            print('Financiamento negado!! O valor mensal ultrapassou o limite da renda mensal')


valor_imovel = float(input('Informe o valor do Imóvel em R$: '))
salario_mensal = float(input('Informe o salário mensal em R$: '))
tempo = int(input('Informe o tempo de pagamento em Anos: '))

financiando = financiamento(valor_imovel, salario_mensal, tempo)
financiando.calcular()



