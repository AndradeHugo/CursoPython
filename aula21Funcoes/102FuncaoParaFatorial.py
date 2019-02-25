# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a
# calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o
# processo de cálculo do fatorial.


def fatorial(num, mostrarCalculo=False):
    """
    -> Calcula o fatorial de um número.
    :param num: O número a ser calculado.
    :param mostrarCalculo: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número num.
    """
    resp = ''
    fat = 1
    if num > 1:
        for i in range(num, 1, -1):
            fat *= i
            if mostrarCalculo:
                resp = resp + f'{i} x '
                if i == 2:
                    resp += '1 = '
    resp += str(fat)
    return resp


help(fatorial)
print(fatorial(5, True))
print(fatorial(5))


