import socket,os

def download_image(url):
    try:
        # Dividindo a URL para obter informações relevantes
        url_parts = url.split('/')
        url_parts = list(filter(None, url_parts)) # Remove elementos vazios
    
        url_host = url_parts[1]
        url_image = '/'.join(url_parts[2:]).split('?')[0]
    
        # Atualizando a extensão do arquivo para PNG
        url_image = os.path.splitext(url_image)[0] + '.png'
        
        # Criando a requisição HTTP
        url_request = f'GET {url_image} HTTP/1.1\r\nHost: {url_host}\r\nConnection: close\r\n\r\n'
    
        HOST_PORT = 80
        BUFFER_SIZE = 4096
    
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_img:
            sock_img.connect((url_host, HOST_PORT))
            sock_img.sendall(url_request.encode())
        
            print('\n<Download> a imagem está sendo baixada...')
        
            # Montando a variável que armazenará os dados de retorno
            data_ret = b''
        
            while True:
                data = sock_img.recv(BUFFER_SIZE)
                if not data:
                    break
                data_ret += data
            
        # Obtendo o tamanho da imagem
        img_size = -1
        tmp = data_ret.split(b'\r\n')
        for line in tmp:
            if b'Content-Length:' in line:
                img_size = int(line.split()[1])
                break
        
        print(f'Tamanho da Imagem: {img_size} bytes')
    
        # Separando o cabeçalho dos dados
        delimiter = b'\r\n\r\n'
        position = data_ret.find(delimiter)
        headers = data_ret[:position]
        image = data_ret[position + 4:]
        
        # Criando o diretório se não existir
        directory = os.path.dirname(url_image)
        if not os.path.exists(directory):
            os.makedirs(directory)
        
        # Salvando a imagem
        with open(url_image, 'wb') as file_output:
            file_output.write(image)
        
        print(f'Imagem salva como: {url_image}')
    
    except Exception as e:
        print(f'<Erro> ocorreu um erro durante a execução: {e}')
        
# Solicita a URL da imagem ao usuário
url = input('Digite a URL completa da imagem: ')
download_image(url)