#anagramas sao palavras que sao construidas com as mesmas letras, mas em ordem diferente

def anagrama(palavra1,palavra2):
    """"
    Verificar se duas palavras sao anagramas
    :param palavra1: primeira palavra
    :param palavra2: segunda palavra
    :return: True se forem anagramas, False caso contrario
    """
    #para retirar os espacos e deixar tudo em minusculo
    palavra1 = palavra1.replace(" ","").lower()
    palavra2 = palavra2.replace(" ","").lower()
   
    if sorted(palavra1) == sorted(palavra2):
        return f"Essas palavras sao anagramas"
    return f"Essas palavras nao sao anagramas"
    
palavra1 = input("Digite a primeira palavra: ")
palavra2 = input("Digite a segunda palavra: ")
resultado = anagrama(palavra1,palavra2)

print(resultado)