# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

tabela = ('Palmeiras', 'Internacional', 'Flamengo', 'São Paulo', 'Grêmio', 'Atlético-MG', 'Santos', 'Cruzeiro ',
          'Atlético-PR', 'Fluminense', 'Bahia', 'Corinthians', 'Vasco', 'Botafogo', 'Ceará', 'Sport', 'Vitória',
          'América-MG', 'Chapecoense', 'Paraná Clube')

print(f'Os cinco primeiros colocados são: {tabela[:5]}')
print(f'Os quatro últimos colocados são: {tabela[-4:]}')
print(f'Os times em ordem alfabética: {sorted(tabela)}')
print(f'A Chapecoense está na posição {tabela.index("Chapecoense")+1}')
