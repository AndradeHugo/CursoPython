# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

nome = input('Nome: ')
media = float(input(f'Média do(a) {nome}: '))
if media >= 7.0:
    situacao = 'Aprovado'
else:
    situacao = 'Recuperação'

ficha = {'nome': nome, 'média': media, 'situação': situacao}
for k, v in ficha.items():
    print(f'- {k} é igual a {v}')