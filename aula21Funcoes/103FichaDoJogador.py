# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e
# quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha
# sido informado


def getFichaDoJogador(nome='<desconhecido>', gols=0):
    return f'O jogador {nome} fez {gols} gol(s) no campeonato.'


print('-'*30)
nome = input('Nome do Jogador: ')
gols = input('Nome do Jogador: ')


if nome.replace(' ', '') == '':
    if gols.isnumeric():
        gols = int(gols)
        print(getFichaDoJogador(gols=gols))
    else:
        print(getFichaDoJogador())
elif gols.isnumeric():
    gols = int(gols)
    print(getFichaDoJogador(nome, gols))
else:
    print(getFichaDoJogador(nome=nome))
