class PersonagemNaruto:
    def __init__(self,nome,poder,nivel,qtde_chakra = 10):
        """
        Inicializa um personagem do Naruto com nome, poder e elemento.
        """	
        self.nome = nome
        self.poder = poder
        self.nivel = nivel
        self.qtde_chakra = qtde_chakra
        
    def exibir_informacoes(self):
        """
        Exibe as informações do personagem.
        """
        print(f"Nome: {self.nome}")
        print(f"Poder: {self.poder}")
        print(f"Nivel: {self.nivel}")
        print(f"Quantidade de chakra: {self.qtde_chakra}")
        
    def treinar(self,horas):
        """
        Treina o personagem por um número de horas.
        """        
        aumento = horas * 10
        self.qtde_chakra += aumento
        print(f"{self.nome} treinou por {horas} horas e aumentou seu nível em {aumento} pontos.")
        
    def transformar(self,novo_nivel):
        """
        Transforma o personagem para um novo nível.
        """
        self.nivel = novo_nivel
        print(f"{self.nome} se transformou para o nível {self.nivel}.")
        
Naruto = PersonagemNaruto("Naruto", "Rasengan", "chunin",100)
Naruto.exibir_informacoes()
Naruto.treinar(5)
Naruto.transformar("jounin")
Naruto.exibir_informacoes()