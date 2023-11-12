import socket,sys,os

def criarList():
    try:
        here = os.path.dirname(os.path.abspath(__file__))
        caminho = os.path.join(here, 'pingas.csv')
        with open(caminho, 'r', encoding='latin-1') as file:
            conteudo = file.read()
            my_list = conteudo.split('\n')[1:]
            my_list = [item for item in my_list if item]
    except Exception as e:
        print(f'<Erro> {e}')
    else:
        return my_list

def checar_ports():
    strHost = 'www.ifrn.edu.br'
    ipHost = socket.gethostbyname(strHost)
    port_list = criarList()

    if port_list is None:
        print('<Erro> lista não foi criada. verifique o erro acima')
        return
    
    for port_info in port_list:
        item = port_info.split(';')
        port = int(item[0].strip('\ufeff'))
        proto = item[1]
        desc = item[2]
        sock = socket.socket(family= socket.AF_INET, type= socket.SOCK_STREAM)
        sock.settimeout(3)
        try:
            conn = sock.connect_ex((ipHost, port))
            if conn == 0:
                stat = 'aberto'
            else:
                stat = 'fechado'
        except Exception as e:
            print(f'<Erro> {port} ------{e}')
        else:
            print(f'Porta: {port} | Protocolo: {proto} | Desc: {desc} | {stat}')
            sock.close()

if __name__ == '__main__':
    checar_ports()