def analisarValores(* num):
    print('-=' * 30)
    print('Analisando os valores passados...')
    for x in num:
        print(f'{x} ', end='')
    print(f'Foi(ram) informado(s) {len(num)} valor(es) ao todo.')
    if len(num) > 0:
        print(f'O maior valor informado foi {max(num)}.')
    else:
        print('Não foi informado nenhum valor, logo não existe o maior número.')


analisarValores(2, 9, 4, 5, 7, 1)
analisarValores(4, 7, 0)
analisarValores(1, 2)
analisarValores()

