import time

#criando decorator
def medir_tempo_execucao(funcao):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        resultado = funcao(*args, **kwargs)
        end_time = time.time()
        tempo_execucao = end_time - start_time
        print(f"Tempo total de execucao : {tempo_execucao} segundos")
        return resultado
    return wrapper

@medir_tempo_execucao
def tarefa1():
    print("Iniciando tarefa 1...")
    time.sleep(2)  # Simulando uma tarefa demorada
    print("Tarefa 1 concluida!")
    
@medir_tempo_execucao
def tarefa2():
    print("Iniciando tarefa 2...")
    time.sleep(3)  # Simulando uma tarefa demorada
    print("Tarefa 1 concluida!")
    
tarefa1()
tarefa2()