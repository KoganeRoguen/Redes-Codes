import socket, subprocess
from socket_constants import *

print('Recebendo Mensagens...\n\n')

def execute_command(command):
    try:
        resultado = subprocess.run(command, shell=True, capture_output=True, text=True)
        return resultado.stdout
    except Exception as e:
        return str(e)

# Criando o socket UDP
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Ligando o socket à porta
udp_socket.bind((HOST_SERVER, SOCKET_PORT))

while True:
    # Recebendo a mensagem e o endereço do cliente
    data, cliente = udp_socket.recvfrom(BUFFER_SIZE)
    mensagem = data.decode(CODE_PAGE)
    print('Conectado por: ', cliente)
    print('Mensagem recebida: ', mensagem)
    
    # Devolvendo uma mensagem (echo) ao cliente
    mensagem_retorno = execute_command(mensagem)
    udp_socket.sendto(mensagem_retorno.encode(CODE_PAGE), cliente)

    print('Finalizando Conexão do Cliente ', cliente)

udp_socket.close()