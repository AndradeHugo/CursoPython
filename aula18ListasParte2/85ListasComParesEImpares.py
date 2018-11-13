# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única
# que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

lista = [[] for i in range(2)]
for cont in range(0, 7):
    num = int(input(f'Digite o {cont+1}º valor: '))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)
print(f'O(s) valore(s) par(es) digitado(s) foi(foram): {sorted(lista[0])}')
print(f'O(s) valore(s) ímpar(es) digitado(s) foi(foram): {sorted(lista[1])}')
