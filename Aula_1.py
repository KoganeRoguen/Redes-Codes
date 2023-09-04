import random
import os
import subprocess

n = int(input('\nDigite o número de elementos que deseja na lista: ')) 
lista = []

while n > 0:
    e = random.randint(1, 1000000)
    lista.append(e)
    n -= 1

print(lista)

file_name = 'Lista_nao_ordenada.txt'
documents_folder = os.path.expanduser('~/Documentos')

if not os.path.exists(documents_folder):
    os.makedirs(documents_folder)

file_path = os.path.join(documents_folder, file_name)

with open(file_path, 'w') as arquivo:
    arquivo.write('\n'.join(map(str, lista)))

if os.path.exists(file_path):
    try:
        if os.name == 'nt':
            subprocess.run(['notepad.exe', file_path])
        else:
            print('<Erro> Sistema operacional não suportado')
    except Exception as e:
        print(f'<Erro> Ocorreu um erro ao abrir o arquivo: {e}')
else:
    print('<Erro> Arquivo não encontrado')