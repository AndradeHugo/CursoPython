# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso,
# crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
# respectivamente. Ao final, mostre o conteúdo das três listas geradas.

valores = list()

resp = 'S'
while resp in ('S', 's', 'sim'):
    valor = int(input('Digite um valor:'))
    valores.append(valor)
    resp = input('Deseja continuar? [S/N] ')

pares = list()
impares = list()
for valor in valores:
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)
print('-='*30)
print(f'A lista completa é {valores}.')
print(f'A lista dos pares é {pares}.')
print(f'A lista dos ímpares é {impares}.')
