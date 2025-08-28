def numeros_infinitos():
    num = 0
    while True:
        yield num
        num += 1
        
gerador = numeros_infinitos()

for _ in range(100000):
    print(next(gerador))