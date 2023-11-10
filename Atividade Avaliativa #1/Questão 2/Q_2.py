from F2 import ler_valor_inteiro, ler_arquivo, ordena_lista, ordena_bubble, ordena_insertion, ordena_selection, ordena_quick

nome_arquivo = input('\nDigite o nome do arquivo a ser lido (valores.txt): ')

sucesso, lista_lida = ler_arquivo(nome_arquivo)

if sucesso:
    print(f'\n Lista lida do arquivo: {lista_lida} \n')
else:
    print('\n <Erro> Não foi possível ler o arquivo ')
    
lista = lista_lida

print('='*50)
print('\nLista original:', lista_lida)

metodo = input('\n Informe o método de ordenação ("BUBBLE", "INSERTION", "SELECTION", "QUICK"): ')

sucesso, lista_ordenada = ordena_lista(lista, metodo)

if sucesso:
    print('\nLista ordenada:', lista_ordenada)
    print('')
else:
    print('\n <Erro> Não foi possível ordenar a lista ')