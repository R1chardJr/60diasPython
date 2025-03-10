from datetime import datetime

#pip install pytz para poder rodar
import pytz

def exibir_data_hora_atual():
    """
    Função para exibir a data e hora atual
    """
    fuso_horario = pytz.timezone('America/Sao_Paulo')
    
    data_hora = datetime.now(fuso_horario)
    
    formato_data_hora = data_hora.strftime('%d/%m/%Y %H:%M:%S')
    
    print(f'Data e hora atual: {formato_data_hora}')
    
if __name__ == '__main__':
    exibir_data_hora_atual()
    
    