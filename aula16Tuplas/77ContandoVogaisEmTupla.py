# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('gerar', 'uma', 'palavra', 'sem', 'que', 'outras', 'pessoas', 'a', 'vejam')

for palavra in palavras:
    print(f'Na palavra {palavra.upper()} temos ', end='')
    for letra in range(0, len(palavra)):
        if palavra[letra].upper() in ('A', 'E', 'I', 'O', 'U'):
            print(f'{palavra[letra]} ', end='')
    print('')
