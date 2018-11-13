# Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização
# de detalhes do aproveitamento de cada jogador.

dadosJogador = dict()
jogadores = list()
resp = 'S'
while resp in 'Ss':
    dadosJogador['nome'] = input('Nome do Jogador: ')
    qtdPartidas = int(input(f'Quantas partidas {dadosJogador["nome"]} jogou? '))
    gols = list()
    for x in range(0, qtdPartidas):
        gols.append(int(input(f'   Quantos gols na partida {x+1}? ')))
    dadosJogador['gols'] = gols
    dadosJogador['total'] = sum(gols)
    jogadores.append(dadosJogador.copy())
    resp = input('Deseja continuar? [S/N] ')
print('-=' * 30)

print('cod ', f'{"nome":<12}', f'{"gols":<18}', f'{"total":<12}')
print('-' * 45)
for c, j in enumerate(jogadores):
    print(f'{c:>3}', '', f'{ j["nome"]:<12}', f'{str(j["gols"]):<18}', f'{sum(j["gols"])}')
print('-' * 45)

resp = 0
while resp != 999:
    resp = int(input('Mostrar dados de qual jogador? (999 interrompe): '))
    while len(jogadores) <= resp < 999:
        print(f'ERRO! Não existe jogador com código {resp}!')
        print('-' * 45)
        resp = int(input('Mostrar dados de qual jogador? (999 interrompe): '))
    if resp != 999:
        print(f' -- LEVANTAMENTO DO JOGADOR {jogadores[resp]["nome"]:}')
        for c, gols in enumerate(jogadores[resp]['gols']):
            print(f'    No jogo {c+1} fez {gols} gol(s).')
print('-='*45, '\n<< VOLTE SEMPRE >>')