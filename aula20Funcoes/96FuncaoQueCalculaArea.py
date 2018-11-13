# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular
# (largura e comprimento) e mostre a área do terreno.


def calcularArea(b, h):
    print(f'A área do terreno {b:.1f} x {h:.1f} é de {b * h:.1f}m².')


print('Controle de terrenos')
print('-'*20)
base = float(input('LARGURA (m): '))
altura = float(input('COMPRIMENTO (m): '))
calcularArea(base, altura)
