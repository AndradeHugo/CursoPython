# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário,
# incluindo o total de gols feitos durante o campeonato.

dados = dict()
dados['nome'] = input('Nome do Jogador: ')
qtdPartidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
gols = list()
for x in range(0, qtdPartidas):
    gols.append(int(input(f'   Quantos gols na partida {x+1}? ')))
dados['gols'] = gols
dados['total'] = sum(gols)

print('-=' * 30)
print(dados)
print('-=' * 30)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {dados["nome"]} jogou {len(dados["gols"])} partida(s).')
cont = 1
for x in gols:
    print(f'    => Na partida {cont}, fez {x} gol(s).')
    cont += 1
print(f'Foi um total de {sum(gols)} gols.')
