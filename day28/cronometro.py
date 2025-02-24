import time

def cronometro(tempo):
    """
    funcao que cronometra ate um tempo especifico
    """ 
    print("Inicializando o cronometro...")
    
    for segundo in range(tempo + 1):
        print(f"Tempo: {segundo} segundos",end ="\r")  #usamos o "\r" para ir sobreescrevendo a informacao
        time.sleep(1)
        
    print("\nCronometro finalizado!")
    
if __name__ == "__main__":
    cronometro(10)