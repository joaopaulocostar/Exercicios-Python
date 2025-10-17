class calcula:
    def __init__(self, valor):
        self.valor =  valor
    
    def quantidade_parcelas(self, quantidade):
        self.quantidade = quantidade
        vezes = 0
        if quantidade == "1" or quantidade == "1x":
            vezes = 1
        elif quantidade == "2" or quantidade == "2x":
            vezes = 2
        elif quantidade == "3" or quantidade == "3x":
            vezes = 3
        return vezes

    def pagamento_dinheiro(self):
        valor = self.valor
        desconto = valor - (10/100 * valor)
        return desconto
    
    def pagamento_cartao(self, parcelas):
        valor = self.valor
        self.parcelas = parcelas
        parcela_total = self.quantidade_parcelas(parcelas)
        if parcela_total == 1:
            preco = valor - (5/100 * valor)
            return preco
        elif parcela_total == 2:
            preco = valor / 2
            return f"O valor do seu produto de R${valor:.2f} fica 2x R${preco:.2f}"
        elif parcela_total == 3:
            preco = valor + (20/100 * valor)
            parcelado = preco / 3
            return f"O valor do seu produto de R${preco:.2f} fica 3x R${parcelado:.2f}"

try:
    valor = float(input('Informe o valor do produto: R$'))
    forma = str(input('Informe a forma de pagamento: Dinheiro ou Cartão? ')).lower().strip()
    calcular = calcula(valor)
    if forma == "dinheiro":
        pagamento = calcular.pagamento_dinheiro()
    elif forma == "cartao" or forma == "cartão":
        parcela = str(input("Em quantas vezes? 1x, 2x, ou 3x? "))
        pagamento = calcular.pagamento_cartao(parcela)   
    print(f"Resultado: {pagamento}")

except ValueError:
    print('Valor inválido!')


    

