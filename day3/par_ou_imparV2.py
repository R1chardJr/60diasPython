entrada = input("Digite um numero:")

try:  #tente rodar
    numero = int(entrada)
    if numero % 2 == 0 :
        print("Numero par")
    else:
        print("Numero é impar")
except ValueError:
    print("Essa entrada nao é um numero inteiro")