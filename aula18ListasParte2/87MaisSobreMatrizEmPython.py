# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = 0
somaTerceiraColuna = 0
maiorSegundaLinha = 0
for x in range(0, 3):
    for y in range(0, 3):
        matriz[x][y] = (int(input(f'Digite um valor para [{x}, {y}]: ')))
        soma += matriz[x][y]
        if y == 2:
            somaTerceiraColuna += matriz[x][y]
        if x == 1:
            if matriz[x][y] > maiorSegundaLinha:
                maiorSegundaLinha = matriz[x][y]

for x in range(0, 3):
    for y in range(0, 3):
        print(f'[{matriz[x][y]:^5}] ', end='')
    print()

print('-='*40)
print(f'A soma de todos os valores pares digitados é {soma}.')
print(f'A soma dos valores da terceira coluna é {somaTerceiraColuna}.')
print(f'O maior valor da segunda linha é {maiorSegundaLinha}.')