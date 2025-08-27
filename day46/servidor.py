import socket

# Criando o socket do servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "127.0.0.1"
port = 12345

server_socket.bind((host, port))

server_socket.listen(5)
print(f"Servidor esta esperando conexao em {host}:{port}")

while True:
    cliente_socket, addr = server_socket.accept()
    #addr recebe o IP e a porta do cliente
    print(f"Conexao esatablecida com {addr}")
    
    message = cliente_socket.recv(1024).decode()
    print(f"Mensagem recebida do cliente: {message}")
    
    cliente_socket.send("Mensagem recebida com sucesso!".encode())
    cliente_socket.close()
    