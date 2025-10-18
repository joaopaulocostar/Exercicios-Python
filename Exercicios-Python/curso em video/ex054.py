from datetime import datetime

class maioridade:
    def __init__(self, nascimento):
        self.nascimento = nascimento
        ano_atual = datetime.today()
        somente_ano = ano_atual.year
        self.somente_ano = somente_ano

    def coleta_ano(self):
        hoje = self.somente_ano
        nascimento_usuario = self.nascimento
        total = 0
        for c in (nascimento_usuario):
            if hoje - c < 18:
                total += 1
        return total

todos_usuarios = []
for c in range(0, 8):
    usuario = int(input("Informe um ano de nascimento: "))
    todos_usuarios.append(usuario)

calculador = maioridade(todos_usuarios)
print(f"Há um total de {calculador.coleta_ano()} pessoas menores de idade!")




            
