import random

def jogo_advinhacao():
    """	
    Um jogo onde o usuário deve adivinhar um número aleatorio.
    """
    
    print("Bem vindo ao jogo de adivinhação!")
    
    numero_secreto = random.randint(0,10)
    
    tentativas = 0
    
    while True:
        try:
            palpite = int(input("Digite seu palpite: "))
            tentativas += 1
            
            if palpite > numero_secreto:
                print("O número secreto é menor.")
            elif palpite < numero_secreto:
                print("O número secreto é maior.")
            else:
                print(f"Parabéns! Você acertou o número secreto em {tentativas} tentativas.")
                break
        except ValueError:
            print("Por favor, digite um numero valido")
            
if __name__ == "__main__":
    jogo_advinhacao()