import json
from typing import Any

def salvar_dados(arquivo:str, dados: Any) -> None:
    """
    Salvar os dados em um arquivo JSON
    
    :param: arquivo: caminho para o arquivo JSON
    :param: dados: dados a serem armazenados
    """
    
    with open(arquivo, 'w', encoding='utf-8') as f:
        json.dump(dados,f, indent=4, ensure_ascii=False)
        
def carregar_dados(arquivo:str) -> Any:
    """
    Ler os dados de um arquivo JSON

    Args:
        arquivo: caminho para o arquivo JSON

    Returns:
        Any: Dados carregados e lidos do arquivo JSON
    """
    
    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Arquivo '{arquivo}' não encontrado.")
        return {}
    


if __name__ == "__main__":
    nome_arquivo = "exemplo.json"
    dados_exemplo = {
    "nome": "Richard",
    "idade": 22,
    "cidade": "São José dos Campos",
    "interesses": ["programação", "IA", "Machines Learning"],
    }

    salvar_dados(nome_arquivo, dados_exemplo)

    dados_carregados = carregar_dados(nome_arquivo)