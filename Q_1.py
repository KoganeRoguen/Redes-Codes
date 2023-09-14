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

v1, v2, v3 = ler_valor_inteiro('Digite o primeiro valor (quantidade): '), ler_valor_inteiro('Digite o segundo valor (valor mínimo): '), ler_valor_inteiro('Digite o terceiro valor (valor máximo): ')

sucesso, lista_gerada = gerar_lista(v1, v2, v3)

if sucesso:
    print(f'\n Lista gerada: {lista_gerada}')
    
    nome_arquivo = 'valores.txt'
    salvo_com_sucesso = salvar_lista(lista_gerada, nome_arquivo)
    
    if salvo_com_sucesso:
        print('\n === Lista salva com êxito! === \n')
    else:
        print('\n <Erro> Ocorreu um erro ao salvar a lista ')
else:
    print('''
 <Erro> Ocorreu um erro ao gerar a lista.
 Verifique se o valor mínimo não é maior que o valor máximo
 e a quantidade seja um valor positivo
''')
