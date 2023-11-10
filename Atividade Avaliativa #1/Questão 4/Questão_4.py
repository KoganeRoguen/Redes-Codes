import os
import subprocess
import time

def extract_rar(file_path, output_dir):
    try:
        subprocess.run(['unrar', 'x', '-o+', file_path, output_dir], check=True)
    except subprocess.CalledProcessError as e:
        print(f'<Erro> ocorreu um erro ao executar o arquivo RAR: {e}')

def create_csv_from_text(file_path, output_csv):
    with open(file_path, 'r') as arquivo_texto, open(output_csv, 'w') as arquivo_csv:
        for linha in arquivo_texto:
            campos = linha.split()
            if len(campos) >= 6:
                regiao_sigla = campos[0]
                estado_sigla = campos[1]
                produto = campos[2]
                data_coleta = campos[3]
                valor_venda = campos[4]
                bandeira = campos[5]

                # Escreva os campos separados por vírgulas no arquivo CSV
                arquivo_csv.write(f'{regiao_sigla},{estado_sigla},{produto},{data_coleta},{valor_venda},{bandeira}\n')

def main():
    dir_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_rar_file = os.path.join(os.path.expanduser('~'), 'Downloads', 'serie_historica_anp.rar')
    dir_destino = os.path.join(os.path.expanduser('~'), 'Downloads', 'serie_historica_anp')
    dir_dados_estatisticos = os.path.join(dir_atual, 'dados_estatisticos')

    if not os.path.exists(dir_destino):
        os.mkdir(dir_destino)

    if not os.path.exists(dir_dados_estatisticos):
        os.makedirs(dir_dados_estatisticos)

    while True:
        for arquivo in os.listdir(dir_destino):
            caminho_completo_arquivo = os.path.join(dir_destino, arquivo)

            if arquivo.endswith('.rar'):
                extract_rar(caminho_completo_arquivo, dir_destino)
                os.remove(caminho_completo_arquivo)

            if arquivo.endswith('.txt'):
                arquivo_controle = f'{caminho_completo_arquivo}.processed'
                if not os.path.exists(arquivo_controle):
                    csv_file = os.path.join(dir_dados_estatisticos, 'dados.csv')
                    create_csv_from_text(caminho_completo_arquivo, csv_file)
                    os.remove(caminho_completo_arquivo)

                    with open(arquivo_controle, 'w'):
                        pass

        time.sleep(60)

if __name__ == '__main__':
    main()
