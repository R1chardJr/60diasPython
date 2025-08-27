class ninja:
    def __init__(self,nome,chakra):
        self.nome = nome
        self.chakra = chakra
        
    def usar_jutsu(self,custo_chakra):
        try:
            if custo_chakra > self.chakra:
                raise ValueError("Chakra insuficiente")
            self.chakra -= custo_chakra
            print(f"{self.nome} usou o jutsu com sucesso")
        except ValueError as erro:
            print(f"Erro: {erro} foi detectado. O {self.nome} precisa de mais chakra")
            
if __name__ == "__main__":
    naruto = ninja('Naruto',100)
    
    naruto.usar_jutsu(150)
    
    naruto.usar_jutsu(50)