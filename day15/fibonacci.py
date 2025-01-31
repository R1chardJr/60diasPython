fibonacci = [0,1]

# 8 primeiros numeros da sequencia de fibonacci
for i in range(8):
    proximonum = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(proximonum)
    

#print(fibonacci)



def Fibonacci(n):
    fib = [0]
    
    if n <= 0:
        raise ValueError("O numero deve ser maior que 0")
    
    if n == 1:
        return fib
    
    while len(fib) < n:
        if len(fib) == 1:
            fib.append(1)
        else:
            fib.append(fib[-1] + fib[-2])
    
    return fib

def tentativa():
    
    try:
        num = int(input("Digite quantos elementos da sequencia de fibonacci deseja: "))
        print(Fibonacci(num))
    except ValueError as e:
        print(e)
        tentativa()
        
tentativa()