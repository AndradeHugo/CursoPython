# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar
# as notas de cada aluno individualmente.

diario = list()
aux = list()
resp = 'S'
while resp in ('S', 's', 'SIM', 'sim'):
    aux.append(input('Nome: '))
    aux.append(float(input('Nota 1: ')))
    aux.append(float(input('Nota 2: ')))
    diario.append(aux[:])
    aux.clear()
    resp = input('Deseja continuar? [S/N]')
print('-=' * 30)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for numero, aluno in enumerate(diario):
    print(f'{numero:<4}{aluno[0]:<10}{(aluno[1] + aluno[2]) / 2:>8.1f}')
print('-' * 26)
resp = 0
while resp != 999:
    resp = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if resp != 999:
        print(f'Notas de {diario[resp][0]} são {diario[resp][1:3]}')
print('FINALIZANDO...\n<<< VOLTE SEMPRE >>>')
