class veiculo:
    def __init__(self,marca,modelo,velocidade_maxima):
        self.marca = marca
        self.modelo = modelo
        self.velocidade_maxima = velocidade_maxima
    
    def ligar_motor(self):
        print(f"O motor do {self.modelo} está ligado.")
        
    def acelerar(self):
        print(f"O {self.modelo} está acelerando em uma velocidade ate {self.velocidade_maxima}.")
        
    def ligar_luzes(self):
        print(f"O {self.modelo} da marca {self.marca} ligou as luzes.")
        
        
class carro(veiculo):
    def __init__(self,marca,modelo,velocidade_maxima,portas):
        super().__init__(marca,modelo,velocidade_maxima)
        self.portas = portas
        
    def abrir_portas(self):
        print(f"As {self.portas} portas do {self.modelo} foram abertas.")
    
    
meu_veiculo = veiculo(marca="Ford",modelo="F-150",velocidade_maxima=200)
meu_veiculo.ligar_motor()
meu_veiculo.acelerar()
print("-----------------------------------------------------------")
meu_carro = carro(marca="Chevrolet",modelo="Camaro",velocidade_maxima=250,portas=2)
meu_carro.ligar_motor()
meu_carro.acelerar()
meu_carro.ligar_luzes()
meu_carro.abrir_portas()