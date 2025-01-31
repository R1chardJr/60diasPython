#Palindromo = se escreve de tras pra frente e de frente pra tras e é a mesma coisa
def is_palindromo(texto):
    """""
    Função que verifica se um texto é um palíndromo
    :param texto: palavra,texto ou num
    :return: uma mensagem indicando se é ou não um palíndromo
    """""
    texto = str(texto).replace(" ", "").lower()
    
    if texto == texto[::-1]:
        return f'{texto} é um palíndromo'
    return f'{texto} não é um palíndromo'

text = input("Digite a palavra para verificar se é palindromo: ")
print(is_palindromo(text))