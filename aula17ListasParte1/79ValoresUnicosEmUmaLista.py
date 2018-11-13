# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado. No final,
# serão exibidos todos os valores únicos digitados, em ordem crescente.

valores = list()

resp = 'S'
while resp in ('S', 's', 'sim'):
    valor = int(input('Digite um valor:'))
    if valor not in valores:
        valores.append(valor)
    resp = input('Deseja continuar? [S/N] ')
print('-='*30)
print(f'Você digitou o(s) valore(s) {sorted(valores)}')
