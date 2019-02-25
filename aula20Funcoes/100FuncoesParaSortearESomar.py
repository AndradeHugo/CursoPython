# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função
# vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores
# pares sorteados pela função anterior.
import time
from random import randint


def sortearValores():
    lista = list()
    print('Sorteando 5 valores da lista: ', end='', flush=True)
    for i in range(0, 5):
        val = randint(0, 9)
        lista.append(val)
        time.sleep(0.5)
        print(f'{val} ', end='', flush=True)
    print('PRONTO!', flush=True)
    return lista


def somaPar(lista):
    soma = 0
    for x in lista:
        if x % 2 == 0:
            soma += x
    print(f'Somando os valores pares de {lista}, temos {soma}', flush=True)


somaPar(sortearValores())
