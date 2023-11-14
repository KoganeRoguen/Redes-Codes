import os,json,struct,requests

def extrair_info_exif(arquivo):
    with open(arquivo, 'rb') as f:
        # Lê os primeiros 2 bytes
        marker = f.read(2)

        # Enquanto houver segmentos
        while marker:
            if marker == b'\xFF\xE1':
                # Encontrou um segmento APP1 (EXIF)
                # Lê o tamanho do segmento
                tamanho_segmento = struct.unpack('>H', f.read(2))[0]

                # Lê 'Exif\0\0'
                exif_header = f.read(6)

                # Verifica se é um segmento EXIF
                if exif_header == b'Exif\0\0':
                    # Lê os dados EXIF
                    dados_exif = f.read(tamanho_segmento - 8)

                    # Lê a quantidade de metadados
                    num_metadados = struct.unpack('>H', dados_exif[16:18])[0]

                    # Pula para a posição dos metadados
                    posicao_metadados = 20
                    latitude, longitude = None, None

                    for _ in range(num_metadados):
                        id_metadado = struct.unpack('>H', dados_exif[posicao_metadados:posicao_metadados + 2])[0]
                        posicao_metadados += 2

                        tipo_metadado = struct.unpack('>H', dados_exif[posicao_metadados:posicao_metadados + 2])[0]
                        posicao_metadados += 2

                        num_repeticoes = struct.unpack('>I', dados_exif[posicao_metadados:posicao_metadados + 4])[0]
                        posicao_metadados += 4

                        valor_metadado = struct.unpack('>I', dados_exif[posicao_metadados:posicao_metadados + 4])[0]
                        posicao_metadados += 4

                        if tipo_metadado == 4 and num_repeticoes > 1:
                            valor_metadado += 12

                        if id_metadado == 0x8825:  # Identificador para informações de GPS
                            if valor_metadado != 0:
                                latitude = struct.unpack('>I', dados_exif[valor_metadado:valor_metadado + 4])[0]
                                longitude = struct.unpack('>I', dados_exif[valor_metadado + 4:valor_metadado + 8])[0]

                    return latitude, longitude

    return None, None

def obter_informacoes_locais(diretorio):
    arquivos = [arquivo for arquivo in os.listdir(diretorio) if arquivo.lower().endswith('.jpg')]

    for arquivo in arquivos:
        caminho_arquivo = os.path.join(diretorio, arquivo)
        latitude, longitude = extrair_info_exif(caminho_arquivo)

        if latitude is not None and longitude is not None:
            print(f'Arquivo: {arquivo}')
            print(f'Latitude: {latitude}')
            print(f'Longitude: {longitude}')

            # Obtenha informações do local usando a API Nominatim
            req_url = f'https://nominatim.openstreetmap.org/reverse?lat={latitude}&lon={longitude}&format=json'
            req = requests.get(req_url)
            str_local = req.text

            # Converta a resposta para JSON usando apenas o módulo json
            local_info = json.loads(str_local)

            print('Informações do Local:')
            print(f'Endereço: {local_info.get("display_name", "N/A")}')
            print(f'CEP: {local_info.get("address", {}).get("postcode", "N/A")}')
            print()

if __name__ == "__main__":
    diretorio = input("Digite o nome do diretório: ")
    obter_informacoes_locais(diretorio)