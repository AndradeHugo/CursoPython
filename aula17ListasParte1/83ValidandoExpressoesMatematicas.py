# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

# Solucao sem lista (Minha)
# exp = input('Digite uma expressão:')
# aberturas = 0
# fechamentos = 0
#
# for c in range(0, len(exp)):
#     if exp[c:c+1] == '(':
#         aberturas += 1
#     elif exp[c:c+1] == ')':
#         fechamentos += 1
# if aberturas == fechamentos:
#     print('Sua expressão é válida!')
# else:
#     print('Sua expressão NÃO é válida!')


# Solucao com lista (Guanabara)
exp = input('Digite uma expressão:')
lista = list()
for c in exp:
    if c == '(':
        lista.append(c)
    elif c == ')':
        if lista:
            lista.pop()
        else:
            lista.append(c)
            break
if lista:
    print('Sua expressão NÃO é válida!')
else:
    print('Sua expressão é válida!')
