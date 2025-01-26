def podedirigir(idade):
    if idade >= 18:
        return True
    else:
        return False
    
try:
    input_user = int(input("Digite a sua idade: "))
    print(podedirigir(input_user))
except ValueError: # Se o usuário digitar algo que não seja um número inteiro
    print("Entrada inválida. Por favor, digite um número inteiro.")
    