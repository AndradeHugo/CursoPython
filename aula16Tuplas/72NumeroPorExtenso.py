# Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
           'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

posicao = int(input('Digite um número de 0 a 20:'))
while posicao < 0 or posicao > 20:
    posicao = int(input('Tente novamente um número de 0 a 20:'))

print(f'O número que você escolheu foi o {numeros[posicao]}.')