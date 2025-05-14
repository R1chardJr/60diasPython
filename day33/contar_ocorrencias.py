from collections import Counter

def contar_ocorrencias(lista):
    """
    contar as ocorrências de cada elemento em uma lista
    Arg:
        lista (list): A lista cujos elementos serão contados.
    Return:
        Counter: Um objeto do tipo Counter contendo a contagem de cada elemento na lista.
    """ 
    
    contagem = Counter(lista)
    print("Contagem de ocorrências:")
    for elemento,quantidade in contagem.items():
        print(f"elemento: {elemento} - quantidade: {quantidade}")
        
        
    return f"Contagem realizada com sucesso!"

if __name__ == "__main__":
    lista_exemplo = ["banana", "maçã","uva", "laranja", "banana", "maçã", "banana","uva"]
    print(contar_ocorrencias(lista_exemplo))