import threading
import time

def tarefa(nome, duracao):
    print(f'Tarefa {nome} iniciada.')
    time.sleep(duracao)
    print(f'Tarefa {nome} concluída após {duracao} segundos.')
    
thead1 = threading.Thread(target=tarefa, args=('tarefa simultanea 1', 3))
thead2 = threading.Thread(target=tarefa, args=('tarefa simultanea 2', 4))

#inicia as threads
thead1.start()
thead2.start()

#aguarda as threads terminarem
thead1.join()
thead2.join()
print('Todas as tarefas concluídas.')

#sem o uso de threads
# tarefa('tarefa 1 sem thread', 3)
# tarefa('tarefa 2 sem thread', 4)