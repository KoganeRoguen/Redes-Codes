from F1 import ler_valor_inteiro, gerar_lista, salvar_lista

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
