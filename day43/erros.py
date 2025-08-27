def dividir(numerador,denominador):
    try:
        resultado = numerador / denominador
        print(f"O resultado é {resultado}")
    except ZeroDivisionError:
        print("Não é possível realizar uma divisão por zero")
    except TypeError:
        print("Informe apenas números para realizar a divisão")
    
if __name__ == "__main__":
    dividir(5,0)
    dividir(5,'e')