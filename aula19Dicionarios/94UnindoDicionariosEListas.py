# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário
# e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

pessoas = list()
pessoa = dict()
somaIdades = 0
resp = 'S'
while resp in ('S', 's'):
    pessoa['nome'] = input('Nome: ')
    sexo = input('Sexo [M/F]: ')
    while sexo not in ('M', 'F', 'm', 'f'):
        print('ERRO! Responda apenas M ou F.')
        sexo = input('Sexo [M/F]: ').upper()
    pessoa['sexo'] = sexo
    pessoa['idade'] = int(input('Idade: '))
    somaIdades += pessoa['idade']
    pessoas.append(pessoa.copy())
    resp = input('Deseja continuar? [S/N] ')
    while resp not in ('S', 's', 'N', 'n'):
        print('ERRO! Responda apenas S ou N.')
        resp = input('Deseja continuar? [S/N] ')
print('-=' * 30)

print(f'A) Ao todo, temos {len(pessoas)} pessoa(s) cadastrada(s).')
media = somaIdades / len(pessoas)
print(f'B) A média de idade é de {media:5.2f} anos.')
print(f'C) As mulheres cadastradas foi(foram) ', end='')
for p in pessoas:
    if p['sexo'] in ('F', 'f'):
        print(f'{p["nome"]} ', end='')
print(f'\nD) Lista da(s) pessoa(s) que está(ão) acimda da média: ')
for p in pessoas:
    if p['idade'] > media:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')






