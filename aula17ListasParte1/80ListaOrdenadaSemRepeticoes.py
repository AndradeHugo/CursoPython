# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

valores = list()
for cont in range(0, 5):
    valorDigitado = int(input('Digite um valor:'))
    if not valores:
        valores.append(valorDigitado)
    else:
        posicaoFinal = 0
        for posicao, valorLista in enumerate(valores):
            if valorDigitado > valorLista:
                posicaoFinal = posicao + 1
            else:
                break
        valores.insert(posicaoFinal, valorDigitado)
print('-'*30)
print(f'Os valors digitados em ordem foram {valores}.')
