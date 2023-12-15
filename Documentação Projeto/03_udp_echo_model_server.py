import socket
from socket_constants import *
from commands import *

print('Recebendo Mensagens...\n\n')

# Criando o socket UDP
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Ligando o socket a porta
udp_socket.bind((HOST_SERVER, SOCKET_PORT))

while True:
    # Recebendo a mensagem e o endereço do cliente
    msg, client = udp_socket.recvfrom(BUFFER_SIZE)
    print('Conectado por: ', client)
    
    # Processando a mensagem e o endereço do cliente
    try:
        opt = {'/p' : ping(client[0]),
               '/s' : showing_ip_configuration()
               }
        command = opt[msg.decode(CODE_PAGE)]
        msg_return = command
    except Exception as e:
        msg_return = str(e)
        
    # Enviando a resposta de volta para o cliente
    udp_socket.sendto(msg_return.encode(CODE_PAGE), client)

udp_socket.close()
