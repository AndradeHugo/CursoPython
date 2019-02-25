# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de
# uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.


def verificarSituacaoVoto(anoNasc):
    from datetime import datetime
    anoAtual = datetime.now().year
    idade = anoAtual - anoNasc
    padrao = f'Com {idade} ano(s): '
    if 18 <= idade <= 65:
        return padrao + 'VOTO OBRIGATÓRIO'
    elif idade < 16:
        return padrao + 'NÃO VOTA'
    else:
        return padrao + 'VOTO OPCIONAL'


print('-'*30)
print(verificarSituacaoVoto(int(input('Em que ano você nasceu: '))))
