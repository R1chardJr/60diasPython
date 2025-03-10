import time

def cronometro_10seg():
    """
    Cronômetro de 10 segundos.
    """
    
    print("Inicializando o cronômetro de 10 segundos...")
    
    tempo = 10
    
    while tempo > 0:
        print(f"Tempo: {tempo} segundos ", end="\r", flush=True)
        time.sleep(1)
        tempo -= 1
    print(f"Tempo: {tempo} segundos ", end="\r", flush=True)
        
    print("\nCronômetro de 10 segundos finalizado!")
    
if __name__ == "__main__":
    cronometro_10seg()