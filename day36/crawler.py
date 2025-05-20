from bs4 import BeautifulSoup
import requests

def main():
    try:
        
        url = input("Digite a url:") # https://pt.wikipedia.org/wiki/Star_Wars
        response = requests.get(url)
        if response.status_code != 200:
            print('Erro ao acessar a URL!')
        menu_de_opcoes(response)
        return
    except requests.exceptions.RequestException as e:
        print(f'Erro ao acessar a URL: {e}')
        exit()

def menu_de_opcoes(response):
    
    soup = BeautifulSoup(response.text,'html.parser')
    while True:
        print('\nMenu de Opções:')
        print('Escolha uma opção:')
        print('1 - Ver titulo')
        print('2 - Ver paragrafos')
        print('3 - Ver links')
        print('4 - Sair')
    
        opcao = input('Digite sua opção: ').strip()
        
        if opcao == '1':
            title = soup.title.string
            print(f"Titulo: {title} ")
            
        elif opcao == '2':
            paragrafos = soup.find_all('p')
            print(f"\nForam encontrados {len(paragrafos)} parágrafos.\n")
            if len(paragrafos) > 0:
                try:
                    n_paragrafo = int(input('Digite o número do parágrafo que deseja ver: '))
                    if 0 <= n_paragrafo < len(paragrafos):
                        print(f"\nParágrafo {n_paragrafo}:\n{paragrafos[n_paragrafo].text.strip()}\n")
                    else:
                        print('Número de parágrafo fora do intervalo.')
                except ValueError:
                        print('Por favor, digite um número válido.')
                    
        elif opcao == '3':
            links = soup.find_all('a',href=True)
            if len(links) > 0:
                for link in links:
                    print(link['href'])
            else:
                print('Nenhum link encontrado.')
                    
        elif opcao == '4':
            print('Saindo...')
            break
        else:
            print('Opção inválida!')
       
    
if __name__ == '__main__':
    main()

    
        
    
    