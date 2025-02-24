def celsius_to_fahrenheit(celsius):
    """
    Converte uma temperatura de Celsius para Fahrenheit.
    Args:
    celisus(float): A temperatura em Celsius    
    return:
    float: A temperatura em Fahrenheit  
    """	
    return round((celsius * 9 / 5) + 32,2)

def fahrenheit_to_celsius(fahrenheit):
    """
    Converte uma temperatura de Fahrenheit para Celsius.
    Args:
    fahrenheit(float): A temperatura em Fahrenheit    
    return:
    float: A temperatura em Celsius  
    """	
    return round((fahrenheit - 32) * 5 / 9,2)

def main(temperatura,tipo_conversao):
    """
    Funcao principal
    Args:
    temperatura(float): A temperatura a ser convertida
    tipo_conversao(str): O tipo de conversao a ser feita
    Returns:
    float: A temperatura convertida
    """
    
    if tipo_conversao == "celsius":
        return celsius_to_fahrenheit(temperatura)
    elif tipo_conversao == "fahrenheit":
        return fahrenheit_to_celsius(temperatura)
    else:
        return print("Tipo de conversao invalido")
    
if __name__ == "__main__":
    print(main(20,"celsius"))
    print(main(20,"fahrenheit"))