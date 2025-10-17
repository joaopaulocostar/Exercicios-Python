class VerificaPalindromo:
    def __init__(self, frase):
        self.frase = frase
        fraseMinuscula = frase.lower()
        fraseLimpa = ''.join(c for c in fraseMinuscula if c.isalnum())
        self.frase_limpa = fraseLimpa
        
        
        

    def palindromo(self):
        usuario = self.frase_limpa
        if usuario[:] == usuario[::-1]:
            print(usuario)
            return "Essa frase é um palindromo!"
            
        else:
            print(usuario)
            return "Essa frase NÂO é um palindromo!"
            
        

frase = str(input('Escreva uma frase: '))
palindromo = VerificaPalindromo(frase)
print(palindromo.palindromo())


