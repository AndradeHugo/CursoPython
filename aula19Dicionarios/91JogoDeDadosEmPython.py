# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem,
# sabendo que o vencedor tirou o maior número no dado.


#só pra testes
# jogador1 = {'nome':'jogador1', 'valor':1}
# jogador2 = {'nome':'jogador2', 'valor':4}
# jogador3 = {'nome':'jogador3', 'valor':4}
# jogador4 = {'nome':'jogador4', 'valor':4}
# ranking = list()
# ranking.append(jogador1.copy())
# ranking.append(jogador2.copy())
# ranking.append(jogador3.copy())
# ranking.append(jogador4.copy())
# for j in ranking:
#     print(f'{j["nome"]} tirou {j["valor"]} no dado.')

from random import randint

ranking = list()
jogador = dict()
print('Valores sorteados:')
for c in range(0, 4):
    jogador['nome'] = 'jogador' + str(c + 1)
    jogador['valor'] = randint(1, 6)
    print(f'{jogador["nome"]} tirou {jogador["valor"]} no dado.')
    ranking.append(jogador.copy())
    jogador.clear()

print('-=' * 30)
print(f'{"== RANKING DOS JOGADORES ==":>29}')
cont = 0
pos = 1
while ranking:
    for jog in ranking:
        if jog['valor'] == max(item['valor'] for item in ranking):
            print(f'{pos}º lugar: {jog["nome"]} com {jog["valor"]}')
            ranking.pop(cont)
            pos += 1
        cont += 1
    cont = 0




