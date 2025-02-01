def contar_palavras(texto):
    """
    Contar palavras em uma string
    :param texto: String de entrada
    :return: Quantidade de palavras
    """
    
    palavras = texto.split()
    
    return len(palavras)

frase = input("Digite uma frase para contar as palavras dela: ")
print(f"essa frase contem {contar_palavras(frase)} palavras") 

#texto.split() separa as palavras de uma string em uma lista separadas por espaço