# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

pessoas = list()
aux = list()
maiorPeso = menorPeso = 0

resp = 'S'
while resp in ('S', 's', 'sim', 'SIM'):
    aux.append(input('Digite o nome:'))
    aux.append(float(input('Digite o peso:')))
    if aux[1] > maiorPeso:
        maiorPeso = aux[1]
    if menorPeso == 0:
        menorPeso = aux[1]
    elif aux[1] < menorPeso:
        menorPeso = aux[1]
    pessoas.append(aux[:])
    aux.clear()
    resp = input('Deseja continuar? [S/N] ')

print('-='*50)
print(f'Ao todo, você cadastrou {len(pessoas)} pessoa(s).')
print(f'O maior peso foi de {maiorPeso:.1f}Kg. Peso de ', end='')
for pessoa in pessoas:
    if pessoa[1] == maiorPeso:
        print(f'[{pessoa[0]}] ', end='')
print(f'\nO menor peso foi de {menorPeso:.1f}Kg. Peso de ', end='')
for pessoa in pessoas:
    if pessoa[1] == menorPeso:
        print(f'[{pessoa[0]}] ', end='')
