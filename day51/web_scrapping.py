from bs4 import BeautifulSoup
import requests

url = "http://books.toscrape.com"

response = requests.get(url)

if response.status_code == 200:
    print("Conexao bem sucedida!")
else:
    print("Erro ao conectar:", response.status_code)
    exit()
    
soup = BeautifulSoup(response.text, 'html.parser')

livros = soup.find_all("article",class_="product_pod")

for livro in livros:
    titulo = livro.find("h3").find("a")["title"]
    preco = livro.find("p", class_="price_color")
    estrelas = livro.find("p", class_="star-rating")['class'][1]
    print(f"Título: {titulo} | Preço: {preco.text} | Estrelas: {estrelas}")