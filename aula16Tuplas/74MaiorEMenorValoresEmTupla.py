# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint

primeiro = randint(0, 100)
segundo = randint(0, 100)
terceiro = randint(0, 100)
quarto = randint(0, 100)
cinco = randint(0, 100)

numeros = (primeiro, segundo, terceiro, quarto, cinco)
print(f'Listagem de números sorteados: {numeros}')
print(f'O maior número da lista é {max(numeros)}')
print(f'O menor número da lista é {min(numeros)}')



