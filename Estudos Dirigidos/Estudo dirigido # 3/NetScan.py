import socket,sys,os

def criar_lista():
    try:
        here = os.path.dirname(os.path.abspath(__file__))
        caminho_arq = os.path.join(here, 'pingas.csv')
        with open(caminho_arq, 'r', encoding='iso-8859-1') as arq:
            conteudo_arq = arq.read()
        list_data = conteudo_arq.split('\n')
        list_data = [linha.strip() for linha in list_data if linha.strip()]
    except Exception as e:
        print(f'<Erro> {e}')
        sys.exit(1)
    else:
        return list_data

def verify_portas(host):
    list_data = criar_lista()

    for n in list_data[1:]:
        item = n.split(';')
        
        try:
            porta = int(item[0].strip('\ufeff'))
        except ValueError:
            print(f'Ignorando linha inválida: {item}')
            continue
        
        protocolo = item[1]
        descricao = item[2]

        sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        sock.settimeout(3)
        
        try:
            conn = sock.connect_ex((host, porta))
            if conn == 0:
                stat = 'Aberto'
            else:
                stat = 'Fechado'
        except Exception as e:
            print(f'<Erro> {porta} ------{e}')
        else:
            print(f'Porta {porta} | Protocolo: {protocolo} | ({descricao}) | Status: {stat}')
        finally:
            sock.close()
        
if __name__ == '__main__':
    str_host = input('Digite a URL: ')
        
    try:
        host_ip = socket.gethostbyname(str_host)
    except socket.gaierror:
        print(f'<Erro> não foi possível resolver o host {str_host}')
        sys.exit(1)
            
    verify_portas(host_ip)
