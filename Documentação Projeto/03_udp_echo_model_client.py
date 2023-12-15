import socket,requests
from socket_constants import *

# Atualizar de mensagem do bot por id
def get_last_update_id():
    response = requests.get(f'{strURL}/getUpdates')
    response_json = response.json()
    
    if 'result' in response_json:
        updates = response_json['result']
        if updates:
            return updates[-1]['update_id']
    
    return None

strURL = f'https://api.telegram.org/bot{API}'
last_update_id = get_last_update_id()

updates_response = requests.get(strURL + '/getUpdates').json()
if 'result' in updates_response:
    if updates_response['result']:
        id_chat = updates_response['result'][0]['message']['chat']['id']
    else:
        id_chat = None
else:
    id_chat = None

# Criando o socket UDP
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    if last_update_id is not None:
        updates_response = requests.get(f'{strURL}/getUpdates', params={'offset': last_update_id + 1}).json()
    else:    
        updates_response = requests.get(f'{strURL}/getUpdates').json()
    
    if 'result' in updates_response:
        updates = updates_response['result']
        
        for update in updates:
            # Processar mensagem
            msg = update.get('message')
            if msg:
                chat_id = msg['chat']['id']
                text = msg['text']
            
                # Convertendo a mensagem digitada de string para bytes
                msg_bytes = text.encode(CODE_PAGE)
                # Enviando a mensagem ao servidor
                udp_socket.sendto(msg_bytes, (HOST_SERVER, SOCKET_PORT))
            
                # Recebendo echo do servidor
                dado_recebido, _ = udp_socket.recvfrom(BUFFER_SIZE)
                msg_recebida = dado_recebido.decode(CODE_PAGE)
                dados = {'chat_id': id_chat, 'text': msg_recebida}
                post = requests.post(strURL + '/sendMessage', data=dados)
            
                # Failsafe para não repetir mesma mensagem
                last_update_id = max(last_update_id, update['update_id'])

# Fechando o socket
udp_socket.close()
