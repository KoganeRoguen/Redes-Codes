import os, random

def ler_valor_inteiro(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print('\n <Erro> favor, digite um valor inteiro')

def gerar_lista(quantidade, valor_minimo, valor_maximo):
    if valor_minimo > valor_maximo or quantidade <= 0:
        return False, None
    
    lista_gerada = [random.randint(valor_minimo, valor_maximo) for _ in range(quantidade)]
    return True, lista_gerada

def salvar_lista(nome_lista, nome_arquivo):
    try:
        caminho = os.path.join(os.path.expanduser('~'), 'Documents', nome_arquivo)
        with open(caminho, 'w') as arquivo:
            arquivo.writelines(map(lambda x: str(x) + '\n', nome_lista))
        return True
    except Exception as e:
        print(f'\n <Erro> Ocorreu um erro ao salvar a lista: {e}')
        return False