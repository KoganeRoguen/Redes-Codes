import socket, os

def download_image(url):
    # Adiciona "http://" à URL se não estiver presente
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "http://" + url

    # Extrair o host e o caminho da URL
    url_parts = url.split('/')
    url_host = url_parts[2]
    url_path = '/' + '/'.join(url_parts[3:])

    # Remover informações extras não referentes à URL da imagem
    url_path = url_path.split('?')[0]

    # Configurações do socket
    HOST_PORT = 80
    BUFFER_SIZE = 4096

    try:
        # Conectar ao servidor remoto
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_img:
            sock_img.connect((url_host, HOST_PORT))
            request = f'GET {url_path} HTTP/1.1\r\nHost: {url_host}\r\nConnection: close\r\n\r\n'
            sock_img.sendall(request.encode())

            print('\nBaixando a imagem...')

            # Montar a variável que armazenará os dados de retorno
            data_ret = b''

            while True:
                data = sock_img.recv(BUFFER_SIZE)
                if not data:
                    break
                data_ret += data

        # Obter o tamanho da imagem
        size_index = data_ret.find(b'Content-Length:')
        if size_index != -1:
            end_index = data_ret.find(b'\r\n', size_index)
            img_size = int(data_ret[size_index + len('Content-Length:'):end_index].strip())
            print(f'\nTamanho da Imagem: {img_size} bytes')

        # Separar o cabeçalho dos dados
        delimiter = b'\r\n\r\n'
        position = data_ret.find(delimiter)
        headers = data_ret[:position]
        image = data_ret[position + 4:]

        # Extrair o nome do arquivo do caminho da URL
        file_name = os.path.basename(url_path)

        # Remover caracteres inválidos do nome do arquivo
        file_name = ''.join(c for c in file_name if c.isalnum() or c in ['.', '-'])

        with open(file_name, 'wb') as file_output:
            file_output.write(image)

        print(f'Imagem salva como: {file_name}')

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Solicitar URL ao usuário
url = input("Digite a URL completa da imagem: ")
download_image(url)
