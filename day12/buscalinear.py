def busca_linear(lista,num_procurado):
    """"
    Procurar um numero dentro de uma lista utilizando busca linear
    :param lista: lista de numeros
    :param num_procurado: numero a ser procurado
    """
    
    # func nativa do python enumerate
    for i,numero in enumerate(lista):  #enumerate passa por cada item dentro de uma lista enquanto contabiliza
        if numero == num_procurado:
            return i
    return -1 #caso o numero nao seja encontrado

lista_exemplo = [10,2,4,6,7,8,11]
numero_procurado = 8

buscando_numero = busca_linear(lista_exemplo,numero_procurado)
if buscando_numero != -1:
    print(f"O numero {numero_procurado} foi encontrado na posicao {buscando_numero}")
else:
    print(f"O numero {numero_procurado} nao foi encontrado na lista")   
    