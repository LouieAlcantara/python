def contador(i, f, p):
    print(f'Esses são os numeros de {i} a {f} de {p} em {p}.')
    cont = i
    while cont <= f:
        print(f'{cont}', end=' ')
        cont += p
    cont = i
    while cont >= f:
        print(f'{cont}', end=' ')
        cont -= p
    print('fim')



contador(1, 10, 1)
contador(90, 60, 2)
contador(182, 45, 8)
contador(104, 114, 2)