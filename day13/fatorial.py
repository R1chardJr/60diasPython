def fatorial(n):
    """"
    Calcular o fatorial de um numero usando recursao
    :param n: numero inteiro nn negativo
    :return: fatorial de n
    """
    if n < 0:
        raise ValueError("O numero deve ser positivo")
    
    if n ==0 or n == 1:
        return 1
    
    return n * fatorial(n-1)

numero = 5
try:
    print((f"fatorial de {numero} igual a {fatorial(numero)}"))
except ValueError as e:
    print(e)
    
''''
Customizavel
    
    def tentativa():
        num = int(input("Digite um numero: "))
        try:
            print((f"fatorial de {numero} igual a {fatorial(numero)}"))
        except ValueError:
            print("Entrada invalida,nao se trata de um numero positivo")
            tentativa()

    tentativa()
'''