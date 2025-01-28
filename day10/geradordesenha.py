import random
import string

def gerador_de_senha(tamanho):
    comprimento = tamanho
    caracteres = string.ascii_letters + string.digits + string.punctuation
    
    senha = ''
    
    while len(senha) < comprimento:
        senha += random.choice(caracteres)
        
    print(f"Sua senha ficou assim: {senha}\n")
    
gerador_de_senha(10) #gera uma senha de 10 caracteres