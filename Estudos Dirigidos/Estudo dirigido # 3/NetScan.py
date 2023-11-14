import socket
import os

pingas = os.path.join(os.path.expanduser('~'), 'Downloads', 'pingas.csv')

def verifica_portas(host):
    with open(pingas, 'r') as file:
        next(file)
        
        for linha in file:
            try:
                porta, protocolo, descricao, status_resposta = linha.strip().split(';')
            except ValueError:
                print(f'<Erro> ocorreu um erro ao processar a linha: {linha}')
                continue
            
            portas = [int(p.strip()) for p in porta.split(',')]
            
            for p in portas:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM if protocolo == 'TCP' else socket.SOCK_DGRAM)
                sock.settimeout(1)
                resultado = sock.connect_ex((host, p))
                sock.close()
                
                status_resposta_porta = 'Responde (Aberta)' if resultado == 0 else 'Não responde (Fechada)'
                
                print(f'Porta: {p} | Protocolo: {protocolo} | ({descricao})/ Status: {status_resposta_porta}')
            
            print(f'Porta: {porta} | Protocolo: {protocolo} | ({descricao})/ Status: {status_resposta_porta}')

if __name__ == '__main__':
    host_alvo = input('Informe o HOST a ser testado: ')
    verifica_portas(host_alvo)