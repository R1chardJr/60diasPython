import requests
from googletrans import Translator


def obter_joke(url):
    resposta = requests.get(url)

    if resposta.status_code != 200:
        print('Erro ao acessar a API')
        return None
        
    data = resposta.json()
    print("EN\nThis is a joke from Chuck Norris:")
    print(data['value'])
        
    tradutor = Translator()
    resultado = tradutor.translate(data['value'], src='en', dest='pt')
    
    print("PT\nEssa é a piada do Chuck Norris:")
    print(resultado.text) 

if __name__ == '__main__':
    url = 'https://api.chucknorris.io/jokes/random'
    obter_joke(url)
