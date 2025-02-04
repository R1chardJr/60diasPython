def converte_moeda(valor,taxa_cambio,tipo_conversao):
    """
    Essa funcao converte um valor de real para dolar e vice-versa.
    Args:
        valor: (float) valor a ser convertido
        taxa_cambio: a taxa de cambio atual
        conversao: dolar para real ou real para dolar
    Returns:
        float: valor convertido, arredondado para 2 casas decimais
    Raises:
        ValueError: se a conversao for errado
    """
    if tipo_conversao == 'dolar_real':
        return round(valor * taxa_cambio,2)
    elif tipo_conversao == 'real_dolar':
        return round(valor / taxa_cambio,2)
    else:
        return ValueError('Tipo de conversao invalido')
    
print(converte_moeda(12,6.1,'real_dolar')) 