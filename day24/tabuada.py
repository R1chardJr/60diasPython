def tabuada():
    """
    Essa funcao recebe um numero e devolve a  tabuada desse numero
    """
    
    try:
        numero = int(input("Digite o numero para gerar a tabuada: "))
        
        print(f"Tabuada do {numero}:")
        #tabuada de 1 a 11
        for i in range(1, 11):
           resultado = numero * i
           print(f"{numero} x {i} = {resultado}")
    except ValueError:
        print("Entrada Inválida. Digite um numero valido")
        
if __name__ == "__main__":
    tabuada()