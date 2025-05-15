#funcao que conta de 0 até um número digitado pelo usuário
def contador_personalizado():
    try:
        limite = int(input("Digite o valor máximo do contador: "))
        for i in range(limite + 1):
            print(i)
            if i == limite:
                print("Fim do contador")
    except ValueError:
        print("Voce diigitou um valor inválido.Por favor, digite um número inteiro.")
        contador_personalizado()
   
contador_personalizado()