def transpor_matriz(matriz):
    """
    Gerar uma Matriz transposta
    Args:
        matriz (list): Matriz a ser transposta
    Returns:
        list: Matriz transposta
    Raises:
        ValueError: Se a matriz não for quadrada
    """
    #verifica se a matriz é quadrada
    for i in range(len(matriz)):
        if len(matriz) != len(matriz[i]):
            raise ValueError("A matriz não é quadrada")
    
    #gera a matriz transposta
    transposta = [[matriz[j][i] for j in range(len(matriz))]for i in range(len(matriz))]
    
    return transposta

#teste
matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
transposta = transpor_matriz(matriz)
for linha in transposta:
    print(linha)