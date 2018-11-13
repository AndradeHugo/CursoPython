# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

valores = list()

resp = 'S'
while resp in ('S', 's', 'sim'):
    valor = int(input('Digite um valor:'))
    valores.append(valor)
    resp = input('Deseja continuar? [S/N] ')
print('-='*30)
print(f'Você digitou {len(valores)} elemento(s).')
print(f'O(s) valore(s) em ordem descrescente é(são) {sorted(valores, reverse=True)}.')
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 NÃO faz parte da lista!')
