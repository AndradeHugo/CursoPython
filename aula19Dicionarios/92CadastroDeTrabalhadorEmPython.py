# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime

dados = dict()

dados['nome'] = input('Nome: ')
anoNascimento = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.today().year - anoNascimento
carteira = int(input('Carteira de Trabalho (0 não tem): '))
if carteira > 0:
    dados['ctps'] = carteira
    anoContrato = int(input('Ano de Contratação: '))
    dados['anoContrato'] = anoContrato
    dados['salario'] = float(input('Salário: '))
    aposentadoria = (anoContrato - anoNascimento) + 35
    dados['aposentadoria'] = aposentadoria
print('-=' * 30)
for k, v in dados.items():
    print(f'  - {k} tem o valor {v}.')
