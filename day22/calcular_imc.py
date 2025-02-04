def calcular_imc():
    """
    Calcula o IMC (Índice de Massa Corporal) de uma pessoa.
    """
    print("Bem vindo a calculadora de IMC!")
    
    try:
        peso = float(input("Digite seu peso (em kg): "))
        altura = float(input("Digite sua altura (em metros): "))
        
        if peso <= 0 or altura <= 0:
            print("Peso e altura devem ser maiores que 0")
            return calcular_imc()

        imc = round(peso / altura ** 2,2)
        
        if imc < 18.5:
            print(f"Seu IMC é {imc} e você está abaixo do peso ideal.")
        elif 18.5 <= imc < 25:
            print(f"Seu IMC é {imc} e você está no peso ideal.")
        elif 25 <= imc < 29.9:
            print(f"Seu IMC é {imc} e você está com sobrepeso.")
        else:
            print(f"Seu IMC é {imc} e você está com obesidade.")
        
    except ValueError:
        print("A entrada esta errada, digite apenas numeros.")
        return calcular_imc()
    
    # # Outra forma de fazer a classificação do IMC, mais compacta
    # classificacao = (
    #     "abaixo do peso" if imc < 18.5 else
    #     "no peso ideal" if imc < 25 else
    #     "com sobrepeso" if imc < 29.9 else
    #     "com obesidade"
    # )

    # print(f"Seu IMC é {imc} e você está {classificacao}.")

#significa que o código só será executado se o arquivo for executado diretamente
if __name__ == "__main__":
    calcular_imc()