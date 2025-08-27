import os

diretorio = "./"

arquivos_pasta = os.listdir(diretorio)
#print(arquivos_pasta)

for arquivo in arquivos_pasta:
    caminho_completo = (os.path.join(diretorio,arquivo))
    if os.path.isfile(caminho_completo):
        print(f"{arquivo} é um arquivo")
    if os.path.isdir(caminho_completo):
        print(f"{arquivo} é um diretório. Seu conteúdo é:")
        print(os.listdir(caminho_completo))