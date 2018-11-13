# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
# cadastrando tudo em uma lista composta.
import time
from random import randint

print('-'*40)
print(f'{"JOGA NA MEGA SENA":^40}')
print('-'*40)
qtdJogos = int(input('Quantos jogos você quer que eu sorteie?'))
print('-=' * 5, f'SORTEANDO {qtdJogos} JOGOS', '-=' * 5)

palpites = [[0,0,0,0,0,0] for i in range(qtdJogos)]
for x in range(0, len(palpites)):
    for y in range(0, len(palpites[x])):
        palpites[x][y] = randint(1, 60)
    time.sleep(0.75)
    print(f'Jogo {x+1}: {palpites[x]}')
print('-=' * 6, '< BOA SORTE! >', '-=' * 6)
