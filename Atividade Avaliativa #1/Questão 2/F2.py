import os

def ler_valor_inteiro(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print('\n <Erro> favor, digite um valor inteiro')

def ler_arquivo(nome_arquivo):
    try:
        caminho = os.path.join(os.path.expanduser('~'), 'Documents', nome_arquivo)
        with open(caminho, 'r') as arquivo:
            linhas = arquivo.readlines()
            lista_gerada = [int(linha.strip()) for linha in linhas]
            return True, lista_gerada
    except FileNotFoundError:
        print(f'\n <Erro> O arquivo "{nome_arquivo}" não foi encontrado.')
        return False, None
    except Exception as e:
        print(f'\n <Erro> Ocorreu um erro ao ler o arquivo: {e}')
        return False, None

def ordena_lista(nome_lista, metodo_ordenado):
    if metodo_ordenado == 'BUBBLE':
        sucesso, lista_ordenada = ordena_bubble(nome_lista)
        return sucesso, lista_ordenada
    elif metodo_ordenado == 'INSERTION':
        sucesso, lista_ordenada = ordena_insertion(nome_lista)
        return sucesso, lista_ordenada
    elif metodo_ordenado == 'SELECTION':
        sucesso, lista_ordenada = ordena_selection(nome_lista)
        return sucesso, lista_ordenada
    elif metodo_ordenado == 'QUICK':
        sucesso, lista_ordenada = ordena_quick(nome_lista)
        return sucesso, lista_ordenada
    else:
        print('\n <Erro> o método de ordenação é inválido, utilize "ascendente" ou "descendente" ')
        return False, None
    
def ordena_bubble(lista):
    n = len(lista)
    for r in range(n - 1):
        for j in range(0, n - r - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return True, lista            
 
def ordena_insertion(lista):
    n = len(lista)
    for r in range(1, n):
        key = lista[r]
        j = r - 1
        while j >= 0 and key < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = key
    return True, lista    
        
def ordena_selection(lista):
    n = len(lista)
    for r in range(n):
        min_index = r
        for j in range(r + 1, n):
            if lista[j] < lista[min_index]:
                min_index = j
        lista[r], lista[min_index] = lista[min_index], lista[r]
    return True, lista
             
def ordena_quick(lista):
    if len(lista) <= 1:
        return True, lista
    else:
        pivot = lista[0]
        less = [x for x in lista[1:] if x <= pivot]
        greater = [x for x in lista[1:] if x > pivot]
        return True, ordena_quick(less)[1] + [pivot] + ordena_quick(greater)[1]