import random

def gerador_numeros_aleatorios():
    """
    Gera numero aleatorios imprimindo 10 numeros de 1 a 100
    """
    
    print("Bem vindo ao gerador de numeros aleatorios")
    
    numeros_aleatorios = []
    
    for _ in range (10):
        numero = random.randint(1, 100)
        numeros_aleatorios.append(numero)
        
    print("\nNumeros aleatorios sao:")   
    for i,num in enumerate(numeros_aleatorios,start=1):
        print(f"Numero {i}: {num}")
        
        
if __name__ == "__main__":
    gerador_numeros_aleatorios()
        
        
