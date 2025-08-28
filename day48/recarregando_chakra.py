import time

def recarregando_chakra():
    chakra = 0
    while True:
        yield f"Nivel de chackra: {chakra}"
        chakra += 10
        time.sleep(0.2)
        
gerador = recarregando_chakra()

for _ in range(100):
    print(next(gerador))