import math

def raiz_quadrada(numero):
    """
    Calcula a raiz quadrada de um número.
    
    Args:
        numero (float): O número do qual se deseja calcular a raiz quadrada.
    
    Returns:
        float: A raiz quadrada do número.
    """
    if numero < 0:
        raise ValueError("Não é possível calcular a raiz quadrada de um número negativo.")
    
    return round(math.sqrt(numero),2)

if __name__ == "__main__":
    numero = float(input("Digite um número para calcular a raiz quadrada: "))
    try:
        resultado = raiz_quadrada(numero)
        print(f"A raiz quadrada de {numero} é {resultado}.")
    except ValueError as e:
        print(e)