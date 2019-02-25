# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python,
# só que fazendo a validação para aceitar apenas um valor numérico.


def lerInteiro(txt):
    n = input(txt)
    while not n.isnumeric():
        if n[0:1] == '-':
            n = n[1:]
            if n.isnumeric():
                return '-' + n
        print('ERRO! Digite um número inteiro válido.')
        n = input(txt)
    return n


n = lerInteiro('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')
