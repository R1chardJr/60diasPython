def escrever_arquivo(nome_arquivo,conteudo):
    """
    Escreve o conteudo em um arquivo de texto
    Arg:
    nome_arquivo(str): O nome do arquivo a ser criado ou sobrescrito
    conteudo(str): O texto q vai ser escrito no arquivo
    """	
    with open(nome_arquivo, "a") as arquivo:
        arquivo.write(conteudo)
        
    print(f"O conteudo foi escrito no arquivo :{nome_arquivo}")
    
def ler_arquivo(nome_arquivo):
    """
    Le o conteudo de um arquivo de texto
    Arg:
    nome_arquivo(str): O nome do arquivo a ser lido
    """
    
    try:
        with open(nome_arquivo,'r') as arquivo:
            conteudo = arquivo.read()
        print(f"Conteudo do arquivo:\n {conteudo}")   
    except FileNotFoundError:
        print("O arquivo nao foi encontrado")
    
def main(nome_arquivo,conteudo):
    """
    Funcao principal
    Args:
    nome_arquivo(str): O nome do arquivo a ser criado ou sobrescrito
    conteudo(str): O texto q vai ser escrito no arquivo
    """
    print("Bem vindo ao nosso programa de escrita e leitura")
    
    escrever_arquivo(nome_arquivo,conteudo)
    ler_arquivo(nome_arquivo)
    
if __name__ == "__main__":
    arquivo = "arquivo.txt"
    texto = "Dia 26 do curso ackerdemy do zero ao python"
    
    main(arquivo,texto)