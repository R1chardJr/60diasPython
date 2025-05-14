from random import randint

def lancar_dado():
    """
    Simular o lançamento de um dado de 1 a 6.
    
    Returns:
        int: O resultado do lançamento do dado (um número entre 1 e 6).
    """
    
    return randint(1, 6)

if __name__ == "__main__":
    resultado = lancar_dado()
    print(f"O resultado do lançamento do dado foi: {resultado}.")
    