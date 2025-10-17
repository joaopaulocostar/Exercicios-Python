from random import choice 
class Jokenpo:
    
    def __init__(self, escolha):
        self.escolha = escolha
        self.opcoes = ["pedra", "papel", "tesoura"]
    
    def vencedor(self):
        escolha_usuario = self.escolha
        escolha_pc = choice(self.opcoes)
        print("-" * 30)
        print(f"Sua escolha é: {escolha_usuario}")
        print(f"O computador escolheu: {escolha_pc}")
        print("-" * 30)

        if escolha_usuario == escolha_pc:
            return "Empate!"
        
        vitoria = {
            "pedra": "tesoura",
            "papel": "pedra",
            "tesoura": "papel"
        }
        if vitoria[self.escolha] == escolha_pc:
            return "Você venceu!"
        
        return "Você perdeu!"

try:  
    print("=-"*30)      
    usuario = str(input("Faça sua escolha [Pedra, Papel ou Tesoura]: ").lower().strip())
    jokenpo = Jokenpo(usuario)
    print(f"{jokenpo.vencedor()}")

except ValueError:
    print('Valor inválido!')




