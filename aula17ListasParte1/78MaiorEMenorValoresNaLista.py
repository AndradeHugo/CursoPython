# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor:')))
print(f'{max(valores)} é o maior e sua posição é a de {valores.index(max(valores))}.')
print(f'{min(valores)} é o menor e sua posição é a de {valores.index(min(valores))}.')
