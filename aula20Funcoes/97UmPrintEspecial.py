def escrever(txt):
    tam = len(txt) + 4
    print('~' * tam)
    print(f'{txt:^{tam}}')
    print('~' * tam)


escrever('Hugo Andrade')
escrever('Python')
escrever('25')
