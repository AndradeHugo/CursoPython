import time


def contar(inicio, fim, passo):
    print('-=' * 30)
    if passo < 0:
        passo *= -1
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    adicional = 1
    if inicio > fim:
        adicional *= -1
        passo *= -1
    for x in range(inicio, fim + adicional, passo):
        time.sleep(0.5)
        print(f'{x} ', end='', flush=True)
    print('FIM!')


contar(1, 10, 1)
contar(10, 0, 2)
print('-=' * 30)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contar(ini, fim, passo)

