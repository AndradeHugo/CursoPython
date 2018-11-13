# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

primeiro = int(input('Digite o primeiro número:'))
segundo = int(input('Digite o segundo número:'))
terceiro = int(input('Digite o terceiro número:'))
quarto = int(input('Digite o quarto número:'))

numeros = (primeiro, segundo, terceiro, quarto)

print(f'O número 9 apareceu {numeros.count(9)} vez(es).')
print(f'A primeira posição do número 3 é a posição de número {numeros.index(3)+1}.')
print('O(s) número(s) pare(s) é(são) { ', end='')
for x in numeros:
    if x % 2 == 0:
        print(f'{x} ', end='')
print('}')


