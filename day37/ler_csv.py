import pandas as pd

def main():
    nome_arquivo = 'test.csv'
    
    df = pd.read_csv(nome_arquivo)
    
    print(df)
    
    print(f"Colunas:{df.columns}")
    
    print("Informações do DataFrame:")
    print(df.info())
    
    print("Shape do DataFrame:")
    print(df.shape)
    
if __name__ == '__main__':
    main()