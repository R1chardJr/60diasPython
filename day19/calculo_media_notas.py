def calcular_media_notas(notas):
    """
    Calcular a medida das notas   
    :param notas: lista de notas
    :return: float da media das notas
    """
    media = sum(notas) / len(notas)
    #arredonda nossa media em duas casas decimais
    return round(media,2)

notas = input("Digite as notas separadas por espaço: ")
notas = notas.split()
notas = [float(nota) for nota in notas]
media = calcular_media_notas(notas)
print(f"A media das notas é: {media}")