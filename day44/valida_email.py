import re

def validar_email(email):
    """
    Valida se o email fornecido é válido.
    args: email (str): O email a ser validado.
    """
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(regex, email):
        print(f"O email '{email}' é válido.")
    else:
        print(f"O email '{email}' é inválido.")
        
# ^ indica o início do texto
# [a-zA-Z0-9._%+-] indica os caracteres permitidos antes do @
# @ é o símbolo obrigatório do e-mail
# +\. obrigatório um ponto após o domínio
# $ final do texto

if __name__ == "__main__":
    email = input("Digite um email para validar: ")
    validar_email(email)